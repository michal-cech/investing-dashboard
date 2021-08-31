from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from investing_dashboard_backend.routing import routes


middleware = [
    Middleware(CORSMiddleware,
               allow_headers=["*"],
               allow_origins=["*"],
               allow_methods=["*"])
]
app = Starlette(routes=routes, middleware=middleware, debug=True)
