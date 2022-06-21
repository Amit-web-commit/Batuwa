from django.urls import path, include
from .import views
from django.views.generic import TemplateView
app_name = 'UserAdmin'

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('categories/', views.addCategories, name="categories"),
    path('categories/<int:pk>/delete/', views.deleteCategories, name="deleteCategories"),
    path('<int:id>', views.updateCategories, name="updateCatagories"),
    path('projects/', views.projects, name="projects"),
    path('users/', TemplateView.as_view(template_name = 'users.html'))
]