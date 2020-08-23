from django.urls import path,include
from basic_app import views

app_name='basic_app'
urlpatterns = [
    path('',views.login_register,name='login_register'),
    path('index/',views.index,name='index'),
    path('manage_acc/<username>',views.acc,name='acc'),
    path('upload/<username>',views.upload,name='upload'),
    path('save/<username>',views.save,name='save'),
    path('change/<username>',views.change,name='change'),
    path('update/<username>',views.update,name='update'),
    path('show/<username>',views.show,name='show'),
    path('apply/<username>',views.apply,name='apply'),
    path('logout',views.user_logout,name='user_logout'),
]