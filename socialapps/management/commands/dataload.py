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
        token = 'EAAC11grBRhMBAOVDZAhzBe2XOgIecNkZB6euD2r250QOhvN8Ukbh9BimFKEBJChu7Vo28y4a4BEMylOtJafo8Oue5hu0ZCL3idhvZCrP1sj9E5ZA9ZAiBaCUuBspkizxAaeOrVoao6VOupjizKLHerRJODJviQSZACaFRBTVNnIad4DzwnyHweI4YZC0JK8blVAetpUQlrmlVDD8UgtP9TusjCtW8njA8T9uY3NUmEZAlcQZDZD'

        graph = facebook.GraphAPI(token)
        fb.fb(graph)
        #graph.put_object(parent_object="me", connection_name="feed", message="Sumit")
        #graph.put_wall_post('Sumit')
