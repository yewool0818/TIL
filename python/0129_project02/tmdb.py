import requests

# maker = URLMaker('add3128f3ad4b9bb3071c8179a916499')

class URLMaker:    
    url = 'https://api.themoviedb.org/3'
    api_key = 'add3128f3ad4b9bb3071c8179a916499'

    def get_url(self, category='movie', feature='popular', **kwargs):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={URLMaker.api_key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url
        

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()

        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None
    