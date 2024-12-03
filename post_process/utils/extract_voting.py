import os
import json
import argparse

import sys

sys.path.append("/home/jyw/Projects/CHESS/src")
from database_utils.execution import aggregate_sqls

# sys.path.append("/home/jyw/Projects/CHESS/src")
# from database_utils.sql_parser import get_sql_columns_dict


db_path = "/home/jyw/Projects/CHESS/data/dev/dev_databases"


def get_sqlite_path(dev_db_path, db_id):
    path = os.path.join(os.path.join(dev_db_path, f"{db_id}"), f"{db_id}.sqlite")
    if os.path.exists(path):
        return path
    else:
        print("can not find the sqlite file: ", db_id)
        return None


def get_SQL_list(input_txt_path) -> dict:
    """
    Get SQL group(List[str]) from the input txt file
    Args:
        input_txt_path(str): Input txt file path
    Returns:
        sql_info(Dict[str, Dict[str, List(str)]]): {q_id: {"db_id": db_id, "sql_list": sql_list}}
    """
    # dict[db_info] = [sql1, sql2, ...]
    with open(input_txt_path, "r") as f:
        lines = f.readlines()
        sql_info = {}
        sql_list = []
        q_id = ""  # 本质是数字
        db_id = ""
        cnt = 0

        for line in lines:
            # 空行: 加入sql_listsql_list
            if line.strip() == "":
                sql_info[q_id] = {"db_id": db_id, "sql_list": sql_list}
                sql_list = []
            # sql line
            elif line.strip()[0].isdigit():
                q_id = line.strip().split()[0]
                db_id = line.strip().split()[1]
                cnt = 0
            else:
                # SQL line
                cnt += 1
                sql_list.append(line.strip())
    return sql_info


def get_voting(sql_info, db_path):
    """
    Get the voting result of the SQLs
    Args:
        sql_info(Dict[str, Dict[str, List(str)]]): {q_id: {"db_id": db_id, "sql_list": sql_list}}
        db_path(str): Path to the database file
    Returns:
        sql_voting_dict(Dict[str, str]): {q_id: top-1 voting_result}
    """
    sql_voting_dict = {}
    for q_id, info in sql_info.items():
        db_id = info["db_id"]
        sqlit_path = get_sqlite_path(db_path, db_id)
        sql_voting = aggregate_sqls(sqlit_path, info["sql_list"])  # Top 1 voting result
        sql_voting_dict[q_id] = sql_voting
    return sql_voting_dict


def to_file(sql_voting_dict, out_txt, out_json):
    """
    Write the voting result to the output file(JSON & txt)
    """
    # sql_voting_dict = {}
    # for q_id, info in sql_.items():
    #     db_id = info["db_id"]
    #     sqlit_path = get_sqlite_path(db_path, db_id)
    #     sql_voting = aggregate_sqls(sqlit_path, info["sql_list"])
    #     sql_voting_dict[q_id] = sql_voting
    #     # break
    with open(out_txt, "w") as f:
        for q_id, sql_voting in sql_voting_dict.items():
            f.write(sql_voting + "\n")
    with open(out_json, "w") as f:
        json.dump(sql_voting_dict, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_txt_path", type=str, default="dev_sqls.txt")
    parser.add_argument("--output_txt_path", type=str, default="voting_result.txt")
    parser.add_argument("--output_json_path", type=str, default="voting_result.json")
    args = parser.parse_args()

    sql_info = get_SQL_list(args.input_txt_path)
    sql_voting_dict = get_voting(sql_info, db_path)
    to_file(sql_voting_dict, args.output_txt_path, args.output_json_path)
    print("Done!")
