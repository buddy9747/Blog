from django.urls import path
from django.views.generic import ListView,DetailView
from  .import views
from Blog.models import blog

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('ms',ListView.as_view(queryset=blog.objects.all().order_by("-date")[:25],template_name="Blog/blog.html"),name='blog'),
    path('<int:pk>',DetailView.as_view(model=blog,template_name="Blog/post.html")),
]