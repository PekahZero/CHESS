# -*- coding: utf-8 -*-
# @Time    : 2023/7/31 09:46
# @Author  : Ray
# @Email   : httdty2@163.com
# @File    : evaluation.py
# @Software: PyCharm
import argparse
import json

from eval.spider_evaluator import EvaluateTool as SpiderEvaluateTool
from eval.bird_evaluator import EvaluateTool as BirdEvaluateTool
from eval.science_evaluator import EvaluateTool as ScienceEvaluateTool


def main(gold, pred, db_dir, ts_db):
    with open(gold, "r") as f:
        gold = json.load(f)
    with open(pred, "r") as f:
        preds = [p.strip() for p in f.readlines()]

    if len(preds[-1]) == 0:
        preds.pop(-1)
    assert len(preds) == len(gold)

    if "bird" in db_dir:
        evaluator = BirdEvaluateTool(iterate_num=2, meta_time_out=30, verbose=True)
        evaluator.register_golds(gold, db_dir)

    elif "science" in db_dir:
        evaluator = ScienceEvaluateTool(iterate_num=2, meta_time_out=30, verbose=True)
        evaluator.register_golds(gold, db_dir)

    else:  # spider
        evaluator = SpiderEvaluateTool(verbose=True)
        evaluator.register_golds(gold, db_dir, ts_db)

    evaluator.evaluate(preds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold", type=str)
    parser.add_argument("--pred", type=str)
    parser.add_argument("--db", type=str)
    parser.add_argument("--ts_db", default="", type=str)
    args = parser.parse_args()

    main(args.gold, args.pred, args.db, args.ts_db)

# science(暂时不可用)
# python -m eval.evaluation --gold=./data/science/dev/dev.json --db=./data/science/dev/dev_databases --pred=/home/jyw/Projects/CHESS/post_process/data/chess/science/predictions.txt

# spider(需要使用原来的dev.json)
# python -m eval.evaluation --gold=./data/spider/dev.json --db=./data/spider/dev/dev_databases --pred=/home/jyw/Projects/CHESS/post_process/data/chess/spider/predictions.txt

# bird(chess)
# python -m eval.evaluation --gold=./data/bird/dev/dev.json --db=./data/bird/dev_databases --pred=/home/jyw/Projects/CHESS/post_process/data/chess/bird/predictions.txt

# bird(mac-sql)
# python -m eval.evaluation --gold=./data/bird/dev/dev.json --db=./data/bird/dev_databases --pred=/home/jyw/Projects/CHESS/post_process/data/mac-sql/predict_dev.txt

# bird(din-sql)
# python -m eval.evaluation --gold=./data/bird/dev/dev.json --db=./data/bird/dev/dev_databases --pred=/home/jyw/Projects/CHESS/post_process/data/din-sql/pred_RE.txt
