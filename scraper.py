from requests_html import HTMLSession
from core import config
from pytube import Playlist
from helper import Helper


helper = Helper()
class Scraper():
    
    # TOURNAMENTS Scrap
    def tournaments(self, url):
        session = HTMLSession()
        response = session.get(url)

        tournaments = []
        tournament_table = response.html.find('section.profile-team')

        for row in tournament_table:
            row_id = row.find('a')[1].attrs["href"].split('/')
            photo = row.find('img')[0].attrs["src"]
            if "/assets/" in photo:
                photo = config.SITE_ENTRYPOINT+photo
            elif "amazonaws.com" in photo:
                photo = 'https:'+photo
            else:
                photo = photo
            item = {
                'tournaments_index': row_id[2],
                'tournaments_name': row.find('h5', first=True).text.strip(),
                'tournaments_logo': photo,
            }
            tournaments.append(item)

        return tournaments
    
    # TEAMS Scrap
    def teams(self, url):
        session = HTMLSession()
        response = session.get(url)

        teamList = []
        teams = response.html.find('section.profile-team')

        for row in teams:
            row_id = row.find('a')[1].attrs["href"].split('/')
            teamName = row.find('h5', first=True).text.strip();
            item = {
                'team_id': row_id[2],
                'team_name': teamName,
                'team_venue': row.find('span', first=True).text.strip(),
                'team_logo': helper.getLogo(row.find('h5', first=True).text.strip()),
            }
            teamList.append(item)

        return teamList
    
    # TEAM PROFILE Scrap
    def team_profile(self, url):
        session = HTMLSession()
        response = session.get(url)

        # TEAM PROFILE
        team = response.html.find('dl.user-profile-dl', first=True)
        team_asset = response.html.find('section.profile-user', first=True)
        team_stats = response.html.find('div.widget-four', first=True)

        team_name = team.find('dd')[0].text.strip()
        team_desc = team.find('dd')[1].text.strip()
        team_founded = team.find('dd')[2].text.strip()
        team_venue = team.find('dd')[3].text.strip()
        team_logo = helper.getLogo(team_name)
        game_play = team_stats.find('p')[0].text.strip()
        game_win = team_stats.find('p')[1].text.strip()
        game_draw = team_stats.find('p')[2].text.strip()
        game_lose = team_stats.find('p')[3].text.strip()
    
        data = {
            "team_name": team_name,
            "team_founded": team_founded,
            "team_logo": team_logo,
            "team_venue": team_venue,
            "game_play": game_play,
            "game_win": game_win,
            "game_draw": game_draw,
            "game_lose": game_lose,
            "description": team_desc,
        }

        return data
    
    # TEAM MATCH Scrap
    def team_match(self, url):
        session = HTMLSession()
        response = session.get(url)

        # TEAM MATCH
        table_match = response.html.find('table')[0]
        data_match = []
        for row in table_match.find('tr'):
           item = {
                'time': row.find('td')[0].text.strip(),
                'home_club': row.find('td')[1].text.strip(),
                'club_logo_home': helper.getLogo(row.find('td')[1].text.strip()),
                'score': row.find('td')[3].text.strip(),
                'club_logo_away': helper.getLogo(row.find('td')[5].text.strip()),
                'away_club': row.find('td')[5].text.strip(),
                'competitions': row.find('td')[6].text.strip(),
            }
           data_match.append(item)

        return data_match
    
    # TEAM STATISTICS Scrap
    def team_statistics(self, url):
        session = HTMLSession()
        response = session.get(url)

        # STATISTICS
        table_stats = response.html.find('table')[2]
        data_stats = []
        for row in table_stats.find('tr'):
           photo = row.find('td')[0].find('img')[0].attrs['src']
           if "default.jpg" not in photo:
               photo = 'https:'+photo
           else:
               photo = config.SITE_ENTRYPOINT+photo
               
           item = {
                'player_photo': photo,
                'player_number': row.find('td')[1].text.strip(),
                'player_name': row.find('td')[2].text.strip(),
                'position': row.find('td')[3].text.strip(),
                'description': row.find('td')[4].text.strip(),
                'total': row.find('td')[5].text.strip(),
            }
           data_stats.append(item)

        return data_stats
    
    # TEAM PLAYERS Scrap
    def team_players(self, url):
        session = HTMLSession()
        response = session.get(url)
    
        # PLAYER LIST
        table_player = response.html.find('table')[1]
        data_player = []
        for row in table_player.find('tr'):
           player_id = row.find('td')[0].find('a')[0].attrs['href'].split('/')
           photo = row.find('td')[0].find('img')[0].attrs['src']
           if "default.jpg" not in photo:
               photo = 'https:'+photo
           else:
               photo = config.SITE_ENTRYPOINT+photo
               
           item = {
                'player_id':player_id[2],
                'player_photo': photo,
                'player_number': row.find('td')[1].text.strip(),
                'player_name': row.find('td')[2].text.strip(),
                'position': row.find('td')[3].text.strip(),
            }
           data_player.append(item)

        return data_player
    
    # PLAYER PROFILE Scrap
    def player_profile(self, url):
        session = HTMLSession()
        response = session.get(url)

        # PLAYER PROFILE
        player = response.html.find('dl.user-profile-dl', first=True)
        widget_name = response.html.find('div.profile-header-title', first=True)
        player_asset = response.html.find('section.profile-user', first=True)
        player_stats = response.html.find('div.widget-four', first=True)
        photo = player_asset.find('img')[0].attrs['src']
        if "default.jpg" not in photo:
            photo = 'https:'+photo
        else:
            photo = config.SITE_ENTRYPOINT+photo

        team_name = player.find('dd')[0].text.strip()
        player_name = widget_name.find('h2')[0].text.strip()
        player_photo = photo
        player_position = player.find('dd')[1].text.strip()
        player_nat = player.find('dd')[2].text.strip()
        player_age = player.find('dd')[3].text.strip()
        player_height = player.find('dd')[4].text.strip()
        player_weight = player.find('dd')[5].text.strip()
        play = player_stats.find('p')[0].text.strip()
        goals = player_stats.find('p')[1].text.strip()
        assists = player_stats.find('p')[2].text.strip()
        red_card = player_stats.find('p')[3].text.strip()
        yellow_card = player_stats.find('p')[4].text.strip()


        data = {
            "player_name": player_name,
            "player_team": team_name,
            "player_photo": player_photo,
            "player_position": player_position,
            "player_nationality": player_nat,
            "player_age": player_age,
            "player_height": player_height,
            "player_weight": player_weight,
            "play": play,
            "goals": goals,
            "assists":assists,
            "red_card": red_card,
            "yellow_card": yellow_card,
        }

        return data
    
     # PLAYER HISTORY Scrap
    def player_history(self, url):
        session = HTMLSession()
        response = session.get(url)

        # PLAYER PROFILE
        widget_name = response.html.find('div.profile-header-title', first=True)
        player_asset = response.html.find('section.profile-user', first=True)
        photo = player_asset.find('img')[0].attrs['src']
        if "default.jpg" not in photo:
            photo = 'https:'+photo
        else:
            photo = config.SITE_ENTRYPOINT+photo

        player_name = widget_name.find('h2')[0].text.strip()
        player_photo = photo
       
        # CLUB HISTORY
        table_club = response.html.find('table')[1]
        data_club = []
        for row in table_club.find('tr'):
           item = {
                'date': row.find('td')[0].text.strip(),
                'club': row.find('td')[1].text.strip(),
                'play': row.find('td')[2].text.strip(),
                'goal': row.find('td')[3].text.strip(),
                'assist': row.find('td')[4].text.strip(),
                'save': row.find('td')[5].text.strip(),
                'avg_intercept': row.find('td')[6].text.strip(),
                'avg_dribble': row.find('td')[7].text.strip(),
                'avg_tackle': row.find('td')[7].text.strip(),
            }
           data_club.append(item)
    
        # TOURNAMENT HISTORY
        table_tournament = response.html.find('table')[2]
        data_tournament = []
        for row in table_tournament.find('tr'):
           item = {
                'tournament': row.find('td')[0].text.strip(),
                'club': row.find('td')[1].text.strip(),
                'play': row.find('td')[2].text.strip(),
                'goal': row.find('td')[3].text.strip(),
                'assist': row.find('td')[4].text.strip(),
                'save': row.find('td')[5].text.strip(),
                'avg_intercept': row.find('td')[6].text.strip(),
                'avg_dribble': row.find('td')[7].text.strip(),
                'avg_tackle': row.find('td')[7].text.strip(),
            }
           data_tournament.append(item)

        # STATISTICS
        # table_stats = response.html.find('table')[2]
        # data_stats = []
        # for row in table_stats.find('tr'):
        #    photo = row.find('td')[0].find('img')[0].attrs['src']
        #    if "default.jpg" not in photo:
        #        photo = 'https:'+photo
        #    else:
        #        photo = config.SITE_ENTRYPOINT+photo
               
        #    item = {
        #         'player_photo': photo,
        #         'player_number': row.find('td')[1].text.strip(),
        #         'player_name': row.find('td')[2].text.strip(),
        #         'position': row.find('td')[3].text.strip(),
        #         'description': row.find('td')[4].text.strip(),
        #         'total': row.find('td')[5].text.strip(),
        #     }
        #    data_stats.append(item)

        data = {
            "player_name": player_name,
            "player_photo": player_photo,
            "club_history": data_club,
            "tournament_history": data_tournament
        }

        return data

    # STANDINGS Scrap
    def standings(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('table')[0]

        table_data = []
        for row in table.find('tr')[2:]:
           item = {
                'position': row.find('td')[0].text.strip(),
                'logo': helper.getLogo(row.find('td')[2].text.strip()),
                'club': row.find('td')[2].text.strip(),
                'matches': row.find('td')[3].text.strip(),
                'win': row.find('td')[4].text.strip(),
                'draw': row.find('td')[5].text.strip(),
                'lose': row.find('td')[6].text.strip(),
                'goals': row.find('td')[7].text.strip(),
                'form': row.find('td')[8].text.strip(),
                'points': row.find('td')[9].text.strip(),
            }
           table_data.append(item)
        return table_data
    
    # MATCHDAY Scrap
    def matchday(self, url):
        session = HTMLSession()
        response = session.get(url)

        widget_gameweek = response.html.find('div#match-active', first=True)
        gameweek = widget_gameweek.find('h5')[0].text.strip().split(' ')
        week = int(gameweek[1])
        table = response.html.find('table')[0]

        array_data = []
        for row in table.find('tr'):
            row_length = len(row.find('td'))
            if(row_length > 1):
                item = {
                    "gameweek": week,
                    "time": row.find('td')[0].text.strip(),
                    "home_club": row.find('td')[1].text.strip(),
                    "home_club_logo": helper.getLogo(row.find('td')[1].text.strip()),
                    "score": row.find('td')[3].text.strip(),
                    "away_club_logo": helper.getLogo(row.find('td')[5].text.strip()),
                    "away_club": row.find('td')[5].text.strip(),
                    "venue": row.find('td')[6].text.strip(),
                }
            else:
                item = {
                    "gameweek": week,
                    "date": row.find('td')[0].text.strip(),
                }
            
            array_data.append(item)
        return array_data
    
    # NEXT MATCH Scrap
    def nextmatch(self, url):
        session = HTMLSession()
        res_current = session.get(url)

        widget_gameweek = res_current.html.find('div#match-active', first=True)
        gameweek = widget_gameweek.find('h5')[0].text.strip().split(' ')
        week = int(gameweek[1])+1

        res_next = session.get(url+'?gameweek='+str(week))
        table = res_next.html.find('table')[0]

        array_data = []
        for row in table.find('tr'):
            row_length = len(row.find('td'))
            if(row_length > 1):
                item = {
                    "gameweek": week,
                    "time": row.find('td')[0].text.strip(),
                    "home_club": row.find('td')[1].text.strip(),
                    "home_club_logo": helper.getLogo(row.find('td')[1].text.strip()),
                    "score": row.find('td')[3].text.strip(),
                    "away_club_logo": helper.getLogo(row.find('td')[5].text.strip()),
                    "away_club": row.find('td')[5].text.strip(),
                    "venue": row.find('td')[6].text.strip(),
                }
            else:
                item = {
                    "gameweek": week,
                    "date": row.find('td')[0].text.strip(),
                }
            
            array_data.append(item)
        return array_data
    
    # HIGHLIGHTS Scrap
    def highlights(self, url):
        playlist = Playlist(url)

        array_data = []
        for video in playlist.videos[:15]:
            item = {
                "title": video.title,
                "video": video.watch_url,
                "thumbnail": video.thumbnail_url,
            }
            array_data.append(item)

        return array_data
    
    # TOP SCORER Scrap
    def topscorer(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('table')[0]
        table_data = []
        for row in table.find('tr')[2:]:
           item = {
                'position': row.find('td')[0].text.strip(),
                'avatar': 'https:'+row.find('td')[1].find('img')[0].attrs['src'],
                'name': row.find('td')[2].text.strip(),
                'club_logo': row.find('td')[3].find('img')[0].attrs['src'],
                'play': row.find('td')[4].text.strip(),
                'goals': row.find('td')[5].text.strip(),
            }
           table_data.append(item)
        return table_data
    
    # GOAL KEEPER SAVES Scrap
    def goalkeeper_save(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('table')[1]
        table_data = []
        for row in table.find('tr')[2:]:
           item = {
                'position': row.find('td')[0].text.strip(),
                'avatar': 'https:'+row.find('td')[1].find('img')[0].attrs['src'],
                'name': row.find('td')[2].text.strip(),
                'club_logo': row.find('td')[3].find('img')[0].attrs['src'],
                'play': row.find('td')[4].text.strip(),
                'total': row.find('td')[5].text.strip(),
            }
           table_data.append(item)
        return table_data
    
    # SUCCESSFUL PASSES Scrap
    def successful_passes(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('table')[2]
        table_data = []
        for row in table.find('tr')[2:]:
           item = {
                'position': row.find('td')[0].text.strip(),
                'avatar': 'https:'+row.find('td')[1].find('img')[0].attrs['src'],
                'name': row.find('td')[2].text.strip(),
                'club_logo': row.find('td')[3].find('img')[0].attrs['src'],
                'play': row.find('td')[4].text.strip(),
                'total': row.find('td')[5].text.strip(),
            }
           table_data.append(item)
        return table_data
    
    # RED CARD Scrap
    def red_card(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('table')[3]
        table_data = []
        for row in table.find('tr')[2:]:
           item = {
                'position': row.find('td')[0].text.strip(),
                'avatar': 'https:'+row.find('td')[1].find('img')[0].attrs['src'],
                'name': row.find('td')[2].text.strip(),
                'club_logo': row.find('td')[3].find('img')[0].attrs['src'],
                'play': row.find('td')[4].text.strip(),
                'total': row.find('td')[5].text.strip(),
            }
           table_data.append(item)
        return table_data
    
    # YELLOW CARD Scrap
    def yellow_card(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('table')[4]
        table_data = []
        for row in table.find('tr')[2:]:
           item = {
                'position': row.find('td')[0].text.strip(),
                'avatar': 'https:'+row.find('td')[1].find('img')[0].attrs['src'],
                'name': row.find('td')[2].text.strip(),
                'club_logo': row.find('td')[3].find('img')[0].attrs['src'],
                'play': row.find('td')[4].text.strip(),
                'total': row.find('td')[5].text.strip(),
            }
           table_data.append(item)
        return table_data
    
    # TEAM TOP GOAL Scrap
    def team_top_goal(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('table')[0]
        table_data = []
        for row in table.find('tr')[2:]:
           item = {
                'position': row.find('td')[0].text.strip(),
                'club_logo': helper.getLogo(row.find('td')[2].text.strip()),
                'club': row.find('td')[2].text.strip(),
                'play':  row.find('td')[3].text.strip(),
                'goal': row.find('td')[4].text.strip(),
                'average': row.find('td')[5].text.strip(),
            }
           table_data.append(item)
        return table_data
    
    # NEWS Scrap
    def news(self, url):
        session = HTMLSession()
        response = session.get(url)
        table = response.html.find('ul.box-article-list')[0]
        data = []
        for row in table.find('li'):
            item = {
                    'title': row.find('p')[0].text.strip(),
                    'thumbnail': row.find('img.lazy_loaded')[0].attrs['data-src'],
                    'url': row.find('a')[0].attrs["href"],
                }
            data.append(item)
        return data