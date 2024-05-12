import enum


@enum.unique
class SystemErrorCode(str, enum.Enum):
    '''Системные ошибки нашего сервиса.
    Такие ошибки не кидаются вручную из кода,
    сам exception_handler ловит исключения типа Exception или
    HTTPException(который был выкинут где то вглубине FastAPI)
    и приводит эти исключения к общему виду, например с code=UNKNOWN'''

    SCHEMAVIOLATED = 'SCHEMAVIOLATED'
    INTERNAL = 'INTERNAL'
    METHODNOTALLOWED = 'NOTALLOWED'
    NOTFOUND = 'NOTFOUND'
    UNKNOWN = 'UNKNOWN'


@enum.unique
class AppErrorCode(str, enum.Enum):
    '''Ошибки бизнес логики приложения.
    По возможности делайте их максимально переиспользуемыми,
    например MTSPAYFAILED не самый лучший пример ошибки, в отличие от RESOURCENOTFOUND'''

    BADREQUEST = 'BADREQUEST'
    FORBIDDEN = 'FORBIDDEN'
    MTSPAYFAILED = 'MTSPAYFAILED'
    RESOURCECONFLICT = 'RESOURCECONFLICT'
    RESOURCENOTFOUND = 'RESOURCENOTFOUND'
    UNAUTHORIZED = 'UNAUTHORIZED'
