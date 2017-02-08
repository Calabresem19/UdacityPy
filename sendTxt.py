from twilio.rest import TwilioRestClient

account_sid = "AC994df2f38186b709dd174deca3b8aa7e" # Your Account SID from www.twilio.com/console
auth_token  = "70dcf1aae988ff8b42eabd6b989bb3e2"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello  from Python",
    to="+14124003808",    # Replace with your phone number
    from_="+14124447230") # Replace with your Twilio number

print(message.sid)
