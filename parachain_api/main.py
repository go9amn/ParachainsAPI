from fastapi import FastAPI

from core.settings.settings import settings


app = FastAPI(title=settings.app.project_name)
