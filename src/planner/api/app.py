from fastapi import FastAPI

from planner.api.routes import router

app = FastAPI(
    title="Intent Planner",
    version="1.0.0"
)

app.include_router(router)
