import os
import sys
import urllib.request
import requests

from django.shortcuts import render

def search(request):

    if request.method == 'GET':

        client_id = "xRYnb6eMOqN65bEi4Ex0"
        client_secret = "FYZ7guPcsw"
        #url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
        url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

        image = request.FILES['image']
        print(image)        
        files = {'image': open("/users/red.png", 'rb')}
        print(files)
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url,  files=image, headers=headers)
        rescode = response.status_code
        if(rescode==200):
            # print (response.text)
            return render(request, 'search.html', {'test': response.text})
        else:
            print("Error Code:" + rescode)