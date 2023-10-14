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
import copy


import playground_api
import contract_all_code

def build_flow_project(contract_address,contract_name):
    # 1. 获得合约的所有import合约,包括自己
    contract_build = contract_all_code.ContractCode()
    contract_list = contract_build.get_all(contract_address,contract_name)

    #构建flow playground的json数据
    json_data = copy.deepcopy(playground_api.json_data_template)#深拷贝，不能用copy或者=，否则会有引用问题
    json_data["variables"]["title"] = contract_name
    json_data["variables"]["description"] = contract_name
    json_data["variables"]["contractTemplates"].extend(contract_list)
    #print(json.dumps(json_data))

    #调用api，创建flow playground项目
    project_id = playground_api.build_project(json_data)
    return project_id

if __name__=="__main__":
    contract_name = "NWayUtilityCoin"
    contract_address = "0x011b6f1425389550"
    project_id = build_flow_project(contract_address,contract_name)
    print("project_id:", project_id)
