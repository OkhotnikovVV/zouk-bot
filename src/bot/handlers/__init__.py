from . import edit_profile
from . import p2p
from . import start


routers = (
    start.router,
    edit_profile.router,
    p2p.router,
    )
