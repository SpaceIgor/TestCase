from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('expenses/', views.ExpenseListCreate.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view(), name='expense-detail'),
    path('expenses/user/<int:user_id>/date_range/<str:start_date>/<str:end_date>/', views.list_expenses_by_date_range, name='list-expenses-by-date-range'),
    path('expenses/user/<int:user_id>/summary/<int:year>/<int:month>/', views.category_summary, name='category-summary'),
]
