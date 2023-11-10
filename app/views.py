from gptbase import base
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

from common.applet import Applet, extract_info_from_link
from .models import App, GPTEntry
from .serializers import AppSerializer, GPTEntrySerializer, URLSerializer


def build_applet_from_model(app: App):
    return Applet(app.name, app.system_prompt, app.prompt)


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer


@method_decorator(ratelimit(key='ip', rate='5/d', method='POST'), name='post')
class OpenAIView(APIView):
    def post(self, request, *args, **kwargs):
        app_id = request.data.get("id")
        content = request.data.get("content")

        app = get_object_or_404(App, id=app_id)
        applet = build_applet_from_model(app)
        chat_comp = applet.ask(content)
        chunks = base.get_chunks(chat_comp)

        return StreamingHttpResponse(chunks)


class GPTEntryViewSet(viewsets.ModelViewSet):
    queryset = GPTEntry.objects.all()
    serializer_class = GPTEntrySerializer


class URLProcessView(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            try:
                entry = extract_info_from_link(url)
                entry, _ = GPTEntry.objects.get_or_create(
                            name=entry['name'],
                            description=entry['description'],
                            image_url=entry['image_url'],
                            link_url=entry['link_url']
                        )
                return Response(
                    {"message": "Entry created successfully"},
                    status=status.HTTP_201_CREATED)
            except Exception as err:
                print(err)
        return Response(serializer.errors, status=400)
