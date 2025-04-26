from django.urls import path
from .views import BlogMixinView,BlogDetailMixinView,BlogCommentMixinView,BlogCommentDetailMixinView
urlpatterns = [
	path('11B/',BlogMixinView.as_view()),
	path('11B/int/<int:pk>/',BlogDetailMixinView.as_view()),
	path('22BC/',BlogCommentMixinView.as_view()),
	path('22BC/int/<int:pk>/',BlogCommentDetailMixinView.as_view())

]