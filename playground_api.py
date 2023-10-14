#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 heyhx, Inc. All Rights Reserved
#
# @Version : 1.0
# @Author  : mariswang
# @Time    : 2021-10-23 15:32
# @FileName: playground_api.py
# @Desc    :
import json
import sys
import requests

HOST = "localhost:8080" #api的地址
json_data_template = {
    'operationName': 'CreateProject',
    'variables': {
        'title': 'hello_world',
        'description': 'Showcase Cadence interactions',
        'readme': '',
        'seed': 2055,
        'numberOfAccounts': 5,
        'transactionTemplates': [
            {
                'script': 'transaction {\n  prepare(acct: AuthAccount) {\n    log("hello flow")\n  }\n}\n',
                'title': 'ChangeGreeting',
            },
        ],
        'scriptTemplates': [
            {
                'script': 'pub fun main() {\n log("hello flow")\n}',
                'title': 'ChangeGreeting',
            },
        ],
        'contractTemplates': [
            {
                'script': '// HelloFlow.cdc\n//\n// Welcome to flow study! This is one of the simplest programs you can deploy on Flow.\n//\n// The HelloWorld contract contains a single string field and a public getter function.\n//\n// Follow the "Hello, World!" tutorial to learn more: https://docs.onflow.org/cadence/tutorial/02-hello-world/\npub contract HelloFlow {\n  // Declare a public field of type String.\n  //\n  // All fields must be initialized in the init() function.\n  pub var greeting: String\n\n  // Public function that returns our friendly greeting!\n  access(all) fun changeGreeting(newGreeting: String) {\n    self.greeting = newGreeting\n  }\n\n  // Public function that returns our friendly greeting!\n  access(all) fun hello(): String {\n      return self.greeting\n  }\n\n  // The init() function is required if the contract contains any fields.\n  init() {\n    self.greeting = "Hello, Flow!"\n  }\n}\n',
                'title': 'HelloFlow',
            },
        ],
    },
    'query': 'mutation CreateProject($parentId: UUID, $title: String!, $description: String!, $readme: String!, $seed: Int!, $numberOfAccounts: Int!, $transactionTemplates: [NewProjectTransactionTemplate!]!, $scriptTemplates: [NewProjectScriptTemplate!]!, $contractTemplates: [NewProjectContractTemplate!]!) {\n  project: createProject(\n    input: {parentId: $parentId, numberOfAccounts: $numberOfAccounts, seed: $seed, title: $title, description: $description, readme: $readme, transactionTemplates: $transactionTemplates, scriptTemplates: $scriptTemplates, contractTemplates: $contractTemplates}\n  ) {\n    id\n    persist\n    mutable\n    parentId\n    seed\n    title\n    description\n    readme\n    accounts {\n      address\n      deployedContracts\n      state\n      __typename\n    }\n    transactionTemplates {\n      id\n      script\n      title\n      __typename\n    }\n    scriptTemplates {\n      id\n      script\n      title\n      __typename\n    }\n    contractTemplates {\n      id\n      script\n      title\n      __typename\n    }\n    __typename\n  }\n}\n',
}

def build_project(json_data):
    response = requests.post(f'http://{HOST}/query', json=json_data)
    data = response.json()
    #print(data)
    project_id = data["data"]["project"]["id"]
    return project_id

if __name__=="__main__":
    json_data = json_data_template.copy() #深拷贝
    project_id = build_project(json_data)
    print(project_id)


