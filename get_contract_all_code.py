#!/usr/bin/env python3
#coding=utf-8
#########################################################################
# Author: @appbk.com
# Created Time: Sun 01 Mar 2020 09:08:42 PM CST
# File Name: get_contract_all_code.py
# Description: 获取合约所有代码
######################################################################
import time
import sql_appbk
import re

result_list = [] #import链表

"""
功能：获得代码相关合约，就是代码import的合约即可，不需要获得别的代码import本合约的，否则基础合约会被很多import
输入：contract_address,合约地址
输入：contract_name,合约名称
返回: related_contract_name，相关合约的名称
返回: related_contract_address，相关合约的地址    
"""
def get_import_contracts(contract_address,contract_name):
    print("contract_address",contract_address, contract_name)
    sql = """
    SELECT * FROM flow_contract_relation WHERE contract_address = '{}' AND contract_name ='{}'
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)
    for item in result:
        contract_address = item["related_contract_address"]
        contract_name = item["related_contract_name"]

        data = {}
        data["related_contract_address"] = contract_address
        data["related_contract_name"] = contract_name
        result_list.append(data)

        # 递归调用
        get_import_contracts(contract_address, contract_name)

if __name__=="__main__":
    contract_name = "NWayUtilityCoin"
    contract_address = "0x011b6f1425389550"
    get_import_contracts(contract_address,contract_name)
    print(result_list)

