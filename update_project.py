import requests

cookies = {
    'flow-playground': 'MTY5NjI1NDczMXxEdi1CQkFFQ180SUFBUkFCRUFBQVJQLUNBQUVHYzNSeWFXNW5EQWdBQm5WelpYSkpSQVp6ZEhKcGJtY01KZ0FrTlROak5tWXhNMlF0TkRaaE9DMDBZalZoTFdGbU5HWXRZV1ZpTVdaa05qUmhNbU0zfME4c8ocFHAkWZGmsHSswERRWDp3fOfIqhrmenspYyny',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'flow-playground=MTY5NjI1NDczMXxEdi1CQkFFQ180SUFBUkFCRUFBQVJQLUNBQUVHYzNSeWFXNW5EQWdBQm5WelpYSkpSQVp6ZEhKcGJtY01KZ0FrTlROak5tWXhNMlF0TkRaaE9DMDBZalZoTFdGbU5HWXRZV1ZpTVdaa05qUmhNbU0zfME4c8ocFHAkWZGmsHSswERRWDp3fOfIqhrmenspYyny',
    'Origin': 'http://localhost:3000',
    'Referer': 'http://localhost:3000/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'operationName': 'UpdateProject',
    'variables': {
        'projectId': 'fb1cd2e7-6187-4a13-b915-a4dedc162092',
        'title': 'hello',
        'description': 'Showcase Cadence interactions',
        'readme': '',
    },
    'query': 'mutation UpdateProject($projectId: UUID!, $title: String!, $description: String!, $readme: String!) {\n  updateProject(\n    input: {id: $projectId, persist: true, title: $title, description: $description, readme: $readme}\n  ) {\n    id\n    persist\n    title\n    description\n    readme\n    __typename\n  }\n}\n',
}

# response = requests.post('http://localhost:8080/query', cookies=cookies, headers=headers, json=json_data)

response = requests.post('http://localhost:8080/query', json=json_data)

