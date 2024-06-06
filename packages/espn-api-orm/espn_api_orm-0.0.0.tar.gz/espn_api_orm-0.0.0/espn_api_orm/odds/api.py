from typing import Optional, List

from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.consts import ESPNSportTypes, ESPNSportSeasonTypes
from espn_api_orm.generic.schema import BaseType
from espn_api_orm.league.api import ESPNLeagueAPI
from espn_api_orm.scoreboard.schema import Scoreboard, Event



class ESPNOddsAPI(ESPNLeagueAPI):
    """
    ESPN Ods API for retrieving sport event odds.

    Methods:

    """

    def __init__(self, sport: ESPNSportTypes, league: str, event_id: int):
        """
        Initialize ESPNScoreboardAPI.
        """
        super().__init__(sport, league)
        self.event_id = event_id

    def get_odds(self, provider_id: int,limit:int=1000) :
        """
        Retrieve odds data for a specific provider.

        Args:


        Returns:

        """
        url = f"{self._core_url}/{self.sport.value}/leagues/{self.league}/events/{self.event_id}/competitions/{self.event_id}/odds/{provider_id}?limit={limit}"
        return self.api_request(url)


    def get_play_probabilities(self, limit:int=1000, return_values=True):
        res = BaseType(**self.api_request(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/events/{self.event_id}/competitions/{self.event_id}/probabilities?limit={limit}"))
        if not return_values:
            return res
        return [int(i) for i in self._get_values(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/events/{self.event_id}/competitions/{self.event_id}/probabilities", res.items)]

    def get_play_probability(self, play_id) :
        """
        Retrieve odds data for a specific provider.

        Args:


        Returns:

        """
        url = f"{self._core_url}/{self.sport.value}/leagues/{self.league}/events/{self.event_id}/competitions/{self.event_id}/probabilities/{play_id}"
        return self.api_request(url)

    def get_prediction(self, limit:int=1000) :
        """
        Retrieve odds data for a specific provider.

        Args:


        Returns:

        """
        url = f"{self._core_url}/{self.sport.value}/leagues/{self.league}/events/{self.event_id}/competitions/{self.event_id}/predictor?limit={limit}"
        return self.api_request(url)


