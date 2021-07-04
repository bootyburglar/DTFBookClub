from typing import List
import math


# list quiz
# 1. 定義一個筆電變數 hp_800_g5 500鎂 另一個筆電變數 hp_800_g6 600鎂
# 2. 比較是不是 hp_800_g6 比較貴
# 3. 因為 hp_800_g5 比較便宜，所以買下來但是要加税 0.25鎂
# 4. 但是每天工作只有 10鎂 幾天才可以買到
def list_quiz():
    hp_800_g5 = 500
    hp_800_g6 = 600
    if hp_800_g6 > hp_800_g5:
        return math.ceil((hp_800_g5 + 0.25) / 10)


# dict quiz
# 1. 建立空的dict叫 intel_chip
# 2. 加入kaby lake跟comet lake
# 3. kaby lake太爛了，改成baby lake
# 4. baby lake真的太爛了被drop 刪除baby lake
# 5. intel後來被AMD消滅了 整個intel_chip直接被AMD清空
def dict_quiz():
    intel_chip = {}
    return intel_chip


# function quiz
'''
做一個用年份來查詢cpu代號的function，給年份會傳回cpu的名字，沒有的話就寫 None
你的資料有以下cpu: kaby lake、ice lake、comet lake、alder lake、whisky lake，年份依序2015-2019 (提示用dict)
ex:
input:  [2015,2016,2021]
output: ['kaby lake','ice lake',None]
'''


def search_cpu_codename(years: List) -> List:
    cpu_codename = {}
    output = []
    cpus = ['kaby lake', 'ice lake', 'comet lake', 'alder lake', 'whisky lake']
    cpu_years = [2015, 2016, 2017, 2018, 2019]
    # construct dict
    for i in range(len(cpu_years)):
        cpu_codename.update({cpu_years[i]: cpus[i]})
    # construct output
    for year in years:
        if year not in cpu_years:
            output.append(None)
        else:
            output.append(cpu_codename[year])
    return output
