import os
import json
import facebook
import requests
import shutil
from django.core.management import BaseCommand
from socialapps.models import Item
from socialapps.models import MyPosts, MyInformation

profile = graph.get_object('me', fields='name,location{location}, gender, id, photos')