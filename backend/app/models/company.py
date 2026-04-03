from pydantic import BaseModel

class Company(BaseModel):
    company: str
    CEO: str
    Founded: str
    Headquarters: str