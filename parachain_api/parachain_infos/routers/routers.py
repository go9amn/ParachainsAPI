from fastapi import APIRouter

from core.settings.settings import settings
from parachain_infos.routers.endpoints import infos


router = APIRouter()

router.include_router(
    infos.router,
    prefix=f'{settings.app.api_v1_str}/infos',
    tags=['Информация о парачейне'],
)
