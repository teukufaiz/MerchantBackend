import json
import bcrypt
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh["name"] = user.name
    refresh["phone_number"] = user.phone_number
    refresh["account_number"] = user.account_number
    refresh["business_name"] = user.business_name
    refresh["address"] = user.address

    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh),
    }

@csrf_exempt
def register(request):
    deserialize = json.loads(request.body)
    phone_number = deserialize['phone_number']
    hashing_password = bcrypt.hashpw(deserialize['password'].encode('utf-8'), bcrypt.gensalt())
    bcrypt_password = hashing_password.decode('utf-8')
    if User.objects.filter(phone_number=phone_number).exists():
        return JsonResponse({"error": "Phone number already exists"}, status=400)
    else:
        user = User(name=deserialize['name'], phone_number=phone_number, password=bcrypt_password, address=deserialize['address'],
                     account_number=deserialize['account_number'], business_name=deserialize['business_name'])
        user.save()
        return JsonResponse({'message': 'User created successfully'}, status=201)

@csrf_exempt
def login(request):
    deserialize = json.loads(request.body)
    phone_number = deserialize['phone_number']
    password = deserialize['password']
    if not User.objects.filter(phone_number=phone_number).exists():
        return JsonResponse({"error": "Phone number does not exist"}, status=400)
    user = User.objects.get(phone_number=phone_number)
    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    
    tokens = get_tokens_for_user(user)

    return JsonResponse({
            "message": "Login successful",
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
        }, status=200)