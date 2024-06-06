from espn_api_orm.calendar.api import ESPNCalendarAPI
from espn_api_orm.consts import ESPNSportTypes, ESPNSportSeasonTypes
from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.odds.api import ESPNOddsAPI
from espn_api_orm.scoreboard.api import ESPNScoreboardAPI
from espn_api_orm.season.api import ESPNSeasonAPI

base_api = ESPNBaseAPI()
single_test = True
sport_string = 'basketball'
sport = ESPNSportTypes(sport_string)

league_string = 'mens-college-basketball'
season = 2024
event_id =401575451
provider_id = 58
play_id = 401575451101805401

odds_api = ESPNOddsAPI(sport, league_string, event_id)
#print(odds_api.get_odds(provider_id, limit=100))
#print(len(odds_api.get_play_probabilities(limit=1000)))
print(odds_api.get_prediction(limit=1000))
#print(odds_api.get_play_probability(play_id))



