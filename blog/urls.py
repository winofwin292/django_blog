from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_post, name='search_post'),
    path('contact/', views.add_contact_save, name='contact'),
    path('blog/', views.all_post, name='all_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/add_comment_save/', views.add_comment_save, name='add_comment_save'),
    path('categories/<slug:category_slug>/', views.get_post_by_category, name='get_post_by_category'),
]
