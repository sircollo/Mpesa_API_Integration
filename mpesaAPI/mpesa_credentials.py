from re import M
import requests
import json
from requests.auth import HTTPBasicAuth
import datetime
import base64
from datetime import datetime
import os

# Lipa Na Mpesa STK push and API integration
class MpesaC2bCredential:
  consumer_key = '2gQU9QrjknjknjnqkuTuZpvPSDEFCIUNINIUNIHNKh0gh3xchme52'
  consumer_secret = '4BHynXdxsdakilKKNIONonsonxpfMAAL7zc'
  api_URL='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
  
class MpesaAccessToken:
  r = requests.get(MpesaC2bCredential.api_URL,auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key,MpesaC2bCredential.consumer_secret))
  mpesa_access_token = json.loads(r.text)
  validated_mpesa_access_token = mpesa_access_token['access_token']
  
  
class LipaNaMpesaPassword:
  lipa_time = datetime.now().strftime("%Y%m%d%H%M%S")
  Business_short_code = '174379'
  passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
  data_to_encode = Business_short_code + passkey + lipa_time
  online_password = base64.b64encode(data_to_encode.encode())
  decode_password = online_password.decode('utf-8')
  
# End of Lipa Na Mpesa STK initialization