import requests

IAM_TOKEN = 'y0_AgAAAAAcBqTjAATuwQAAAAD4i1cepiea5uXiQvudXbWzfhf_J0lhzgw'
# folder_id = '<идентификатор_каталога>'
target_language = 'ru'
texts = ["Hello", "World"]

body = {
    "targetLanguageCode": target_language,
    "texts": texts,
    # "folderId": folder_id,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(IAM_TOKEN)
}

response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
    json = body,
    headers = headers
)

print(response.text)