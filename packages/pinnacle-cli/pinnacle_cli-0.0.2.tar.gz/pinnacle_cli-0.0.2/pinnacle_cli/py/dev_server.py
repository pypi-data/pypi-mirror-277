from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pinnacle_python.endpoints import endpoints
from pinnacle_cli.constants import DIRECTORY
from pinnacle_cli.py.import_modules import import_modules
import json

import_modules()

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def route_factory(http_method, endpoint):
    route_name = endpoint.__name__
    params = endpoint.__annotations__.items()

    @app.api_route(f"/{route_name}", methods=[http_method])
    async def route_handler(request: Request):
        body = await request.body()
        if body:
            params = json.loads(body)
        else:
            params = {}

        params_dict = {}

        for param, _ in params.items():
            if param != "return":
                params_dict[param] = params[param]

        return endpoint(**params_dict)

    return (route_name, params)


endpoints_data = {}
for http_method, endpoints in endpoints.items():
    for endpoint in endpoints:
        route_name, params = route_factory(http_method, endpoint)
        endpoints_data[route_name] = http_method

file_path = f"{DIRECTORY}/.metadata/py_endpoints.json"
with open(file_path, "w") as file:
    json.dump(endpoints_data, file)
