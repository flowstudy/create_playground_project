import time

import sql_appbk
import build_flow_project

def update_playground_project():
    # step 1 从数据库flow_code获得一批需要处理的代码，标记为is_relate。
    sql = """
    select * from flow_code where playground_project_id is null limit 10
    """
    result = sql_appbk.mysql_com(sql)   # 原始代码列表
    if 0 == len(result):# 没有查询到结果返回
        print("no data need to update, sleep 100s")
        time.sleep(100)
        return 0
    # step 2 处理flow_code每一段代码，抽取相关代码，

    for item in result:  # 处理每一个原始的code数据，
        contract_id = item["id"]  # 代码id
        contract_name = item["contract_name"]  # 原始代码的名称
        contract_address = item["contract_address"]  # 原始代码地址

        try:
            project_id = build_flow_project.build_flow_project(contract_address, contract_name)   #抽取相关代码
            print("process------------", contract_id,"get project id", project_id)

            sql_update = """
            update flow_code set  playground_project_id='{}' where id = {}
            """.format(project_id, contract_id)
            ret_code = sql_appbk.mysql_com(sql_update)
        except Exception as e:
            print("process------------", contract_id, "error", e)

            sql_update = """
            update flow_code set  playground_project_id='{}' where id = {}
            """.format("-1", contract_id)
            ret_code = sql_appbk.mysql_com(sql_update)

            continue

    return 0

if __name__ == '__main__':
    #update_playground_project()
    while 1:
        update_playground_project()