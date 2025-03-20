import json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populates the WomanProfile table with data from a JSON file.'

    def handle(self, *args, **options):
        with open('data.json', 'r') as f:
            data = json.load(f)

            for item in data:
                # WomanProfile.objects.create(
                #     name=item['name'],
                #     bio=item['bio'],
                #     field=item['field'],
                #     image_url=item['image_url'],
                #     timeline_events = item['timeline_events']
                # )
                print(item['name'])

        self.stdout.write(self.style.SUCCESS('Successfully populated WomanProfile table.'))