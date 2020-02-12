import os
import json
import facebook
import requests
import shutil
from django.core.management import BaseCommand
from socialapps.models import Item
from socialapps.models import MyPosts, MyInformation, MyLikes
import requests
import time
from pymongo import MongoClient



class Fb():
    def fb(self, graph):
        profile = graph.get_object('me', fields='name,location{location}, gender, id, photos')
        photos = graph.get_object('me', fields='photos{images}')
        listofPhotos = photos['photos']['data']
        posts_fullPictures = graph.get_object('me', fields='posts{full_picture}')
        print(type(posts_fullPictures))
        listofPictures = posts_fullPictures['posts']['data']
        # print(listofPhotos)
        # for listofPictures_ID in posts_fullPictures:
        #     item = Item()
        #     item.image_id = listofPictures_ID.get('id')
        #     item.save()
        try:
            shutil.rmtree('images')
        except:
            print("Images folder doesn't exist")
        Item.objects.all().delete()
        for pictures in listofPictures:
            item = Item()
            if not pictures.get("full_picture") == None:
                item.image_url = pictures.get("full_picture")
                item.save()
                item.cache()
                item.save
        # try:
        #     client = MongoClient('mongodb+srv://sumit:Sumit@facebookdata-v6b32.mongodb.net/test?retryWrites=true&w=majority')
        #
        #     db = client.fbdata
        #     print(type(profile))
        #     data = dict(profile)
        #     print(type(data))
        #     db.fbuserdata.insert_one(data)
        #     print(json.dumps(profile, indent=4))
        # except:
        #     print("Momgo db is down")

        #Importing Posts data
        MyPosts.objects.all().delete()
        posts = graph.get_object('me', fields='posts{permalink_url,caption,created_time,name,type,status_type}')
        postsData = posts['posts']['data']
        for post in postsData:
            myPosts = MyPosts()
            if not post.get('permalink_url') == None:
                myPosts.post_url = post.get('permalink_url')
            if not post.get('type') == None:
                myPosts.status_type = post.get('type')
            if not post.get('status_type') == None:
                myPosts.status_source=post.get('status_type')
            if not post.get('caption') == None:
                myPosts.caption= post.get('caption')
            else:
                myPosts.caption="N/A"
            if not post.get('created_time') == None:
                myPosts.post_time = post.get('created_time')
            myPosts.save()

        #importing user personal MyInformation
        MyInformation.objects.all().delete()
        info = graph.get_object('me', fields='birthday,email,location,hometown,languages,first_name,last_name,friends')
        myInformation = MyInformation()
        if not info.get('first_name') is None:
            myInformation.user_first_name = info.get('first_name')
        if not info.get('last_name')==None:
            myInformation.user_last_name = info.get('last_name')
        if not info.get('birthday')==None:
            myInformation.birthday = str(info.get('birthday'))
        if not info.get('email')==None:
            myInformation.user_email = info.get('email')
        if not info.get('location').get('name')==None:
            myInformation.present_location =info.get('location').get('name')
        if not info.get('hometown').get('name')==None:
            myInformation.user_hometown = info.get('hometown').get('name')
        if not info.get('friends').get('summary').get('total_count')==None:
            myInformation.number_of_friends = info.get('friends').get('summary').get('total_count')
        try:
            lang_numbers= len(info.get('languages'))
            for loc in range(0,lang_numbers):
                if not info.get('languages')[loc].get('name') == None:
                    if loc==0:
                        myInformation.user_first_language = info.get('languages')[loc].get('name')
                    else:
                        myInformation.user_second_language = info.get('languages')[loc].get('name')
        except:
            myInformation.user_first_language = "N/A"
            myInformation.user_second_language = "N/A"
            print("no languages found")
        likes = graph.get_object('me', fields='likes{link,name}')
        number_of_likes = len(likes['likes']['data'])
        number_of_photos = Item.objects.values('image_url').count()
        number_of_posts = MyPosts.objects.values('post_url').count()
        myInformation.number_of_likes = number_of_likes
        myInformation.number_of_photos = number_of_photos
        myInformation.number_of_posts = number_of_posts
        myInformation.save()

        # MY likes unsuitable
        MyLikes.objects.all().delete()
        likes = graph.get_object('me', fields='likes{link,name}')
        number_of_likes = len(likes['likes']['data'])
        for like in likes['likes']['data']:
            myLikes = MyLikes()
            if not like.get('link')==None:
                myLikes.like_link = like.get('link')
            if not like.get('name')==None:
                myLikes.like_subject=like.get('name')
            myLikes.save()
