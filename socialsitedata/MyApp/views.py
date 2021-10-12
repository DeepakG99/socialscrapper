from django.shortcuts import render, redirect
from MyApp import connections as conn
from MyApp import constants
from MyApp.models import *
import json
import pymongo

# Create your views here.


# index page

def Homepage(request):
    return render(request,'index.html')

def getTwitter(request):
    Twitter_data()
    return redirect('/')



def Twitter_data(request):
    conn.twitterCol.drop()

    i = 1
    for status in conn.twitterAPI.user_timeline(user_id='32968470'):
        print(status)
        tweetData = {
            "status_num": i,
            "status_text": status.text,
            "status_name": status.user.name,
            "status_created_at": status.created_at,
            "status_favourate_Count": status.favorite_count,
            "status_lang": status.lang
        }
        conn.twitterCol.insert_one(tweetData)
        conn.db.heights.create_index([('name', pymongo.ASCENDING)], unique=True)
        print(tweetData['status_text'])
        i+=1
        cc = twitter.objects.create(status_num=tweetData['status_num'],status_name=tweetData['status_name'], status_text=tweetData['status_text'],
                                    status_created_at=tweetData['status_created_at'],status_favourate_Count=tweetData['status_favourate_Count'], status_lang=tweetData['status_lang'])
        cc.save()

    tweets = twitter.objects.all()
    context = {
        "tweet":tweets
    }
    return render(request,'twitter.html', context)


def getTumblerdata(request):
    conn.tumblerrCol.drop()
    data = conn.tumblrClient.posts(constants.tumblr.BLOG_NAME)

    postdata = []
    p = data['posts']
    print(p)
    i =1
    for element in p:
        traildata = element['trail']
        blogContent = ""
        for blog in traildata:
            blogContent = blog['content']
        data = {
            "post_number": i,
            "post_type": element['type'],
            "post_url": element['post_url'],
            "post_created_at": element['date'],
            "post_tittle": element['summary'],
            "post_content": blogContent
        }
        postdata.append(data)
        print(data)
        i+=1
        final_data = {"post_data":postdata}
        conn.tumblerrCol.insert_one(final_data)
        ff = trumbler.objects.create(status_num=data['post_number'],status_name=data['post_type'], status_text=data['post_tittle'],
                                    status_created_at=data['post_created_at'],status_favourate_Count=data['post_content'], status_lang=data['post_url'])
        ff.save()
    tt = trumbler.objects.all()
    context = {
        "tt":tt
    }
    return render(request, 'tumbler.html', context)