"""
URL configuration for ExcessFood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ExcessFoodApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="index"),
    path('loginDonor/', donorLogin, name="donorLogin"),
    path('signupDonor/', donorSignup, name="donorSignup"),
    path('sendOtp/', send_otp, name="send_otp"),
    path('verifyOtp/<int:id>', verify_otp, name="verify_otp"),
    path('logoutNow/', logout_all, name="logout_all"),
    path('addFood/<int:id>', add_food, name="add_food"),
    path('donorHome/', donorHome, name="donorHome"),
    path('getFood/<int:id>/<int:category>', get_food, name="get_food"),
    path('viewFood/<int:id>', view_food, name="viewFood"), # type: ignore
    path('changeFoodStatus/<int:id>/<int:value>', change_food_status, name="changeFoodStatus"), # type: ignore
    path('get_food_details/', get_food_to_edit, name="getFoodData"), # type: ignore
    path('deleteFood/<int:id>/', delete_food, name="deleteFood"), # type: ignore
    path('updateFood/', update_food, name="update_food"), # type: ignore
    path('viewRequest/', view_request, name="view_request"), # type: ignore

    # user
    path('loginUser/', userLogin, name="userLogin"),
    path('signupUser/', userSignup, name="userSignup"),
    path('userHome/', userHome, name="userHome"),
    path('profileInfo/<int:id>/<int:category>', profile, name="profiles"), # type: ignore
    path('ratings/<int:category>', ratings, name="ratings"), # type: ignore
    path('editProfile/<int:id>/<int:category>', editProfile, name="editProfile"), # type: ignore
    path('orderFood/', order_food, name="order_food"), # type: ignore
    path('viewHistory/', view_history, name="view_history"), # type: ignore
]


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
