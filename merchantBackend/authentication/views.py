import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    deserialize = json.loads(request.body)
    phone_number = deserialize['phone_number']
    if User.objects.filter(phone_number=phone_number).exists():
        return JsonResponse({"error": "Phone number already exists"}, status=400)
    
    name = deserialize['name']
    password = deserialize['password']
    pin_code = deserialize['pin_code']
    business_name = deserialize['business_name']
    address = deserialize['address']
    user = User.objects.create(name=name, phone_number=phone_number, password=password , pin_code=pin_code, business_name=business_name, address=address)
    user.save()
    return JsonResponse({"message": "User registered successfully"})

@csrf_exempt
def login(request):
    deserialize = json.loads(request.body)
    phone_number = deserialize['phone_number']
    password = deserialize['password']
    if not User.objects.filter(phone_number=phone_number).exists():
        return JsonResponse({"error": "Phone number does not exist"}, status=400)
    user = User.objects.get(phone_number=phone_number)
    if user.password != password:
        return JsonResponse({"error": "Incorrect password"}, status=400)
    user_data = {
        "id": user.user_id,
        "name": user.name,
        "phone_number": user.phone_number,
        "pin_code": user.pin_code,
        "business_name": user.business_name,
        "address": user.address,
        "point": user.point,
    }
    return JsonResponse({"response": user_data}, status=200)