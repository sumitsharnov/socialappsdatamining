import os
import json
import facebook
import requests
import shutil
from django.core.management import BaseCommand
from socialapps.management.commands.datauploadfacebook import FbUpload
from socialapps.management.commands.facebook import Fb
from socialapps.management.commands.twitterpost import StdOutListener
from socialapps.models import Item

class Command(BaseCommand):
    def handle(self, *args, **options):
        fb = Fb()
        print("Connecting to facebook")
        print(Item.objects.values('image_url').count())
        token = 'EAAC11grBRhMBACGfKciBTS3xOyBB5f8MUfwvHAkmfZBfa5QZAdBRpku5KzjWjdgLgUJX8YRKms1RIX99ffsheI4tItzsgmdrnxZA8w167jdHVZAeGMxZCXBVc2ZAqN8MMRsQq3y7e5b336N7izo8iTs4DK4RTbRgxLZBR67dDOskQZDZD'
        graph = facebook.GraphAPI(token)
        fb.fb(graph)
        #graph.put_object(parent_object="me", connection_name="feed", message="Sumit")
        #graph.put_wall_post('Sumit')

    def upload_image(self,image_name):
        fbUpload = FbUpload()
        user_page_token = 'EAAC11grBRhMBAIHhW1TKxsP4ZAYlLYzRqmyLlF2IbZBISlikZC6pZCNq5CSUo9nG6TKwsXJbC96wiXqAtpO9OxbIfJLtiSFOpj04aYPN6kPM1lni4jZAVn7rhCF0n1tKX02ooKwxmHczi0l7IzdlPZCHZCmzZBkO1nBgcxq6M43dwAZDZD'
        graph_user_page = facebook.GraphAPI(user_page_token)
        fbUpload.fbUpload(graph_user_page, image_name)

    def tweetpost(self, userpost):
        listener = StdOutListener()
        listener.twitterpost(userpost)
