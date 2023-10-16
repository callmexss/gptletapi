from gptbase import basev2
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse

from common.applet import Applet
from .models import App
from .serializers import AppSerializer


def build_applet_from_model(app: App):
    return Applet(app.name, app.system_prompt, app.prompt)


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class OpenAIView(APIView):
    def post(self, request, *args, **kwargs):
        app_id = request.data.get("id")
        content = request.data.get("content")

        app = get_object_or_404(App, id=app_id)
        applet = build_applet_from_model(app)
        chat_comp = applet.ask(content)
        chunks = basev2.get_chunks(chat_comp)

        return StreamingHttpResponse(chunks)
