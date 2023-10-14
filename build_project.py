import requests

cookies = {
    'flow-playground': 'MTY5NjI1NDY0NHxEdi1CQkFFQ180SUFBUkFCRUFBQUJQLUNBQUE9fCRrjpIb-6YSvMoF7tplKRI6qR41nYr1vMbcrtvn3Co1',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'flow-playground=MTY5NjI1NDY0NHxEdi1CQkFFQ180SUFBUkFCRUFBQUJQLUNBQUE9fCRrjpIb-6YSvMoF7tplKRI6qR41nYr1vMbcrtvn3Co1',
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
    'operationName': 'CreateProject',
    'variables': {
        'title': 'hello_world',
        'description': 'Showcase Cadence interactions',
        'readme': '',
        'seed': 2055,
        'numberOfAccounts': 5,
        'transactionTemplates': [
            {
                'script': 'import HelloWorld from 0x05\n\ntransaction(greeting: String) {\n\n  prepare(acct: AuthAccount) {\n    log(acct.address)\n  }\n\n  execute {\n    HelloWorld.changeGreeting(newGreeting: greeting)\n  }\n}\n',
                'title': 'ChangeGreeting',
            },
        ],
        'scriptTemplates': [
            {
                'script': 'import HelloWorld from 0x05\n\npub fun main() {\n  log(HelloWorld.hello())\n}\n',
                'title': 'GetGreeting',
            },
        ],
        'contractTemplates': [
            {
                'script': '// HelloWorld.cdc\n//\n// Welcome to Cadence! This is one of the simplest programs you can deploy on Flow.\n//\n// The HelloWorld contract contains a single string field and a public getter function.\n//\n// Follow the "Hello, World!" tutorial to learn more: https://docs.onflow.org/cadence/tutorial/02-hello-world/\npub contract HelloWorld {\n  // Declare a public field of type String.\n  //\n  // All fields must be initialized in the init() function.\n  pub var greeting: String\n\n  // Public function that returns our friendly greeting!\n  access(all) fun changeGreeting(newGreeting: String) {\n    self.greeting = newGreeting\n  }\n\n  // Public function that returns our friendly greeting!\n  access(all) fun hello(): String {\n      return self.greeting\n  }\n\n  // The init() function is required if the contract contains any fields.\n  init() {\n    self.greeting = "Hello, World!"\n  }\n}\n',
                'title': 'HelloWorld',
            },
        ],
    },
    'query': 'mutation CreateProject($parentId: UUID, $title: String!, $description: String!, $readme: String!, $seed: Int!, $numberOfAccounts: Int!, $transactionTemplates: [NewProjectTransactionTemplate!]!, $scriptTemplates: [NewProjectScriptTemplate!]!, $contractTemplates: [NewProjectContractTemplate!]!) {\n  project: createProject(\n    input: {parentId: $parentId, numberOfAccounts: $numberOfAccounts, seed: $seed, title: $title, description: $description, readme: $readme, transactionTemplates: $transactionTemplates, scriptTemplates: $scriptTemplates, contractTemplates: $contractTemplates}\n  ) {\n    id\n    persist\n    mutable\n    parentId\n    seed\n    title\n    description\n    readme\n    accounts {\n      address\n      deployedContracts\n      state\n      __typename\n    }\n    transactionTemplates {\n      id\n      script\n      title\n      __typename\n    }\n    scriptTemplates {\n      id\n      script\n      title\n      __typename\n    }\n    contractTemplates {\n      id\n      script\n      title\n      __typename\n    }\n    __typename\n  }\n}\n',
}

#response = requests.post('http://localhost:8080/query', cookies=cookies, headers=headers, json=json_data)
response = requests.post('http://8.218.127.18:8080/query', json=json_data)
print(response.text)
