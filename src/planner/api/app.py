from __future__ import annotations

import uuid

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from planner.api.routes import router
from planner.engine.errors import PlannerError

app = FastAPI(title="Intent Planner", version="1.0.0")


@app.middleware("http")
async def correlation_middleware(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    return response


@app.exception_handler(PlannerError)
async def planner_error_handler(request: Request, exc: PlannerError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={
            "api_version": "v1",
            "request_id": request.state.request_id,
            "data": None,
            "error": {
                "code": exc.detail.code,
                "message": exc.detail.message,
                "context": exc.detail.context,
            },
        },
    )


app.include_router(router)
