import os
import json
from mitmproxy import http
from pinnacle_cli.constants import HOST, PORT, PYTHON_PORT, JAVASCRIPT_PORT, DIRECTORY

METADATA_DIR = os.path.join(os.getenv("PINNACLE_CWD") or "", DIRECTORY, ".metadata")
SERVER_PORTS = {"py": PYTHON_PORT, "js": JAVASCRIPT_PORT}


def load_endpoints():
    """
    Load the endpoints from the metadata directory (./.metadata/py_endpoints.json and ./.metadata/js_endpoints.json)

    Returns:
    endpoints: dict - The endpoints for the Python and JavaScript servers in the following format:
        {
            "py": {
                "endpoint_name": "HTTP_METHOD"
            },
            "js": {
                "endpoint_name": ""
            }
        }
    """
    endpoints = {"py": {}, "js": {}}
    with open(f"{METADATA_DIR}/py_endpoints.json", "r") as f:
        endpoints["py"] = json.load(f)
    with open(f"{METADATA_DIR}/js_endpoints.json", "r") as f:
        endpoints["js"] = json.load(f)

    print("Available Python endpoints:")
    for route_name, http_method in endpoints["py"].items():
        print(f"{http_method}: http://{HOST}:{PORT}/{route_name}")

    print("Available JavaScript endpoints:")
    for route_name in endpoints["js"]:
        print(f"http://{HOST}:{PORT}/{route_name}")
    return endpoints


def request(flow: http.HTTPFlow):
    endpoints = load_endpoints()
    pathname = flow.request.path.replace("/", "")

    if pathname in endpoints["py"]:
        flow.request.host = HOST
        flow.request.port = SERVER_PORTS["py"]
    elif pathname in endpoints["js"]:
        flow.request.host = HOST
        flow.request.port = SERVER_PORTS["js"]
    else:
        raise ValueError(f"Endpoint not found: {flow.request.path}")


load_endpoints()
