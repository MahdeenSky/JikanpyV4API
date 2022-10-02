import requests as r

class JikanAPI:
    """
    Wrapper class for the Jikan v4 API
    """
    def __init__(self):
        self.url = 'https://api.jikan.moe/v4'

    def searchAnimeTitles(self, anime_name):
        """
        Queries the Jikan API for a list of anime titles
        cuz MAL API sucks ass
        """
        search_result = r.get(f'{self.url}/anime?q={anime_name}').json()['data'][:5]
        return [anime['title'] for anime in search_result]

    def getAnimeIDByName(self, anime_name):
        """
        Queries the Jikan API for the anime id
        cuz MAL API sucks
        """
        search_result = r.get(f'{self.url}/anime?q={anime_name}').json()['data'][:10]
        for anime in search_result:
            if anime['title'].lower() == anime_name.lower():
                return anime['mal_id']
        return search_result[0]['mal_id']

    def getAnimeByID(self, anime_id):
        """
        Queries the Jikan API for the anime using the anime id
        cuz MAL API sucks
        """
        return r.get(f'{self.url}/anime/{anime_id}').json()

if __name__ == "__main__":
    jikan_api = JikanAPI()
    assert len(jikan_api.searchAnimeTitles('Spy x Family')) == 5
    assert jikan_api.getAnimeIDByName('Spy x Family') == 50265
    assert jikan_api.getAnimeByID(19815)['data']['mal_id'] == 19815

