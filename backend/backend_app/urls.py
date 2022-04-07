import backend_app.views

from django.urls import path

urlpatterns = {
    path('admin/<str:module>/', backend_app.views.AdminView.as_view()),
    path('books/<str:module>/', backend_app.views.BooksView.as_view()),
    path('notice/<str:module>/', backend_app.views.NoticeView.as_view()),
    path('user/<str:module>/', backend_app.views.UserView.as_view()),
    path('record/<str:module>/', backend_app.views.RecordView.as_view()),
}