from . import edit_profile
from . import misc
from . import p2p
from . import start


routers = (
    start.router,
    edit_profile.router,
    misc.router,
    p2p.router,
    )
