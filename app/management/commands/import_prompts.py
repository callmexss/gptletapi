from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from app.models import App
from prompts import PROMPT_LIST


User = get_user_model()


class Command(BaseCommand):
    help = "Import prompts from prompts module."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        user = User.objects.get(id=1)
        for prompt in PROMPT_LIST:
            app, _ = App.objects.get_or_create(
                name=prompt.NAME,
                user=user,
            )
            app.author = prompt.AUTHOR
            app.description = prompt.DESCRIPTION
            app.system_prompt = prompt.SYSTEM_PROMPT
            app.prompt = prompt.PROMPT
            app.save()
            self.stdout.write(
                self.style.SUCCESS(f"create {prompt.NAME} executed successfully")
            )
