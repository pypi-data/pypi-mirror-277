from __future__ import annotations

from pydantic import BaseModel

from datetime import datetime
from typing import List, Optional


class DateObserved(BaseModel):
    type: str
    value: datetime


class Payload(BaseModel):
    victimid: str
    incidentid: str
    devicetype: str
    respiratoryrate: Optional[float] = -1
    systolicbloodpressure: Optional[float] = -1
    diastolicbloodpressure: Optional[float] = -1
    temperature: Optional[float] = -1
    pulserate: Optional[float] = -1
    heartratevariability: Optional[float] = -1
    pulseoxymetry: Optional[float] = -1
    skinmoisture: Optional[float] = -1
    encounterdatetime: datetime


class Model(BaseModel):
    id: str
    type: str
    dateObserved: DateObserved
    payload: Payload
