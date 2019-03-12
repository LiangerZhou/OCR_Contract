from django.conf.urls import url,include
import myapp.views

urlpatterns = [
    url(r'add_book$',myapp.views.add_book, name='add_book'),
    url(r'show_books$',myapp.views.show_books, name='show_book'),
    # url(r'',myapp.views.index, name='index')
]