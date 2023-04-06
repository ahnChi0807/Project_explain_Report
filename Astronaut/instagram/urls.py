
from django.contrib import admin
from django.urls import path
from .views import Sub
from content.views import Main
# content는 다른 폴더에 있는 views파일을 접근하는것이므로 .키워드는 사용하지 않습니다.
# 키워드 .이란? 나랑 같은 소스 폴더에 있는 걸 가르키는 것 입니다. 즉 .views하면 views.py를 가르킵니다.

# views 파일에 있는 Sub 클래스를 가져오기 위한 import
# urlpatterns는 서버 주소 뒤에 특정 주소를 더해서 어떤 프로그램을 실행시킬지 결정해주는 역할입니다.
# path(사용자 어떤 주소로 접속했는지, 해당 주소로 접속시 실행할 내용), 형식 : path('url', View)
# http://127.0.0.1:8005/admin/으로 접속하면 admin.site.urls를 실행한다는 의미입니다.
urlpatterns = [
    path('admin/', admin.site.urls),
    #as.view란? Sub 클래스를 view로 사용하겠다는 의미, 저 자리에는 무조건 view가 와야합니다.
    path('main/', Main.as_view())
]
