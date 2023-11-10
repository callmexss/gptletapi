from gptbase import base
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

from common.applet import Applet, extract_info_from_link, get_category_name
from .models import App, GPTEntry, Category
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
                info = extract_info_from_link(url)
                name=info['name']
                description = info['description']
                category_name = get_category_name(f'{name}\n{description}')
                category, _ = Category.objects.get_or_create(
                    name=category_name
                )
                _ = GPTEntry.objects.get_or_create(
                            name=name,
                            description=description,
                            image_url=info['image_url'],
                            link_url=info['link_url'],
                            category=category,
                        )
                return Response(
                    {"message": "Entry created successfully"},
                    status=status.HTTP_201_CREATED)
            except Exception as err:
                print(err)
        return Response(serializer.errors, status=400)
