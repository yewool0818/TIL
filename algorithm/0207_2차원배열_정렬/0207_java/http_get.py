import requests

class URLMaker():
    base_url = "https://jsonmock.hackerrank.com/api/"

    def get_url(self, category, feature, **kwargs):
        url = f'{URLMaker.base_url}/{category}/{feature}'

        for key, value in kwargs.items():
            url += f'&{key}={value}'


        return url


urlMaker = URLMaker();

response = requests.get(urlMaker.get_url('countries', 'search', page=1))
data_dick = response.json()
