import os
import json
import argparse

import sys

sys.path.append("/home/jyw/Projects/CHESS/src")
from database_utils.sql_parser import get_sql_columns_dict

# directory_path = r"/home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/2024-11-17T14:45:29.370506/"
# output_file_path = r"refined_query.txt"


# get_sqlite_path('/home/jyw/Projects/CHESS/data/dev/dev_databases', "toxicology")
def get_sqlite_path(dev_db_path, db_id):
    """
    Constructs the path to the SQLite database file based on the provided database path and database ID.

    Args:
        dev_db_path (str): The path to the development databases directory.
        db_id (str): The ID of the database.

    Returns:
        str: The path to the SQLite database file.
    """
    path = os.path.join(os.path.join(dev_db_path, f"{db_id}"), f"{db_id}.sqlite")
    if os.path.exists(path):
        return path
    else:
        print("can not find the sqlite file: ", db_id)
        return None


def is_contain(sql_schema, schema_info):
    """
    Determines if the SQL schema is contained in the schema info.

    Args:
        sql_schema (Dict[str, List[str]]): The gold SQL schema info.
        schema_info (Dict[str, Dict[str, List[str]]]):  The SQL schema infered by LLM, which is a dictionary with the question ID as the key and the schema information(table, column_list) as the value.

    Returns:
        bool: True if the SQL schema is contained in the schema info, False otherwise.
    """
    for table, columns in sql_schema.items():
        if table not in schema_info:
            return False
        for column in columns:
            if column not in schema_info[table]:
                return False
    return True


