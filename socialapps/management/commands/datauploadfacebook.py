import os
import json
import facebook
import requests
import shutil
from django.core.management import BaseCommand
from socialapps.models import Item
from socialapps.models import MyPosts, MyInformation, MyLikes



class FbUpload():
    def fbUpload(self, graph, image_name):
        with open("media/%s" %(image_name),"rb") as image:
            graph.put_photo(image)
