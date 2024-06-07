from .input import Input
from .output import Output


if __name__ == "__main__":
    import json

    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi


    app = FastAPI()

    @app.post("/")
    def run(input: Input) -> Output:
        return None

    with open('openapi.json', 'w') as f:
        json.dump(get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ), f, indent=2)
