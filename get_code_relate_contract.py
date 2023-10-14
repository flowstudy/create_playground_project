#!/usr/bin/env python3
#coding=utf-8
#########################################################################
# Author: @appbk.com
# Created Time: Sun 01 Mar 2020 09:08:42 PM CST
# File Name: index.py
# Description:根据import关系，获得相关代码
######################################################################
import time
import sql_appbk
import re


"""
功能；获取一段合约代码的相关代码,抽取import名称 并存入数据库。
输入：contract_code,合约代码。
输入：contract_address,合约地址。
返回：list 格式如下 [{"contract_name":"name1","contract_address":"address1"},
                    {"contract_name":"name2","contract_address":"address2"}]。
"""
def get_code_related(contract_code):
    relate_contract_list = []
    #step 1 ，获得所有的import行
    #step 1,获得所有引用
    p = re.compile('import.{3,30}from 0x\w{10,25}') #引用的正则
    import_list = p.findall(contract_code)
    # step 2 ,解析每一行，获得相关的合约地址和合约名称
    for item in import_list:
        item_list = item.split()
        contract_name = item_list[1]
        contract_address = item_list[3]
        #print(contract_name, contract_address)
        import_data = {
            "contract_name":contract_name,
            "contract_address":contract_address,
        }
        relate_contract_list.append(import_data)
    return relate_contract_list


"""
功能；抽取flowcode代码的相关代码，插入数据库contract_related
输入：
返回：0成功，-1失败
"""
def update_relate_code():
    # step 1 从数据库flow_code获得一批需要处理的代码，标记为is_relate。
    sql = """
    select * from flow_code where  is_relate = 0 limit 10
    """
    result = sql_appbk.mysql_com(sql)   # 原始代码列表
    if 0 == len(result):# 没有查询到结果返回
        print("no data need to update, sleep 100s")
        time.sleep(100)
        return 0
    # step 2 处理flow_code每一段代码，抽取相关代码，

    for item in result:  # 处理每一个原始的code数据，
        contract_id = item["id"]  # 代码id
        # print(contract_id)
        contract_code = item["contract_code"]   # 原始代码的contract_code
        contract_name = item["contract_name"]  # 原始代码的名称
        contract_address = item["contract_address"]  # 原始代码地址

        relate_code_list = get_code_related(contract_code)    #抽取相关代码


        data_list = []  # 一条代码的，需要插入数据库的orm数据列表
        for relate_code in relate_code_list:    # 处理每一行代码相关信息
            ralated_contract_name = relate_code["contract_name"]    # 相关代码名称
            related_contract_address = relate_code["contract_address"]  #   相关代码地址
            # 构建orm数据
            data = {}
            data["contract_name"] = contract_name   # 原始代码名称
            data["contract_address"] = contract_address  # 原始代码地址
            data["related_contract_name"] = ralated_contract_name    # 相关代码名称
            data["related_contract_address"] = related_contract_address    #    相关代码地址
            data["fetch_time"] = time.strftime("%Y-%m-%d %H:%M:%S")  # 更新时间
            data_list.append(data)


        # step 3 一条代码的结果,统一插入数据库，contract_related
        ret = sql_appbk.insert_data_list(data_list, "flow_contract_relation") # 插入 一条代码的相关信息

        #step 4 更新flow_code中的处理标记位，
        sql_update = """
        update flow_code set is_relate = 1 where id = {}
        """.format(contract_id)
        ret_code = sql_appbk.mysql_com(sql_update)

    return 0

if __name__ == '__main__':
    while 1:
        update_relate_code()