def to_lowercase(data):
    """
    Trans data into lowercase
    """
    if isinstance(data, dict):
        return {k.lower(): to_lowercase(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_lowercase(i) for i in data]
    elif isinstance(data, str):
        return data.lower()
    else:
        return data


def all_json_paths(directory_path):
    """
    Get all JSON file paths in the directory, ordered by the number at the beginning of the file name, total number of files is 1534(0-1533).
    Args:
        directory_path (str): The path to the directory containing the JSON files, which are named with a number followed by an underscore and the database ID. E.g., "1_toxicology.json".
    Returns:
        json_paths (List[str]): A list of paths to the JSON files in the directory, ordered by the number at the beginning of the file name.
    """
    json_paths = []
    # 获取目录中的所有文件，并按照文件名开头的数字大小进行升序排列
    json_paths = sorted(
        [
            f
            for f in os.listdir(directory_path)
            if f.endswith(".json") and f[0].isdigit()
        ],
        key=lambda x: int(x.split("_")[0]),
    )
    json_paths = [os.path.join(directory_path, f) for f in json_paths]
    return json_paths


def merge_dicts(dict_list):
    """
    The union of the 20 SQL schema dict infos, merge a list of dictionaries into one dictionary,
    Args:
        dict_list: List[Dict[str, Any]]
    Returns:
        merged_dict: Dict[str, Any]
    """
    merged_dict = {}
    for d in dict_list:
        for key, value in d.items():
            if key not in merged_dict:
                merged_dict[key] = value
            else:
                if isinstance(value, list):
                    merged_dict[key] = list(set(merged_dict[key] + value))
                elif isinstance(value, dict):
                    merged_dict[key] = merge_dicts([merged_dict[key], value])
                else:
                    merged_dict[key] = value
    return merged_dict


# 抽取出来的schema_info
def get_schema_info(json_paths):
    """
    Get the schema information from the JSON files, which are the output of the LLM model.
    Args:
        json_paths: List[str]
    Returns:
        schema_info: Dict[str, Dict[str, List[str]]]
        schema_info["1"] = {'frpm': ['free meal count (ages 5-17)', \
                                    'free meal count (k-12)', \
                                    'enrollment (ages 5-17)', \
                                    'frpm count (k-12)', \
                                    'enrollment (k-12)'], \
                            'schools': ['edopscode', 'gsserved']}
    """
    schema_info = {}

    for file_path in json_paths:
        id = file_path.split("/")[-1].split("_")[0]
        with open(file_path, "r") as f:
            data = json.load(f)

            for item in data:
                if item.get("tool_name") == "retrieve_context":
                    schema_dict = item.get("schema_with_descriptions", {})
                    # sql_schema
                    schema = {}
                    for table, column_info in schema_dict.items():
                        column_names = [col_name for col_name in column_info.keys()]
                        schema[table] = column_names
                    # print(schema)
        schema_info[id] = schema
    return schema_info


def get_schema_info_refine(txt_path, db_path):
    # 我们现在有一个txt文件，每20行为一组，第一行是question_id和数据库名称，以空格分隔
    # 之后的20行，里面的每一行都是一条SQL
    # 该21行结束后，有一个空行表示改组结束，之后开启的是下一组的SQL信息
    # 1. 抽取每条SQL的schema（table_name & column_names）该步可以使用get_sql_columns_dict
    # 2. 将schema信息取并集，得到这一组的schema_info
    # 3. 最终的保存形式为dict, key为question_id, value为这一组并集的schema_info

    q_id = "0"  # question_id in JSON filename
    db_id = ""  # database category name, e.g. "financial"
    schema_info = {}  # return value
    refine_schema_list = []  # templately store the schema of each SQL in a group

    with open(txt_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # The end of a predicted SQL group
            if line.strip() == "":
                # Union
                refine_schema = merge_dicts(refine_schema_list)
                schema_info[q_id] = refine_schema
                # Reset
                refine_schema_list = []
                cnt = 0
            # The start of a predicted SQL group, get question_id and database category name
            elif line.strip()[0].isdigit():
                q_id = line.strip().split()[0]
                db_id = line.strip().split()[1]
            # SQL line
            else:
                cnt += 1
                sqlite_path = get_sqlite_path(db_path, db_id)
                try:
                    # Get the schema(Dict[str, List[str]]) of the SQL
                    refine_schema_list.append(get_sql_columns_dict(sqlite_path, line))
                except Exception as e:
                    print(f"Error processing line: {line.strip()} - {e}")
    return schema_info


def main_refine(gold_sql_path, db_path, output_file_path, txt_path):
    schema_info_refine = get_schema_info_refine(txt_path, db_path)
    print(len(schema_info_refine))
    # gold_sql & judge
    cnt = 0
    tol = 0
    error_res = {}
    with open(gold_sql_path, "r") as f:
        gold_datas = json.load(f)
        for gold_data in gold_datas:
            tol += 1
            # gold_sql
            q_id = str(gold_data["question_id"])
            db_id = gold_data["db_id"]
            gold_sql = gold_data["SQL"]

            sqlite_path = get_sqlite_path(db_path, db_id)
            gold_schema = get_sql_columns_dict(sqlite_path, gold_sql)
            gold_schema = to_lowercase(gold_schema)

            # judge
            if is_contain(gold_schema, schema_info_refine[q_id]):
                cnt += 1
            else:
                error_res[q_id] = error_res[q_id] = {
                    "gold_schema": gold_schema,
                    "schema_info": schema_info_refine[q_id],
                }
    print("Correct: ", cnt, "Total: ", tol)
    print("Recall: ", cnt / tol)

    # 结果写入json文件
    with open(output_file_path, "w") as f:
        json.dump(error_res, f)
    return error_res


def main(directory_path, gold_sql_path, db_path, output_file_path):
    # schema_info
    json_paths = all_json_paths(directory_path)
    # print(len(json_paths))
    schema_info = get_schema_info(json_paths)
    # print(schema_info)

    # gold_sql & judge
    cnt = 0
    tol = 0
    error_res = {}
    with open(gold_sql_path, "r") as f:
        gold_datas = json.load(f)
        for gold_data in gold_datas:
            tol += 1
            # gold_sql
            q_id = str(gold_data["question_id"])
            db_id = gold_data["db_id"]
            gold_sql = gold_data["SQL"]

            sqlite_path = get_sqlite_path(db_path, db_id)
            gold_schema = get_sql_columns_dict(sqlite_path, gold_sql)
            gold_schema = to_lowercase(gold_schema)

            # judge
            if is_contain(gold_schema, schema_info[q_id]):
                cnt += 1
            else:
                error_res[q_id] = error_res[q_id] = {
                    "gold_schema": gold_schema,
                    "schema_info": schema_info[q_id],
                }
    print("Correct: ", cnt, "Total: ", tol)
    print("Recall: ", cnt / tol)

    # 结果写入json文件
    with open(output_file_path, "w") as f:
        json.dump(error_res, f)
    return error_res


#   python -m post_process.utils.extract_schema --directory_path /home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/2024-11-17T14:45:29.370506/ --gold_sql_path /home/jyw/Projects/CHESS/data/dev/dev.json --db_path /home/jyw/Projects/CHESS/data/dev/dev_databases --output_file_path /home/jyw/Projects/CHESS/post_process/error_res_refine.json --type refined

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--directory_path", type=str)
    args.add_argument("--gold_sql_path", type=str)
    args.add_argument("--db_path", type=str)
    args.add_argument("--output_file_path", type=str)
    args.add_argument("--type", type=str)  # refined or raw
    args = args.parse_args()

    if args.type == "refined":
        txt_path = r"/home/jyw/Projects/CHESS/post_process/refined_query_with_info.txt"
        main_refine(args.gold_sql_path, args.db_path, args.output_file_path, txt_path)
    else:
        main(
            args.directory_path, args.gold_sql_path, args.db_path, args.output_file_path
        )
