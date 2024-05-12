from fastapi import APIRouter

from core.settings.settings import settings
from accounts.routers.endpoints import accounts


router = APIRouter()

router.include_router(
    accounts.router,
    prefix=f'{settings.app.api_v1_str}/accounts',
    tags=['Информация об аккаунтах'],
)
