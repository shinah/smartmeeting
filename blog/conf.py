from django.conf import settings


CHAT_ROUTER = getattr(settings, 'ROUTER', 'blog.message_router.MessageRouter')
CHAT_ENGINE = getattr(settings, 'ENGINE', 'blog.engine')
