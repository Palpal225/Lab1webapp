from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, \
    CategoryDetail, CategoryCreate, CategoryUpdate, CategoryDelete, ExportPDFView
from django.contrib.auth.views import LogoutView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category'),
    path('category-create/', CategoryCreate.as_view(), name='category-create'),
    path('category-update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
    path('category-delete/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),
    path('export-pdf/', ExportPDFView.as_view(), name='export-pdf'),
]
urlpatterns += [
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]