from typing import List
import math


# list quiz
# 1. 定義一個筆電變數 hp_800_g5 500鎂 另一個筆電變數 hp_800_g6 600鎂
# 2. 比較是不是 hp_800_g6 比較貴
# 3. 因為 hp_800_g5 比較便宜，所以買下來但是要加税 0.25鎂
# 4. 但是每天工作只有 10鎂 幾天才可以買到
def list_quiz():
    hp_800_g5=500
    hp_800_g6=600
    if (hp_800_g5<hp_800_g6):
        days=(((hp_800_g5+0.25)//10))+1
        #if days %1 !=0:
            #days=days+1
            #return days
    return days


    pass


# dict quiz
# 1. 建立空的dict叫 intel_chip
# 2. 加入kaby lake跟comet lake
# 3. kaby lake太爛了，改成baby lake
# 4. baby lake真的太爛了被drop 刪除baby lake
# 5. intel後來被AMD消滅了 整個intel_chip直接被AMD清空
def dict_quiz():
    intel_chip={}
    intel_chip_new={'kaby_lake':0,'comet_lake':1} 
    intel_chip.update(intel_chip_new)   #update是否不能不填值？目前測試是無法
    # del intel_chip['kaby_lake']
    # intel_chip_baby={'baby_lake':2}
    # intel_chip.update(intel_chip_baby)
    intel_chip['baby_lake']= intel_chip.pop('kaby_lake') # 這一行等同於上面三行，並且不用有多的變數以及新的baby_lake取代kaby_lake，他的值也是跟kaby_lake一樣是0，參考https://blog.csdn.net/a1007720052/article/details/81542134
    del intel_chip['baby_lake']
    intel_chip.clear()
    #intel_chip={}
    
    return intel_chip



    pass


# function quiz
'''
做一個用年份來查詢cpu代號的function，給年份會傳回cpu的名字，沒有的話就寫 None
你的資料有以下cpu: kaby lake、ice lake、comet lake、alder lake、whisky lake，年份依序2015-2019 (提示用dict)
ex:
input:  [2015,2016,2021]
output: ['kaby lake','ice lake',None]
'''


def search_cpu_codename(years: list) -> list:
    cpu_dict={'kaby lake':2015,'ice lake':2016,'comet lake':2017,'alder lake':2018,'whisky lake':2019}
    output_key=[]
    for input_year in years:
        for cpu_key,cpu_value in cpu_dict.items():
            if input_year ==cpu_value:
                output_key.append(cpu_key)
                break
        else:
            output_key.append(None)
    return output_key
    
    pass
