from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import Question
import requests


def index(request):
    # return HttpResponse("Hello fake response")
    questions = Question.objects.all()
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': questions
    }
    output = ",".join([q.question_text for q in questions])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def getPictures(request):
    lat = 37.7749295
    longt = -122.4194155
    access_token = '209911174.1fb234f.f16debe650484b16aa7675ff82da2284'
    url = "https://api.instagram.com/v1/media/search?access_token=%s&lat=%s&lng=%s&distance=2000"%(access_token, lat, longt)
    # import pdb;pdb.set_trace()
    # response = httpRequest(None, url, 'GET')
    response = requests.get(url)
    # print response.status_code
    # print response.content
    image_list = []
    import json
    data = json.loads(response.content)["data"]
    for d in data:
        image_list.append(d["images"]["standard_resolution"]["url"])

    context = {
        'images': image_list
    }

    # import pdb;pdb.set_trace()
    return render(request, 'polls/instagram.html', context)


def httpRequest(context, url, requestType):
    import httplib, urllib
    params = urllib.urlencode(context) if context else {}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(url)
    conn.request(requestType, "/cgi-bin/query", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    #output: 200 OK
    data = response.read()
    conn.close()
    return response


