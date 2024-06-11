import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

#websockets
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from main_user import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shapy_backnd.settings')

shapy_application = get_asgi_application()

#router to handle websockets
application = ProtocolTypeRouter({
    "http": shapy_application,
    #only let host that we allowed to have websockets
    "websocket" : AllowedHostsOriginValidator(
        #use django auth to give access to logged in user
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    )
})

app = shapy_application