from django.urls import path,include
from user_admin import views1

app_name='user_admin'
urlpatterns = [
     path('acc/<username>',views1.acc,name='acc'),
     path('upload/<username>',views1.upload,name='upload'),
     path('save/<username>',views1.save,name='save'),
     path('change/<username>',views1.change,name='change'),
     path('update/<username>',views1.update,name='update'),
     path('add/<username>',views1.add,name="add"),
     path('save_challenge/<username>',views1.save_challenge,name="save_challenge"),
     path('edit/<username>',views1.edit,name='edit'),
     path('show/<username>',views1.show,name='show'),
     path('delete/<username>',views1.delete,name='delete'),
     path('admin_logout/',views1.user_logout,name='admin_logout'),
     path('applicants/<username>',views1.applicants,name='applicants'),
     path('complete/<username>',views1.complete,name='complete')
]