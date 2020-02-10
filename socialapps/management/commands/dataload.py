import os
import json
import facebook
import requests
import shutil
from django.core.management import BaseCommand

from socialapps.management.commands.facebook import Fb
from socialapps.models import Item

class Command(BaseCommand):
    def handle(self, *args, **options):
        fb = Fb()
        print("Connecting to facebook")
        print(Item.objects.values('image_url').count())
        token = 'EAAC11grBRhMBAF1BkDPmZBCQXcotle3DwT3P9NsNxwwMbSII8NCbbqPc0dwFISGyXZA7rmuAyDHOHoWdrT2aRwOJryUHP1q1uya88ZBd1VmSyMlOUtk1xcdfsUOJ6r3HJZAyaLJlmerkDA3mnGPkKTfey97Sr7m5G9sou8kGlOaJashrQcuk9fHz4Kh6cZCZAeBySGrrjXNHVJAYtbS3N8i3xqy0YfYXHnnoZAnVhd68AZDZD'
        graph = facebook.GraphAPI(token)
        fb.fb(graph)
