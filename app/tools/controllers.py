from twilio.rest import Client

account_sid = 'AC3302c5571759108eb1fdb45f8a002eeb'
auth_token = '039b5d9abb599eef4a7623f183aa6f24'
client = Client(account_sid, auth_token)
from_number = 'whatsapp:+14155238886'
to_number = 'whatsapp:+34690663097'
client.messages.create(
    body='Hello!',
    from_=from_number,
    to=to_number)