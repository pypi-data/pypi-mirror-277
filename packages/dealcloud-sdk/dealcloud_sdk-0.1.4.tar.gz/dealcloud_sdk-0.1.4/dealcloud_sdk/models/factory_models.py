from pydantic import BaseModel


class DealCloudFactoryArgs(BaseModel):
    site_url: str
    client_id: str | int
    client_secret: str
