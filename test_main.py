import pytest
from fastapi.testclient import TestClient
from core import config
from typing import Generator
from main import app

@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as client:
        yield client

def test_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_teams(client: TestClient):
    url = f"{config.API_VERSION}/teams"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_team_profile(client: TestClient):
    url = f"{config.API_VERSION}/team/profile/471"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_team_match(client: TestClient):
    url = f"{config.API_VERSION}/team/match/471"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_team_statistics(client: TestClient):
    url = f"{config.API_VERSION}/team/statistics/471"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_team_players(client: TestClient):
    url = f"{config.API_VERSION}/team/players/471"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_player(client: TestClient):
    url = f"{config.API_VERSION}/player/profile/24690"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_player_history(client: TestClient):
    url = f"{config.API_VERSION}/player/history/24690"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_standings(client: TestClient):
    url = f"{config.API_VERSION}/standings"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_matchday(client: TestClient):
    url = f"{config.API_VERSION}/matchday"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_topscorer(client: TestClient):
    url = f"{config.API_VERSION}/statistics/topscorer"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_goalkeeper_save(client: TestClient):
    url = f"{config.API_VERSION}/statistics/goalkeeper_save"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_successful_passes(client: TestClient):
    url = f"{config.API_VERSION}/statistics/successful_passes"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_red_card(client: TestClient):
    url = f"{config.API_VERSION}/statistics/red_card"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_yellow_card(client: TestClient):
    url = f"{config.API_VERSION}/statistics/yellow_card"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def test_team_top_goal(client: TestClient):
    url = f"{config.API_VERSION}/statistics/team_top_goal"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def netxmatch(client: TestClient):
    url = f"{config.API_VERSION}/nextmatch"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def netxmatch(client: TestClient):
    url = f"{config.API_VERSION}/news"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data

def netxmatch(client: TestClient):
    url = f"{config.API_VERSION}/highlights"
    response = client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response.json() == response_data