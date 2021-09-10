import argparse
import sys

english_freq = {"A":0.082,	"B":0.015,	"C":0.028,	"D":0.043,	"E":0.13,	"F":0.022,	"G":0.02,	"H":0.061,	"I":0.07,	"J":0.0015,	"K":0.0077,	"L":0.04,	"M":0.024,	"N":0.067,	"O":0.075,	"P":0.019,	"Q":0.00095,	"R":0.06,	"S":0.063,	"T":0.091,	"U":0.028,	"V":0.0098,	"W":0.024,	"X":0.0015,	"Y":0.02,	"Z":0.00074}
text = "AAZIQSTZZLHFTDBLRKKTMWBNECMEELHTBWVFTPVXVKPPIGRXUWIRQATDUMFKIZVMFWSDMRGAAWJYGATTAXUWDPIHYAEDBQNUHTVIUMMLVMGQHLAIIWRNZINLEO"
text = text.upper()

#creates dict of letters in string, stores freq of letters and returns dict and index of c
def createDict(text):
#Creates dict of all chars used in text, count starts at 0
    char_dict = {}
    for letters in english_freq:
        char_dict[letters] = letters = {'count':0,'indexOfC':0,'freq':english_freq[letters],'expected':0,'err':0}
    for chars in text:
        if chars in char_dict:
            char_dict[chars]['count'] += 1
            #print(char_dict[chars])
    num_chars = len(text)
    #total_index_of_c = 0
    for chars in char_dict.values():
        indexOfC = (chars['count'] / num_chars) * ((chars['count'] - 1)  / (num_chars - 1))
        chars['indexOfC'] = indexOfC
        #total_index_of_c += indexOfC
    
    #.066
    total_index_of_c = sum(i['indexOfC'] for i in char_dict.values())
    #print(total_index_of_c)
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
    total_ioc = sum(ioc_list) / key

    return total_ioc
    

def key_cracker(text,key):
    chi_dict = english_freq
    group_num = 0
    key_dict = {}
    keyword = []
    #group text into groups based on key size
    key_group = string_sort_key(text,key)
    #iter through each key group
    for group in key_group:
        #iters through letters A-Z to determine key
        for letters in english_freq.keys():
            temp_dict = createDict(v_decipher(group,letters))[0]
            #print(v_decipher(group,letters))
            #iter through each letter in decrypted text to see if chi_value is low
            for i in temp_dict.keys():
                temp_dict[i]['expected'] = len(group) * temp_dict[i]['freq']
                temp_dict[i]['err'] = (int((temp_dict[i]['count'] - temp_dict[i]['expected'])) ** 2 ) / temp_dict[i]['expected']
                #print(f"Letter = {i}, count{temp_dict[i]['count']} - expected{temp_dict[i]['expected']} ^2 = {int((temp_dict[i]['count'] - temp_dict[i]['expected'])) ^ 2},Err = {temp_dict[i]['err']}")
            chi_value = sum(i['err'] for i in temp_dict.values())
            if group_num in key_dict.keys():
                key_dict[group_num].update({letters:chi_value})
            else:
                key_dict = {group_num:{letters:chi_value}}
            
            #print(f"Group Number = {group_num}, Letter = {letters}, Chi-value = {chi_value}")
        group_num += 1
        for i in key_dict.values():
            print(min(i, key=i.get))

def v_cipher(text,key):
    cipher_text = []
    text = text.upper()
    key = list(gen_key(text,key).upper())
    for i in range(len(text)):
        cipher_char = ((ord(text[i]) + ord(key[i]))) % 26
        cipher_char += ord('A')
        cipher_text.append(chr(cipher_char))
    return "".join(cipher_text)

def v_decipher(text,key):
  cipher_text = [] 
  key = list(gen_key(text,key).upper())
  for i in range(len(text)): 
    x = (ord(text[i]) - ord(key[i]) + 26) % 26
    x += ord('A') 
    cipher_text.append(chr(x)) 
  return("" . join(cipher_text))

def gen_key(text,key):
    if len(text) == len(key):
        return(key)
    else:
        key = list(key)
        for i in range(len(text)- len(key)):
            key.append(key[i])
        return "".join(key) 


