from django.urls import path
from .views import HomeView, ArticleDetailsView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article_details'),
    path('add_post/>', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_category/>', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='categories'),
    path('category-list', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/>', AddCommentView.as_view(), name='add_comment'),

]
