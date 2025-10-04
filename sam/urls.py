from django.urls import path
from sam.views import *



urlpatterns=[
 
    path('three',pro,),
    path('four',add,name='addpro'),
    path('five/<int:id>',edit,name='edit'),
    path('six/<int:pid>',deletes,name='del'),

]