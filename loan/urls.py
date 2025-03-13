from django.urls import path
from .views import *

urlpatterns = [
    path('create_loan', create_loan, name='create_loan'),
    path('get_loans/<int:user_id>', get_loans, name='get_loans'),
    path('total_approved_loans/<int:user_id>', total_approved_loans, name='total_approved_loans'),
    path('update_loan_status/<int:loan_id>', update_loan_status, name='update_loan_status'),
    path('delete_loan/<int:loan_id>', delete_loan, name='delete_loan'),
]