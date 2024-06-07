import logging

import sys
from time import time

from matplotlib import pyplot as plt

sys.path.append("..")

from evaluation.benchmarks import simulation, run_xges
from xges.search import XGES

res = []
for i in range(30):
    data, dag = simulation(30, 10000, 3, seed=i)
    _, stats = run_xges(data, extended_search=True, verbose=0)
    score_xges_cpp = stats["score"]

    model = XGES()
    logging.basicConfig(level=logging.INFO)
    start_time = time()
    model.fit(data, extended_search=True)
    # print("Execution time: ", time() - start_time)
    score_xges_python = model.total_score
    res.append((score_xges_cpp, score_xges_python))
    # res.append((score_xges_cpp, stats["time"]))

import pandas as pd
# print(pd.DataFrame(res, columns=["score", "time"]).describe())
# exit(0)

df = pd.DataFrame(res, columns=["score_xges_cpp", "score_xges_python"])
df["diff"] = df["score_xges_cpp"] - df["score_xges_python"]

df["cpp_win"] = df["diff"] > 1e-5
df["python_win"] = df["diff"] < -1e-5
df["draw"] = (df["diff"] >= -1e-5) & (df["diff"] <= 1e-5)

print(
    f"CPP wins: {df['cpp_win'].sum()} ({df['cpp_win'].sum() / len(df) * 100:.2f}%) | Python wins: {df['python_win'].sum()} ({df['python_win'].sum() / len(df) * 100:.2f}%) | Draw: {df['draw'].sum()} ({df['draw'].sum() / len(df) * 100:.2f}%)"
)
