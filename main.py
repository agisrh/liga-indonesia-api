from fastapi import FastAPI, Request
from scraper import Scraper
from core.schemas import BaseResponse, BaseResponseList
from core import config

app = FastAPI(
    title='Unofficial API Liga Indonesia',
    description='This is unofficial API Liga 1 Indonesia with method scrapping data',
    version='1.0.0'
    )
scrap = Scraper()

@app.get("/", status_code=200, response_model=BaseResponse)
async def health_check(request: Request):
    data = {
            "project": config.PROJECT_NAME,
            "author": config.PROJECT_AUTHOR,
            "version": config.VERSION,
            "source": str(request.url),
            "documentation": str(request.url)+'docs'
    }

    return BaseResponse(data=data)

# @app.get(config.API_VERSION+"/tournaments")
# async def read_item():
#     data = scrap.tournaments(config.SITE_ENTRYPOINT+'/list-of-tournaments')
#     return BaseResponseList(message="List of Tournaments", data=data)

@app.get(config.API_VERSION+"/teams")
async def read_item():
    data = scrap.teams(config.SITE_ENTRYPOINT+'/tournaments/teams/'+config.SITE_INDEX)
    return BaseResponseList(message="List Data Team", data=data)

@app.get(config.API_VERSION+"/team/profile/{team_id}")
async def read_item(team_id: str):
    data = scrap.team_profile(config.SITE_ENTRYPOINT+'/teams/'+team_id)
    return BaseResponse(message="Team Profile Data", data=data)

@app.get(config.API_VERSION+"/team/match/{team_id}")
async def read_item(team_id: str):
    data = scrap.team_match(config.SITE_ENTRYPOINT+'/teams/'+team_id)
    return BaseResponseList(message="Team Match Data", data=data)

@app.get(config.API_VERSION+"/team/statistics/{team_id}")
async def read_item(team_id: str):
    data = scrap.team_statistics(config.SITE_ENTRYPOINT+'/teams/'+team_id)
    return BaseResponseList(message="Team Statistics Data", data=data)

@app.get(config.API_VERSION+"/team/players/{team_id}")
async def read_item(team_id: str):
    data = scrap.team_players(config.SITE_ENTRYPOINT+'/teams/'+team_id)
    return BaseResponseList(message="Team Players Data", data=data)

@app.get(config.API_VERSION+"/player/profile/{player_id}")
async def read_item(player_id: str):
    data = scrap.player_profile(config.SITE_ENTRYPOINT+'/players/'+player_id)
    return BaseResponse(message="Player Profile Data", data=data)

@app.get(config.API_VERSION+"/player/history/{player_id}")
async def read_item(player_id: str):
    data = scrap.player_history(config.SITE_ENTRYPOINT+'/players/'+player_id)
    return BaseResponse(message="Player History Data", data=data)

@app.get(config.API_VERSION+"/standings")
async def read_item():
    data = scrap.standings(config.SITE_ENTRYPOINT+'/tournaments/'+config.SITE_INDEX)
    return BaseResponseList(message="Standings", data=data)

@app.get(config.API_VERSION+"/matchday")
async def read_item(gameweek: str = ''):
    data = scrap.matchday(config.SITE_ENTRYPOINT+'/tournaments/fixtures/'+config.SITE_INDEX+'?gameweek='+gameweek)
    return BaseResponseList(message="Matchday", data=data)

@app.get(config.API_VERSION+"/statistics/topscorer")
async def read_item():
    data = scrap.topscorer(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Scorer", data=data)

@app.get(config.API_VERSION+"/statistics/goalkeeper_save")
async def read_item():
    data = scrap.goalkeeper_save(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Goal Keeper Save", data=data)

@app.get(config.API_VERSION+"/statistics/successful_passes")
async def read_item():
    data = scrap.successful_passes(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Successful Passes", data=data)

@app.get(config.API_VERSION+"/statistics/red_card")
async def read_item():
    data = scrap.red_card(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Red Card", data=data)

@app.get(config.API_VERSION+"/statistics/yellow_card")
async def read_item():
    data = scrap.yellow_card(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Yellow Card", data=data)

@app.get(config.API_VERSION+"/statistics/team_top_goal")
async def read_item():
    data = scrap.team_top_goal(config.SITE_ENTRYPOINT+'/tournaments/team_stats/'+config.SITE_INDEX)
    return BaseResponseList(message="Team Top Goal", data=data)
    