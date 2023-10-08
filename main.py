from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.assistant import router as assistant_router


def application_factory() -> FastAPI:
    """"""
    app_ = FastAPI()

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app_.include_router(
        router=assistant_router,
        prefix="/v1/assistant"
    )

    return app_


app = application_factory()
