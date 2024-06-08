from __future__ import annotations

from pydantic import BaseModel
from typing import Optional


class DateObserved(BaseModel):
    type: str
    value: str


class Payload(BaseModel):
    victimid: str
    name: Optional[str] = None
    surname: Optional[str] = None
    dateofbirth: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    encounterdatetime: Optional[str] = None
    triagestatus: Optional[str] = None
    totalgcs: Optional[int] = None
    dttid: Optional[str] = None
    currentdisposition: Optional[int] = None
    incidentid: Optional[str] = None
    contamination: Optional[bool] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    chiefcomplaint: Optional[str] = None
    chiefcomplaintname: Optional[str] = None
    pregnant: Optional[bool] = None
    gcseye: Optional[int] = None
    gcsverbal: Optional[int] = None
    gcsmotor: Optional[int] = None
    nickname: Optional[str] = None


class Model(BaseModel):
    id: str
    type: str
    dateObserved: DateObserved
    payload: Payload
