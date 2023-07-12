import pandas as pd

import pandas as pd


def getinfo(filename):
    result = []
    dataframe = pd.read_excel(filename)
    i = 1
    for row in dataframe.iterrows():
        ls = [str(i)]
        i = i + 1
        for cell in row[1]:
            ls.append(cell)
        result.append(ls)
    return result
