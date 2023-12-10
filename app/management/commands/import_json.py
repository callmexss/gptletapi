import os
import json
from dotenv import load_dotenv
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model

from app.models import GPTEntry


load_dotenv()


def import_gpt_entries(json_file_path):
    with open(json_file_path, 'r') as file:
        gpt_entries = json.load(file)

    cnt = 0
    for entry in gpt_entries:
        try:
            _, created = GPTEntry.objects.get_or_create(
                name=entry['title'],
                author=entry['author'],
                description=entry['description'],
                image_url=entry['logoUrl'] if entry['logoUrl'] else os.environ['logoUrl'],
                link_url=entry['url'],
                unique_link_url=entry['url'],
            )
            if created:
                cnt += 1
        except Exception as err:
            print(err)
    print(f'total {cnt} new gptlet added.')


class Command(BaseCommand):
    help = "Import gpts from json file."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        json_file = options['json_file']
        import_gpt_entries(json_file)
