from django.conf import settings

import pusher


PUSH_CHANNEL_SIGNATURE = 'signatures'
PUSH_EVENTS = {
    PUSH_CHANNEL_SIGNATURE: ['new'],
}


##
# Pusher *singleton*

pusher_client = pusher.Pusher(
  app_id=settings.PUSHER_APP_ID,
  key=settings.PUSHER_KEY,
  secret=settings.PUSHER_SECRET,
  host=settings.PUSHER_HOST,
)
