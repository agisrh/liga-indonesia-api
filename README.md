# Unofficial REST API Liga Indonesia

This is unofficial API Liga 1 Indonesia with method scrapping data using python.

## Run the app

    uvicorn main:app --reload

## Run the tests

    pytest

# REST API

The REST API to the example app is described below.

## Get Standing

### Request

`GET /standings`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/standings

### Response

    {
      "success": true,
      "status_code": 200,
      "message": "Standings",
      "data": [
          {
              "position": "1",
              "logo": "https://drive.google.com/uc?export=view&id=1VcKpq_KNEefPtRs31GuXuS8zdU8DuZfa",
              "club": "Borneo FC Samarinda",
              "matches": "15",
              "win": "9",
              "draw": "4",
              "lose": "2",
              "goals": "22-13",
              "form": "L W W W W",
              "points": "31"
          }
      ]
    }

## Get Matchday

### Request

`GET /matchday`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/matchday

### Response

    {
      "success": true,
      "status_code": 200,
      "message": "Matchday",
      "data": [
          {
              "date": "6 Oktober 2023"
          },
          {
              "time": "FT",
              "home": "RANS Nusantara FC",
              "home_club_logo": "https://drive.google.com/uc?export=view&id=1vrIBnJfycF3QN9xh8rZY_DyvcBZvO580",
              "score": "2-1",
              "away_club_logo": "https://drive.google.com/uc?export=view&id=1JIOFvJCdswP0gQLz8_qMYQ95ej33N2M-",
              "away": "PSIS Semarang",
              "venue": "Stadion Maguwoharjo, Sleman"
          }
      ]
    }

## Get Team List

### Request

`GET /teams`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/teams

### Response

    {
      "success": true,
      "status_code": 200,
      "message": "List Data Team",
      "data": [
          {
              "team_id": "818",
              "team_name": "PSIS Semarang",
              "team_venue": "Stadion Jatidiri Semarang",
              "team_logo": "https://drive.google.com/uc?export=view&id=1JIOFvJCdswP0gQLz8_qMYQ95ej33N2M-"
          }
      ]
    }

## Get Team Profile

### Request

`GET /team/profile/:id`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/team/profile/818

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "Team Profile Data",
    "data": {
        "team_name": "PSIS Semarang",
        "team_founded": "18 Mei 1932.",
        "team_logo": "https://drive.google.com/uc?export=view&id=1JIOFvJCdswP0gQLz8_qMYQ95ej33N2M-",
        "team_venue": "Stadion Jatidiri Semarang",
        "game_play": "166",
        "game_win": "63",
        "game_draw": "38",
        "game_lose": "65",
        "description": "Persatuan Sepak Bola Indonesia Semarang (PSIS) adalah suatu klub profesional yang berasal dari ibukota provinsi Jawa Tengah, Semarang. PSIS berdiri pada 18 Mei 1932. Pada 1998, PSIS mendapatkan juara Liga Indonesia. Sempat mengalami neik turun prestasi dan kini sudah kembali lagi di kasta tertinggi kompetisi sepak bola Indonesia. Julukan PSIS yakni Mahesa Jenar."
      }
    }

## Get Team Match

### Request

`GET /team/match/:id`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/team/match/818

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "Team Match Data",
    "data": [
              {
                  "time": "28-04-2024 15:00",
                  "home": "PERSIJA Jakarta",
                  "club_logo_home": "https://drive.google.com/uc?export=view&id=1acrxY2ypAFQsmsHtF6b7P_3Qlek-eSyY",
                  "score": "vs",
                  "club_logo_away": "https://drive.google.com/uc?export=view&id=1JIOFvJCdswP0gQLz8_qMYQ95ej33N2M-",
                  "away": "PSIS Semarang",
                  "competitions": "Liga 1 Indonesia"
              }
          ]
    }

## Get Team Statistics

### Request

`GET /team/statistics/:id`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/team/statistics/818

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "Team Statistics Data",
    "data": [
              {
                  "player_photo": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/Jonathan_original_24621.webp?1670223027",
                  "player_number": "10",
                  "player_name": "Jonathan Eduardo Cantillana Zorilla",
                  "position": "Forward",
                  "description": "Top Scorer",
                  "total": "16"
              }
          ]
    }

## Get Team Players

### Request

`GET /team/players/:id`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/team/players/818

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "Team Players Data",
    "data": [
              {
                  "player_id": "24625",
                  "player_photo": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/Dewa_original_24625.webp?1670222949",
                  "player_number": "19",
                  "player_name": "Alfeandra Dewangga Santosa",
                  "position": "Defender"
              }
          ]
    }

## Get Player Profile

### Request

