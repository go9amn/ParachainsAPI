from fastapi import FastAPI

from core.settings.settings import settings
from parachain_infos.routers.routers import router as infos_router


app = FastAPI(title=settings.app.project_name)
app.include_router(infos_router)
