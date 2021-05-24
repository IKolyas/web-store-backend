from django.urls import path, re_path
from userprofile.views import UserProfileView

app_name = 'userprofile'

urlpatterns = [
    # path('products/', ProductsFilterCategoryView.as_view(), name='product_filter'),
    path('profile/', UserProfileView.as_view(), name='userprofile')
]
