from starlette.routing import Route, Mount, WebSocketRoute
from investing_dashboard_backend.schema import schema
from strawberry.asgi import GraphQL

graphql_app = GraphQL(schema)

routes = [
    Mount('/', routes=[
        Route('/graphql', graphql_app),
        WebSocketRoute('/graphql', graphql_app),
    ])
]
