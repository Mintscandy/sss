import openpyxl

def getTotal(name):
    try:
        workbook = openpyxl.load_workbook(name)
        sheet = workbook.active
        i = 1
        while True:
            rpos = 'A' + str(i)
            if str(sheet[rpos].value) == 'None':
                break
            i = i + 1
        return i
    except FileNotFoundError:
        return None


def getinfo(name, index):
    workbook = openpyxl.load_workbook(name)
    sheet = workbook.active
    result = []
    s = ['A', 'B', 'C', 'D', 'E']
    for i in range(len(s)):
        pos = s[i] + str(index)
        result.append(str(sheet[pos].value))
    return result

def getReadData(filename):
    result = []
    i = 2
    len = getTotal(filename)
    while i < len:
        result.append(getinfo(filename, i))
        i = i + 1

    return result
