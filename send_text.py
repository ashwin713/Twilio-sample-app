from twilio.rest import TwilioRestClient

account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Your Account SID from www.twilio.com/console
auth_token  = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+919999999999",    # Replace with your phone number
    from_="+123456789") # Replace with your Twilio number

print(message.sid)
