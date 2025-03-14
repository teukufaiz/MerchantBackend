from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import loan
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import json

@csrf_exempt
def create_loan(request):
    data = json.loads(request.body)
    user_id = data.get("user_id")
    amount = data.get("amount")
    loan_term = data.get("loan_term")
    status = "Diproses"  # Default status saat pengajuan
    
    new_loan = loan.objects.create(user_id_id=user_id, amount=amount, status=status, loan_term=loan_term)
    return JsonResponse({"message": "Loan created successfully", "loan_id": new_loan.loan_id}, status=200)


def get_loans(request, user_id):
    loans = loan.objects.filter(user_id=user_id)
    loan_list = [{
        "loan_id": l.loan_id,
        "amount": l.amount,
        "status": l.status,
        "loan_term": l.loan_term,
        "created_at": l.created_at.strftime("%Y-%m-%d %H:%M:%S")
    } for l in loans]
    return JsonResponse({"loans": loan_list}, safe=False)


def total_approved_loans(request, user_id):
    total = loan.objects.filter(user_id=user_id, status="Diterima").aggregate(Sum('amount'))['amount__sum'] or 0
    return JsonResponse({"total_approved_loans": total})

@csrf_exempt
def update_loan_status(request, loan_id):
    data = json.loads(request.body)
    new_status = data.get("status")
    
    loan_obj = get_object_or_404(loan, loan_id=loan_id)
    loan_obj.status = new_status
    loan_obj.save()
    
    return JsonResponse({"message": "Loan status updated successfully"})

@csrf_exempt
def delete_loan(request, loan_id):
    loan_obj = get_object_or_404(loan, loan_id=loan_id)
    loan_obj.delete()
    return JsonResponse({"message": "Loan deleted successfully"})