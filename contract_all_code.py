#!/usr/bin/env python3
#coding=utf-8
#########################################################################
# Author: @appbk.com
# Created Time: Sun 01 Mar 2020 09:08:42 PM CST
# File Name: get_contract_all_code.py
# Description: 获取合约所有代码
######################################################################
import json
import re
import time
import sql_appbk

class ContractCode():
    def __init__(self):
        self.result_list = []
        self.contract_name_list = []

    def revise_code(self,code, address="0x05"):
        """
        功能：修正代码，将import的地址改成0x05
        输入：code，合约的代码
        输入：address，地址
        返回: code，合约的代码
        """
        #code = code.replace("import", "import {}".format(address))
        p = re.compile('from 0x\w{10,25}') #引用的正则
        code_new = p.sub("from 0x05", code)
        return code_new

    def get_code(self, contract_address, contract_name):
        """
        功能：获得合约的代码
        输入：contract_address,合约地址
        输入：contract_name,合约名称
        返回: code，合约的代码
        """
        sql = """
        SELECT * FROM flow_code WHERE contract_address = '{}' AND contract_name ='{}'
        """.format(contract_address, contract_name)
        result = sql_appbk.mysql_com(sql)
        code = result[0]["contract_code"]

        #import的地址都改成0x05,如 import HelloWorld from 0x05
        code_new = self.revise_code(code)
        return code_new


    """
    功能：获得代码相关合约，就是代码import的合约即可，不需要获得别的代码import本合约的，否则基础合约会被很多import
    输入：contract_address,合约地址
    输入：contract_name,合约名称
    返回: related_contract_name，相关合约的名称
    返回: related_contract_address，相关合约的地址    
    """
    def get_import_contracts(self, contract_address, contract_name):
        sql = """
        SELECT * FROM flow_contract_relation WHERE contract_address = '{}' AND contract_name ='{}'
        """.format(contract_address, contract_name)
        result = sql_appbk.mysql_com(sql)
        for item in result:
            contract_address = item["related_contract_address"]
            contract_name = item["related_contract_name"]

            data = {}
            data["related_contract_address"] = contract_address
            data["related_contract_name"] = contract_name
            if contract_name not in self.contract_name_list:
                self.contract_name_list.append(contract_name)
                self.result_list.append(data)

            # 递归调用
            self.get_import_contracts(contract_address, contract_name)

    def get_all(self, contract_address, contract_name):
        #构建代码数据结构  data = {"script":script, "title","title"} script是代码，title是代码名称
        data_list = []
        #先添加自己
        code = self.get_code(contract_address, contract_name)
        data = {}
        data["script"] = code
        data["title"] = contract_name
        data_list.append(data)

        #再添加相关代码
        self.result_list = [] #注意这里清空了
        self.get_import_contracts(contract_address, contract_name)
        for item in self.result_list:
            contract_address = item["related_contract_address"]
            contract_name = item["related_contract_name"]
            code = self.get_code(contract_address, contract_name)

            data = {}
            data["script"] = code
            data["title"] = contract_name
            data_list.append(data)

        return data_list

if __name__=="__main__":
    contract_importer = ContractCode()

    contract_name = "NWayUtilityCoin"
    contract_address = "0x011b6f1425389550"

    contract_name = "TheFabricantS1MintTransferClaim"
    contract_address = "0x09e03b1f871b3513"

    ret = contract_importer.get_all(contract_address, contract_name)
    #[{"script":"script","code":code}]
    print(json.dumps(ret))
