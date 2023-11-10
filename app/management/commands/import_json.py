import json
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model

from app.models import GPTEntry


def import_gpt_entries(json_file_path):
    with open(json_file_path, 'r') as file:
        gpt_entries = json.load(file)

    for entry in gpt_entries:
        GPTEntry.objects.get_or_create(
            name=entry['name'],
            description=entry['description'],
            image_url=entry['image_url'],
            link_url=entry['link_url']
        )


class Command(BaseCommand):
    help = "Import gpts from json file."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        json_file = options['json_file']
        import_gpt_entries(json_file)
