from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<id>\d+)$', views.books),
    url(r'^add_author_to_book/(?P<id>\d+)$', views.add_author_to_book),
    url(r'^authors$', views.author_page),
    url(r'^add_author$', views.add_author),
    url(r'^authors/(?P<id>\d+)$', views.authors),
    url(r'^add_book_to_author/(?P<id>\d+)$', views.add_book_to_author)
]