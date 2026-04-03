
from fastapi import FastAPI
from app.routes import user_routes, finance_routes, dashboard_routes
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(finance_routes.router, prefix="/finance", tags=["Finance"])
app.include_router(dashboard_routes.router, prefix="/dashboard", tags=["Dashboard"])

@app.get("/")
def root():
    return {"message": "Finance Dashboard Backend Running"}
