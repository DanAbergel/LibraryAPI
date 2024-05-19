from fastapi import FastAPI
from routes.route import router

app = FastAPI(
    title="Library Manager",
    summary="Application which manages a library , and makes easier to order a book online"
)

app.include_router(router)