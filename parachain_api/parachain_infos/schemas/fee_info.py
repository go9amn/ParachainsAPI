from pydantic import BaseModel


class FeeInfo(BaseModel):
    name_for_keypair_by_uri: str
    value: int
