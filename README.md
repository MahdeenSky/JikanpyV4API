# JikanpyV4API
As Jikan API V3 has been officially discontinued, I decided to make a temporary python wrapper for the Jikan V4 Api, in the form of a python script. If there are some functions that you need or improve, do open an issue or submit your own edits!


## Usage

```py
from jikan4pyAPI import JikanAPI
jikan = JikanAPI()

# Searching for anime titles (default limit = 5)
jikan.searchAnimeTitles("Spy x Family", limit=5) # returns ['Spy x Family', 'Spy x Family Part 2', 'Spy X Family 2 Promo', 'X', 'Family']

# Getting Anime ID by Name
jikan.getAnimeIDByName("Spy x Family") # returns 50265

# Getting Anime Information By ID
jikan.getAnimeByID(50265) # returns a huge dictionary with these information about the anime in the node "data": ['mal_id', 'url', 'images', 'trailer', 'approved', 'titles', 'title', 'title_english', 'title_japanese', 'title_synonyms', 'type', 'source', 'episodes', 'status', 'airing', 'aired', 'duration', 'rating', 'score', 'scored_by', 'rank', 'popularity', 'members', 'favorites', 'synopsis', 'background', 'season', 'year', 'broadcast', 'producers', 'licensors', 'studios', 'genres', 'explicit_genres', 'themes', 'demographics']
```
