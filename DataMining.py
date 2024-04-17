import pandas as pd 
import jieba
from china_regions import province_city

def get_percentage_of_missing_data(data_ser):
    total = len(data_ser)
    missing_data = 0
    for d in data_ser:
        if pd.isnull(d):
            missing_data += 1
    return missing_data/total

def judge_province_chinese(input_str):
    seg_list = jieba.lcut(input_str)
    len_s = len(seg_list)

    if len_s > 1:
        first = seg_list[0]
        second = seg_list[1]
    else:
        first = seg_list[0]

    if len_s > 1:
        for itm in province_city.items():
            pvr = itm[0]
            dic = itm[1]
            if first in pvr:
                return pvr
            else:
                for d in dic.items():
                    if first in d[0]:
                        return pvr
                    else:
                        for n in d[1]:
                            if first in n:
                                return pvr
                        
        for itm in province_city.items():
            pvr = itm[0]
            dic = itm[1]
            if second in pvr:
                return pvr
            else:
                for d in dic.items():
                    if second in d[0]:
                        return pvr
                    else:
                        for n in d[1]:
                            if second in n:
                                return pvr
    else:
        for itm in province_city.items():
            pvr = itm[0]
            dic = itm[1]
            if first in pvr:
                return pvr
            else:
                for d in dic.items():
                    if first in d[0]:
                        return pvr
                    else:
                        for n in d[1]:
                            if first in n:
                                return pvr
    return None



















