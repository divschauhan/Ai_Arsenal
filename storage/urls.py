from os import name
from django.conf.urls import include
from django.urls import path
from .views import AiModelListView
from .views import upload_form,detail_of_ai_model,query_ai_models,download_file,review_form,edit_ai_model,delete_ai_model

urlpatterns = [
    path('',AiModelListView.as_view(), name='view_model'),
    path('model/<int:pk>',detail_of_ai_model, name='detail_model'),
    path('upload/',upload_form, name='upload_ai_model'),
    path('search/',query_ai_models, name='search_ai_model'),
    path('download/',download_file,name='download_ai_model'),
    path('review/<int:pk>',review_form,name='review_ai_model'),
    path('edit/<int:pk>',edit_ai_model,name='edit_ai_model'),
    path('delete/<int:pk>',delete_ai_model,name='delete_ai_model'),
    

]