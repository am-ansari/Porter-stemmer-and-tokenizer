# -*- coding: utf-8 -*-

import re
import numpy as np

def tokenize(line):
    
    hyphenExcl = re.compile(r"[^a-zA-Z']") 
    string = line.replace('.','')
    string = hyphenExcl.sub(" ",line)
    arr = string.split()   
    arrToken = []
    for i in range(len(arr)):
        skip_flag = False
        arr[i] = arr[i].replace('-',' ') 
        if arr[i].startswith('\'') == True or arr[i].endswith('\'') == True:
            if arr[i].startswith('\'') == True and arr[i].endswith('\'') == True and len(arr[i]) == 2:
                np.delete(arr,i)
                skip_flag = True
                continue
            else:    
                arr[i] = arr[i].replace('\'','') 
        if skip_flag == False:
            arr[i] = arr[i].lower()
            x = re.search(r"\w+",arr[i])
            if x is not None:
                arr[i] = x.group()
        arr[i] = arr[i].strip()
    idxArr = np.where(arr == "''")
    cleanArr = np.delete(arr, idxArr)
    for word in cleanArr:
        arrToken.append(word)
        
    return arrToken


