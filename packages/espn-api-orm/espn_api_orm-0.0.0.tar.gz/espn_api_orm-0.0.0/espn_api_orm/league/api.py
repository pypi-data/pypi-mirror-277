from espn_api_orm.consts import ESPNSportTypes, FIRST_SEASON
from espn_api_orm.generic.schema import BaseType
from espn_api_orm.league.schema import League
from espn_api_orm.sport.api import ESPNSportAPI


class ESPNLeagueAPI(ESPNSportAPI):
    """
    ESPN League API for retrieving sport information about a specific league.

    Attributes:

    Methods:
    """

    def __init__(self, sport: ESPNSportTypes, league: str):
        """
        Initialize ESPNSportAPI.
        """
        super().__init__(sport)
        self.league = league

    def get_league(self):
        return League(**self.api_request(f"{self._core_url}/{self.sport.value}/leagues/{self.league}"))

    def get_seasons(self, return_values=True):
        res = BaseType(**self.api_request(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/seasons?limit=200"))
        if not return_values:
            return res
        return [int(i) for i in self._get_values(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/seasons", res.items) if int(i) > FIRST_SEASON]

    def get_franchises(self, return_values=True):
        res = BaseType(**self.api_request(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/franchises?limit=1000"))
        if not return_values:
            return res
        return [int(i) for i in self._get_values(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/franchises", res.items)]

    def get_odds_providers(self, return_values=True):
        res = BaseType(**self.api_request(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/providers?limit=1000"))
        if not return_values:
            return res
        return [int(i) for i in self._get_values(f"{self._core_url}/{self.sport.value}/leagues/{self.league}/providers", res.items)]


