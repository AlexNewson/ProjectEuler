import pandas as pd


def print_problem(problem_id):
    basic = pd.read_csv('https://projecteuler.net/minimal=problems',
                        sep='##',
                        engine='python')

    print("Promblem: ", problem_id)
    print("Title:    ", basic.loc[problem_id - 1]["Description"])
    print("URL:      ", "https://projecteuler.net/problem=" + str(problem_id))
    print("")

