from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! Test SMS 📱",
    from_="YOUR_TWILIO_NUMBER",
    to="YOUR_PHONE_NUMBER"
)

print("Message SID:", message.sid)