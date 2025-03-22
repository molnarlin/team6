import json
import os
from django.core.management.base import BaseCommand
from django.db import models

class Command(BaseCommand):
    help = 'Populates the WomanProfile table with data from a JSON file.'

    def handle(self, *args, **options):
        # Adjust base_dir to point to the project root
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        file_path = os.path.join(base_dir, 'category', 'management', 'commands', 'data.json')

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)

                for item in data:
                    # WomanProfile.objects.create(
                    #     name=item['name'],
                    #     bio=item['bio'],
                    #     field=item['field'],
                    #     image_url=item['image_url'],
                    #     timeline_events=item['timeline_events']
                    # )
                    print(item['name'])

            self.stdout.write(self.style.SUCCESS('Successfully populated WomanProfile table.'))
        except FileNotFoundError:
            self.stderr.write(f"File not found: {file_path}")

