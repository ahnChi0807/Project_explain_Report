from django.db import models
# 장고에 있는 models를 쓸 것이다 라고 알려주는 선언문
# Feed 클래스에서 models.Model 안에 코딩되어있는 내용을 상속 받아 가져다 쓰겠다라는 소리
class Feed(models.Model):
    content= models.TextField()         #글내용
    image = models.TextField()          #피드에 업로드되는 이미지
    profile_image = models.TextField()  #프로필 이미지
    user_id = models.TextField()        #글쓴이 ID
    like_count = models.IntegerField()  #좋아요 수