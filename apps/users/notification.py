from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message

def send_notification(user_ids,title, message, data):
      device = FCMDevice.objects.filter(user__in=user_ids).first()
      print(device)
      result = device.send_message(Message(data={
        "Nick" : "Mario",
        "body" : "great match!",
        "Room" : "PortugalVSDenmark"
   },))
      return result
   
    
    