`GET /player/profile/:id`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/player/profile/22345

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "Player Profile Data",
    "data": {
        "player_name": "#19. David Aparecido Da Silva",
        "player_team": "PERSIB Bandung",
        "player_photo": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/PE1812811890_original_22345.png?1690858097",
        "player_position": "Forward",
        "player_nationality": "Brazil",
        "player_age": "33",
        "player_height": "185.0 cm",
        "player_weight": "70.0 kg",
        "play": "113 (11)",
        "goals": "49 (6)",
        "assists": "7",
        "red_card": "0",
        "yellow_card": "10"
    }
}

## Get Player History

### Request

`GET /player/history/:id`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/player/history/22345

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "Player History Data",
    "data": {
            "club_history": [
                {
                    "date": "29 Dec 2021 - sekarang",
                    "club": "PERSIB Bandung",
                    "play": "65",
                    "goal": "43",
                    "assist": "6",
                    "save": "0",
                    "avg_intercept": "0.54",
                    "avg_dribble": "0.91",
                    "avg_tackle": "0.91"
                }
            ],
            "tournament_history": [
                {
                    "tournament": "Liga 1 Indonesia",
                    "club": "PERSIB Bandung",
                    "play": "13",
                    "goal": "10",
                    "assist": "0",
                    "save": "0",
                    "avg_intercept": "0.54",
                    "avg_dribble": "0.46",
                    "avg_tackle": "0.46"
                }
            ]
        }
    }

## 5 Top Scorer

### Request

`GET /statistics/topscorer`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/statistics/topscorer

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "5 Top Scorer",
    "data": [
            {
                "position": "1",
                "avatar": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/70_Gustavo_original_27101.png?1690777871",
                "name": "Gustavo Almeida dos Santos",
                "club_logo": "https://drive.google.com/uc?export=view&id=1CfPlBagfTEW178VFPxHRt21pnHrU2mlu",
                "play": "12(1)",
                "goals": "11 (5)"
            }
        ]
    }

## Get 5 Top Goal Keeper Save

### Request

`GET /statistics/goalkeeper_save`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/statistics/goalkeeper_save

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "5 Top Goal Keeper Save",
    "data": [
            {
                "position": "1",
                "avatar": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/ilson_original_29373.png?1690778866",
                "name": "Adilson Aguero dos Santos",
                "club_logo": "https://drive.google.com/uc?export=view&id=1l24rmfJA0qGsKVCB99b3vyRKxJ3IW_gW",
                "play": "15(0)",
                "total": "60"
            }
        ]
    }

## Get 5 Top Successful Passes

### Request

`GET /statistics/successful_passes`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/statistics/successful_passes

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "5 Top Successful Passes",
    "data": [
            {
                "position": "1",
                "avatar": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/PE22223572_original_32703.png?1690863011",
                "name": "Adam Ahmad Najem",
                "club_logo": "https://drive.google.com/uc?export=view&id=16y2oKDOd7T36UpcxYL90l2tpWDli0vov",
                "play": "15(0)",
                "total": "653"
            }
        ]
    }

## Get 5 Top Red Card

### Request

`GET /statistics/red_card`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/statistics/red_card

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "5 Top Red Card",
    "data": [
            {
                "position": "1",
                "avatar": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/Arif_Catur_original_33531.webp?1670220410",
                "name": "Arief Catur",
                "club_logo": "https://drive.google.com/uc?export=view&id=1T29mKuWDsUX7e4pxGwUPnbgkRMWI0K7M",
                "play": "12(0)",
                "total": "2"
            }
        ]
    }

## Get 5 Top Yellow Card

### Request

`GET /statistics/yellow_card`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/statistics/yellow_card

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "5 Yellow Red Card",
    "data": [
            {
                "position": "1",
                "avatar": "https://lapangbola-rails-files.s3.ap-southeast-1.amazonaws.com/documents/players/Arif_Catur_original_33531.webp?1670220410",
                "name": "Arief Catur",
                "club_logo": "https://drive.google.com/uc?export=view&id=1T29mKuWDsUX7e4pxGwUPnbgkRMWI0K7M",
                "play": "12(0)",
                "total": "2"
            }
        ]
    }


## Get Team Top Goal

### Request

`GET /statistics/team_top_goal`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/statistics/team_top_goal

### Response

    {
    "success": true,
    "status_code": 200,
    "message": "Team Top Goal",
    "data": [
            {
                "position": "1",
                "club_logo": "https:https://drive.google.com/uc?export=view&id=1n_7zH8RakesperGrmrG7WL-odzUrOSM0",
                "club": "PERSIB Bandung",
                "play": "15",
                "goal": "29",
                "average": "1.93"
            }
        ]
    }
