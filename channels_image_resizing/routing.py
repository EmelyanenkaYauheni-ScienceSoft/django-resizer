from channels import route
from resizers.consumers import connect_blog, disconnect_blog


channel_routing = [
    route("websocket.connect", connect_blog, path=r'^/statistics/stream/$'),
    route("websocket.disconnect", disconnect_blog, path=r'^/statistics/stream/$'),
]
