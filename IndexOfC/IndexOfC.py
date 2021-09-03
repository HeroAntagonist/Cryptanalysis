import argparse
import sys


text = "Moqkuwsctnmaastolauwakaqxapsbasphyuqkgdoavxwbggywapaaoobdzxjwhebefksckeymomjeasomoileguvwzcus"

#creates dict of letters in string, stores freq of letters and returns dict and index of c
def createDict(text):
#Creates dict of all chars used in text, count starts at 0
    char_dict = {}
    for chars in text:
        if chars in char_dict:
            continue
        else:
            #[Count of occurance, IndexOfC]
            char_dict[chars] = chars = {'count':0,'indexOfC':0}
    for chars in text:
        if chars in char_dict:
            char_dict[chars]['count'] += 1
            #print(char_dict[chars])
    num_chars = len(text)
    for chars in char_dict.values():
        indexOfC = (chars['count'] * (chars['count'] - 1)) / (num_chars * (num_chars - 1))
        #print(f"{chars['count']} * {chars['count'] - 1} / {num_chars} * {num_chars - 1} = {indexOfC}")
        chars['indexOfC'] = indexOfC
    total_index_of_c = sum(i['indexOfC'] for i in char_dict.values())
    return char_dict, total_index_of_c
         

#groups string based on key length
def string_sort_key(string,key):
    temp = []
    pos_start = 0
    for i in (range(key)):
        temp.append(string[pos_start::key])
        pos_start +=1
    return (temp)

#returns sum of ioc for all string groups
def ioc(text,key):
    ioc_list = []
    string_list = string_sort_key(text,key)
    for i in string_list:
        ioc_list.append(createDict(i)[1])
    total_ioc = sum(ioc_list)

    return total_ioc


for i in range(20):
    print(f"Key = {i}, IOC = {ioc(text,i)}")

    


