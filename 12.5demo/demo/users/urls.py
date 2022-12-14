from django.urls import path
from users import account_handler, email
urlpatterns = [
    # modify, delete, add
    path('account_op/', account_handler.account_dispatcher),
    path('email/', email.email)

    #path('list/', views.display)
    
]