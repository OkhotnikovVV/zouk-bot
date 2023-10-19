# from admin import admin_router
# from organizator import organizator_router
# from user import user_router
from . import start
from . import edit_profile
from . import misc

routers = (
    start.router,
    edit_profile.router,
    misc.router,
    )
