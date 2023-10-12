from requests_html import HTMLSession
from core import config

class Scraper():

    # CLUB Scrap
    def clubs(self, url):
        session = HTMLSession()
        response = session.get(config.SITE_ENTRYPOINT+url)
        print(response.status_code)

        clubList = []
        clubs = response.html.find('div.item-team')

        for row in clubs:
            item = {
                'club_name': row.find('h5', first=True).text.strip(),
                'club_venue': row.find('span.group-team', first=True).text.strip(),
                'club_logo': row.find('img')[1].attrs["src"],
            }
            clubList.append(item)

        return clubList
    
    # STANDINGS Scrap
    def standings(self, url):
        session = HTMLSession()
        response = session.get(config.SITE_ENTRYPOINT+url)
        print(response.status_code)

        table = response.html.find('table')[0]
        table_data = [[c.text for c in row.find('td')[:-1]] for row in table.find('tr')][1:]
        table_header = [[c.text for c in row.find('td')[:-1]] for row in table.find('tr')][0]
        res = [dict(zip(table_header, t)) for t in table_data]

        return res
    
    # FIXTURES Scrap
    def fixtures(self, url):
        session = HTMLSession()
        response = session.get(config.SITE_ENTRYPOINT+url)
        print(response.status_code)

        fixture = response.html.find('div.table')[0]
        print(fixture)
        tables = response.html.find('table')
        for table in tables:
             table_data = [[c.text for c in row.find('td')] for row in table.find('tr')]
             print(table_data)
        
        #table_data = [[c.text for c in row.find('td')] for row in table.find('tr')]
        #table_header = [[c.text for c in row.find('td')[:-1]] for row in table.find('tr')][0]
      
        #print(table_data)
        # return clubList
        # table_header = [[c.text for c in row.find('td')[:-1]] for row in table.find('tr')][0]
        # res = [dict(zip(table_header, t)) for t in table_data]

        return []