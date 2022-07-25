from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import LipaNaMpesaPassword,MpesaAccessToken
import os
import environ
from django.conf import settings
from mpesa_api_test.settings import consumer_keys
env = environ.Env()
environ.Env.read_env()
# Create your views here.
# consumer_key = os.environ.get('consumer_key')
# Lipa Na Mpesa STK push and API integration
def getAccessToken(request):
  consumer_key = '2gQU9QrjknjknjnqkuTuZpvPSDEFCIUNINIUNIHNKh0gh3xchme52'
  consumer_secret = '4BHynXdxsdakilKKNIONonsonxpfMAAL7zc'
  api_URL='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
  
  r = requests.get(api_URL,auth=HTTPBasicAuth(consumer_key ,consumer_secret))
  mpesa_access_token = json.loads(r.text)
  validated_mpesa_access_token = mpesa_access_token['access_token']
  return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
  access_token = MpesaAccessToken.validated_mpesa_access_token
  api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
  headers = {'Authorization':'Bearer ' + access_token}
  request = {
      "BusinessShortCode": LipaNaMpesaPassword.Business_short_code,   
      "Password": LipaNaMpesaPassword.decode_password,    
      "Timestamp":LipaNaMpesaPassword.lipa_time,    
      "TransactionType": "CustomerPayBillOnline",    
      "Amount":"20000",    
      "PartyA": "254745095549",     
      "PartyB":"174379",    
      "PhoneNumber": "254745095549",   
      "CallBackURL":"https://mydomain.com/pat",   
      "AccountReference":"Collo",    
      "TransactionDesc":"Test"
  }
  response = requests.post(api_url, json=request, headers=headers)
  return HttpResponse(response,'success')

# End of Lipa Na Mpesa STK initialization