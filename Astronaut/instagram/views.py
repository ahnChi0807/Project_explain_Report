from django.shortcuts import render
from rest_framework.views import APIView


# APIView는 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할을 합니다.
# render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수이다.
# render를 사용하면 우리가 만든 html을 브라우저를 통해 보여줄 수 있습니다.
class Sub(APIView):
    # Sub클래스를 get으로 실행했을 때 main.html을 브라우저에 보여줌
    def get(self, request):
        print("Get으로 호출")
        return render(request, "instagram/main.html")

    # Sub클래스를 post로 실행했을 때 main.html을 브라우저에 보여줌
    def post(self, request):
        print("Post로 호출")
        return render(request, "instagram/main.html")
