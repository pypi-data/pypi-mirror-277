from espn_api_orm.calendar.api import ESPNCalendarAPI
from espn_api_orm.consts import ESPNSportTypes, ESPNSportSeasonTypes
from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.sport.api import ESPNSportAPI
from espn_api_orm.league.api import ESPNLeagueAPI
from espn_api_orm.season.api import ESPNSeasonAPI
from espn_api_orm.team.api import ESPNTeamAPI

base_api = ESPNBaseAPI()
single_test = True

sport_string ='basketball'#'soccer'
sport = ESPNSportTypes(sport_string)
league_string = 'mens-college-basketball'#'eng.1'
season = 2024

sport_api = ESPNSportAPI(sport)
sport_obj = sport_api.get_sport()

league_api = ESPNLeagueAPI(sport, league_string)
league_obj = league_api.get_league()

season_api = ESPNSeasonAPI(sport, league_string, season)
season_obj = season_api.get_season()

teams_list = [1] if single_test else season_api.get_team_ids(return_values=True)
teams = []
for team_id in teams_list:
    team_api = ESPNTeamAPI(sport, league_string, season, team_id)
    team_obj = team_api.get_team()
    teams.append(team_obj)
print(teams)

