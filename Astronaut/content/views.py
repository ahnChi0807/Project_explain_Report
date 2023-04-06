from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


# 키워드 .이란? 나랑 같은 소스 폴더에 있는 걸 가르키는 것 입니다. 즉 .models하면 models.py를 가르킵니다.
class Main(APIView):
    def get(self, request):
        # Feed에 있는 모든 데이터를 가져와서 feed_list에 저장하겠다
        # Feed.objects.all()는 select * from content_feed; 와 같은 것
        # 새롭게 추가된 게시글은 테이블의 최상단에 위치하게 됩니다.
        feed_list = Feed.objects.all().order_by('-id')
        for feed in feed_list:
            print(feed.content)
        # feeds (키이름, 이름은 사용자지정) = feed_list (키의 값, 위에서 구해온 값)
        return render(request, "instagram/main.html", context=dict(feeds=feed_list))
