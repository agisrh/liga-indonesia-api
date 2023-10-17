from fastapi import FastAPI, Request
from scraper import Scraper
from core.schemas import BaseResponse, BaseResponseList
from core import config

app = FastAPI()
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


@app.get(config.API_VERSION+"/tournaments")
async def read_item():
    data = scrap.tournaments(config.SITE_ENTRYPOINT+'/list-of-tournaments')
    return BaseResponseList(message="List of Tournaments", data=data)

@app.get(config.API_VERSION+"/teams")
async def read_item():
    data = scrap.teams(config.SITE_ENTRYPOINT+'/tournaments/teams/'+config.SITE_INDEX)
    return BaseResponseList(message="Teams Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/team/profile/{id}")
async def read_item(id: str):
    data = scrap.team_profile(config.SITE_ENTRYPOINT+'/teams/'+id)
    return BaseResponse(message="Team Profile Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/player/{id}")
async def read_item(id: str):
    data = scrap.player(config.SITE_ENTRYPOINT+'/players/'+id)
    return BaseResponse(message="Player Profile Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/standings")
async def read_item():
    data = scrap.standings(config.SITE_ENTRYPOINT+'/tournaments/'+config.SITE_INDEX)
    return BaseResponseList(message="Standings Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/matchday")
async def read_item(gameweek: str = ''):
    data = scrap.matchday(config.SITE_ENTRYPOINT+'/tournaments/fixtures/'+config.SITE_INDEX+'?gameweek='+gameweek)
    return BaseResponseList(message="Matchday Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/statistics/topscorer")
async def read_item():
    data = scrap.topscorer(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Scorer Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/statistics/goalkeeper_save")
async def read_item():
    data = scrap.goalkeeper_save(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Goal Keeper Save Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/statistics/successful_passes")
async def read_item():
    data = scrap.successful_passes(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Successful Passes Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/statistics/red_card")
async def read_item():
    data = scrap.red_card(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Red Card Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/statistics/yellow_card")
async def read_item():
    data = scrap.yellow_card(config.SITE_ENTRYPOINT+'/tournaments/stats/'+config.SITE_INDEX)
    return BaseResponseList(message="5 Top Yellow Card Liga 1 Indonesia", data=data)

@app.get(config.API_VERSION+"/statistics/team_top_goal")
async def read_item():
    data = scrap.team_top_goal(config.SITE_ENTRYPOINT+'/tournaments/team_stats/'+config.SITE_INDEX)
    return BaseResponseList(message="Team Top Goal Liga 1 Indonesia", data=data)
    