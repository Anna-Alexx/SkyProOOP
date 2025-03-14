#poetry add requests

# Пример запроса:
#
# import requests
#
# response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.content)


# url = 'https://api.github.com/search/repositories'
# params = {'q': 'python', 'sort': 'stars'}
# response = requests.get(url, params=params)
#
# response.content
# # b'{"total_count":3204986,"incomplete_results":false,"items":[{"id":83222441, ...
#
# response.text
# # {"total_count":3204990,"incomplete_results":false,"items":[{"id":83222441 ...
#
# response.json()
# # {'total_count': 3204992, 'incomplete_results': False, 'items': [{'id': 83222441, ...
#
# response.ok
# # True