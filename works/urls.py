from django.urls import path
from works.views import index


app_name = "works"


urlpatterns = [
    path("work/index/",index, name="index")

]
