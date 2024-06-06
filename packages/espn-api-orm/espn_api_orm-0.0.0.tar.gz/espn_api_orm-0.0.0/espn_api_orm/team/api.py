from enum import Enum
from typing import Optional, List

from espn_api_orm.consts import ESPNSportTypes
from espn_api_orm.season.api import ESPNSeasonAPI
from espn_api_orm.team.schema import Team

class ESPNTeamAPI(ESPNSeasonAPI):
    """
    ESPN Team API for retrieving sport information about a specific team.

    Attributes:

    Methods:
    """

    def __init__(self, sport: ESPNSportTypes, league: str, season: int, team_id: int):
        """
        Initialize ESPNTeamAPI.
        """
        super().__init__(sport, league, season)
        self.team_id = team_id

    def get_team(self) -> Team:
        res = self.api_request(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/seasons/{self.season}/teams/{self.team_id}")
        if res is None:
            raise Exception(f'Invalid Season: {self.season} for {self.sport.value}/{self.league}')
        return Team(**res)

    ## statistics
    ## athletes
    ## injuries
    ## events
    ## schedule
    ## against the spread
