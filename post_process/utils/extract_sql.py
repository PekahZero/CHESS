import os
import json
import argparse


# directory_path = r"/home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/2024-11-17T14:45:29.370506/"
# output_file_path = r"refined_query.txt"


def all_json_paths(directory_path):
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


def refined_to_file(json_paths, output_file_path="refined_query.txt"):
    cnt = 0

    for file_path in json_paths:
        with open(file_path, "r") as f:
            data = json.load(f)
            found_revise = False

            for item in data:
                if item.get("tool_name") == "revise":
                    found_revise = True
                    # 获取 candidates 列表
                    sql_dict_list = item.get("candidates", [])
                    if len(sql_dict_list) != 20:
                        print(
                            file_path, " is not 20 candidates, is ", len(sql_dict_list)
                        )

                    # SQL写入文件
                    with open(output_file_path, "a") as output_file:
                        for sql_dict in sql_dict_list:
                            output_file.write(sql_dict["refined_query"].strip() + "\n")
                    cnt += 1
                    with open(output_file_path, "a") as output_file:
                        output_file.write("\n")

            if not found_revise:
                print(file_path, " tool_name is not revise")

    print("------ finish writing to file: ", output_file_path)
    return cnt


def refined_to_file_with_info(
    json_paths, output_file_path="refined_query_with_info.txt"
):
    cnt = 0

    for file_path in json_paths:
        with open(file_path, "r") as f:
            data = json.load(f)
            found_revise = False

            for item in data:
                if item.get("tool_name") == "revise":
                    found_revise = True
                    # 获取 candidates 列表
                    sql_dict_list = item.get("candidates", [])
                    if len(sql_dict_list) != 20:
                        print(
                            file_path, " is not 20 candidates, is ", len(sql_dict_list)
                        )
                    # 添加info
                    file_path_id = file_path.split("/")[-1].split("_")[0]
                    tmp = file_path.split("/")[-1].split(".")[0]
                    tmp1 = [i for i in tmp.split("_") if i != file_path_id]
                    file_path_db = "_".join(tmp1)
                    info = file_path_id + " " + file_path_db

                    # SQL写入文件
                    with open(output_file_path, "a") as output_file:
                        output_file.write(info + "\n")
                        for sql_dict in sql_dict_list:
                            output_file.write(sql_dict["refined_query"].strip() + "\n")
                    cnt += 1
                    with open(output_file_path, "a") as output_file:
                        output_file.write("\n")

            if not found_revise:
                print(file_path, " tool_name is not revise")

    print("------ finish writing to file: ", output_file_path)
    return cnt


def candidates_to_file(json_paths, output_file_path="candidates.txt"):
    cnt = 0

    for file_path in json_paths:
        with open(file_path, "r") as f:
            data = json.load(f)

            for item in data:
                if item.get("tool_name") == "generate_candidate":
                    sql_dict_list = item.get("candidates", [])
                    if len(sql_dict_list) != 20:
                        print(
                            file_path, " is not 20 candidates, is ", len(sql_dict_list)
                        )
                        # 补全
                        if len(sql_dict_list) == 0:
                            for _ in range(20):
                                sql_dict_list.append({"SQL": "SELECT * FROM table"})
                        else:
                            i = 0
                            while len(sql_dict_list) < 20:
                                sql_dict_list.append(sql_dict_list[i])
                                i += 1

                    # SQL写入文件
                    with open(output_file_path, "a") as output_file:
                        for sql_dict in sql_dict_list:
                            output_file.write(sql_dict["SQL"].strip() + "\n")
                    cnt += 1
                    with open(output_file_path, "a") as output_file:
                        output_file.write("\n")

    print("------ finish writing to file: ", output_file_path)
    return cnt


def main(directory_path, output_file_path, type):
    json_paths = all_json_paths(directory_path)
    print("Already get json_paths: ", len(json_paths))

    if type == "refined":
        # 生成 refined_query.txt
        refined_to_file_with_info(json_paths, output_file_path)
    elif type == "candidates":
        # 生成 candidates.txt
        candidates_to_file(json_paths, output_file_path)
    print("------ finish writing to file: ", output_file_path)


# command
# python -m post_process.utils.extract_sql --directory_path /home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/2024-11-17T14:45:29.370506/ --output_file_path post_process/refined_query_with_info.txt --type refined

# python -m post_process.utils.extract_sql --directory_path /home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/2024-12-06T09:34:31.669070 --output_file_path post_process/data/chess/spider/20_candidates.txt --type candidates
# python -m post_process.utils.extract_sql --directory_path /home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/2024-12-06T09:34:31.669070 --output_file_path post_process/data/chess/spider/20_candidates.txt --type candidates

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory_path", type=str)
    parser.add_argument("--output_file_path", type=str)
    parser.add_argument("--type", type=str, default="refined")  # refined or candidates

    args = parser.parse_args()

    main(args.directory_path, args.output_file_path, args.type)


# python -m post_process.utils.extract_sql --directory_path /home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/Spider --output_file_path post_process/data/chess/spider/new_20_candidates.txt --type candidates

# python -m post_process.utils.extract_sql --directory_path /home/jyw/Projects/CHESS/results/dev/CHESS_IR_CG_UT/dev/Science --output_file_path post_process/data/chess/science/20_candidates.txt --type candidates
