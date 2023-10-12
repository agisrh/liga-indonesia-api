from fastapi import FastAPI, APIRouter, Request
from scraper import Scraper
from core.schemas import BaseResponse, BaseResponseList
from core import config

app = FastAPI()
router = APIRouter(prefix=config.API_VERSION)
app.include_router(router)

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

@app.get("/clubs")
async def read_item():
    data = scrap.clubs('clubs/'+config.SITE_INDEX)
    return BaseResponseList(message="Clubs", data=data)

@app.get("/standings")
async def read_item():
    data = scrap.standings('table/'+config.SITE_INDEX)
    return BaseResponseList(message="Standings", data=data)

@app.get("/fixtures")
async def read_item():
    data = scrap.fixtures('fixtures/'+config.SITE_INDEX)
    return BaseResponseList(message="Fixtures", data=data)