from twilio.rest import Client


from decouple import config

def sending_sms(phone_num,otp):

    account_sid = config('TWILIO_ACCOUNT_SID')

    auth_token = config('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(

        from_='+19706994079',
        to=f'{phone_num}',
        body=f'Your OTP for Verification : {otp}'
          )
   

