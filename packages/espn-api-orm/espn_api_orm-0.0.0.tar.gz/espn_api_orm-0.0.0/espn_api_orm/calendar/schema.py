##################################
# Scoreboard Classes
##################################

from typing import List, Optional, Any

from pydantic import BaseModel, Field
import datetime

from espn_api_orm.consts import ESPNSportSeasonTypes
from espn_api_orm.generic.schema import Ref


class Calendar(BaseModel):
    ref: str = Field(..., alias='$ref')
    type: str
    startDate: datetime.datetime
    endDate: datetime.datetime
    eventDate: 'EventDate'
    sections: List['SeasonSection']
    season: Ref

    class EventDate(BaseModel):
        type: str
        dates: List[datetime.datetime]

    class SeasonSection(BaseModel):
        label: str
        detail: Optional[str] = None
        startDate: datetime.datetime
        endDate: datetime.datetime
        seasonType: Optional[Ref] = None


class CalendarDates(BaseModel):
    startDate: datetime.datetime
    endDate: datetime.datetime
    dates: List[datetime.datetime]
    seasonType: ESPNSportSeasonTypes
