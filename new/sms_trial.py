from twilio.rest import Client

account_sid="AC2a4f80ff9299572c1f0b3230ffa44481"
auth_token="f4d4246ca03645177e78103500f5228e"

str1="+918619537747"
client=Client(account_sid,auth_token)
message=client.messages.create(to=str1,from_="+12052366897",body="Someone plugged a usb!!!")

print(message.sid)
