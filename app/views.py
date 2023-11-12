from gptbase import base
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
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
    serializer_class = GPTEntrySerializer
    queryset = GPTEntry.objects.all()

    def get_queryset(self):
        queryset_cache = cache.get('gpt_entry_queryset')

        if not queryset_cache:
            queryset_cache = GPTEntry.objects.all()
            cache.set('gpt_entry_queryset', queryset_cache, 300)

        return queryset_cache


class URLProcessView(APIView):
    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            generate_category = serializer.validated_data['generate_category']
            print(generate_category)
            try:
                info = extract_info_from_link(url)
                name=info['name']
                description = info['description']
                image_url = info['image_url']
                if generate_category:
                    category_name = get_category_name(f'{name}\n{description}')
                    category, _ = Category.objects.get_or_create(
                        name=category_name
                    )
                else:
                    category = None

                entry, _ = GPTEntry.objects.get_or_create(
                    link_url=info['link_url'],
                )
                
                if name != entry.name:
                    entry.name = name
                if description != entry.description:
                    entry.description = description
                if image_url != entry.image_url:
                    entry.image_url=info['image_url']
                
                if not entry.category:
                    entry.category = category

                entry.save()
                
                return Response(
                    {"message": "Entry created successfully"},
                    status=status.HTTP_201_CREATED)
            except Exception as err:
                print(err)
        return Response(serializer.errors, status=400)
