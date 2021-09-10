

#Avg distribution of letter in english langugage
english_freq = {"A":0.082,	"B":0.015,	"C":0.028,	"D":0.043,	"E":0.13,	"F":0.022,	"G":0.02,	"H":0.061,	"I":0.07,	"J":0.0015,	"K":0.0077,	"L":0.04,	"M":0.024,	"N":0.067,	"O":0.075,	"P":0.019,	"Q":0.00095,	"R":0.06,	"S":0.063,	"T":0.091,	"U":0.028,	"V":0.0098,	"W":0.024,	"X":0.0015,	"Y":0.02,	"Z":0.00074}
text = "AAZIQSTZZLHFTDBLRKKTMWBNECMEELHTBWVFTPVXVKPPIGRXUWIRQATDUMFKIZVMFWSDMRGAAWJYGATTAXUWDPIHYAEDBQNUHTVIUMMLVMGQHLAIIWRNZINLEO".upper()


#Creates dict of letters in string, stores freq of letters and returns dict and index of c
def createDict(text):
#Creates dict of all chars used in text, count starts at 0
    char_dict = {}
    for letters in english_freq:
        char_dict[letters] = letters = {'count':0,'indexOfC':0,'freq':english_freq[letters],'expected':0,'err':0}
    for chars in text:
        if chars in char_dict:
            char_dict[chars]['count'] += 1
    num_chars = len(text)
    for chars in char_dict.values():
        indexOfC = (chars['count'] / num_chars) * ((chars['count'] - 1)  / (num_chars - 1))
        chars['indexOfC'] = indexOfC
    total_index_of_c = sum(i['indexOfC'] for i in char_dict.values())
    return char_dict, total_index_of_c
         

#Groups string based on key length
def string_sort_key(string,key):
    temp = []
    pos_start = 0
    for i in (range(key)):
        temp.append(string[pos_start::key])
        pos_start +=1
    return (temp)

#Returns sum of Index of coincidence for all string groups
def ioc(text,key):
    ioc_list = []
    string_list = string_sort_key(text,key)
    for i in string_list:
        ioc_list.append(createDict(i)[1])
    total_ioc = sum(ioc_list) / key
    return total_ioc
    
#Outputs key for encrpyted Vigenere Text
def key_cracker(text,key_l):
    chi_dict = english_freq
    group_num = 0
    key = []
    key_dict = {}
    #group text into groups based on key size
    key_group = string_sort_key(text,key_l)
    #iter through each key group
    for group in key_group:
        #iters through letters A-Z to determine key
        for letters in english_freq.keys():
            temp_dict = createDict(v_decipher(group,letters))[0]
            #iter through each letter in decrypted text to see if chi_value is low
            for i in temp_dict.keys():
                #Calculates expected letter count vs actual letter count based on english letter freq
                temp_dict[i]['expected'] = len(group) * temp_dict[i]['freq']
                temp_dict[i]['err'] = (int((temp_dict[i]['count'] - temp_dict[i]['expected'])) ** 2 ) / temp_dict[i]['expected']
            #Lower value = closer to avg english letter distribution
            chi_value = sum(i['err'] for i in temp_dict.values())
            if group_num in key_dict.keys():
                key_dict[group_num].update({letters:chi_value})
            else:
                key_dict = {group_num:{letters:chi_value}}
        group_num += 1
        for i in key_dict.values():
            key.append(min(i, key=i.get))
    return "".join(key)

#Encodes message with key using Vigenere Cipher
def v_cipher(text,key):
    cipher_text = []
    text = text.upper()
    key = list(gen_key(text,key).upper())
    for i in range(len(text)):
        cipher_char = ((ord(text[i]) + ord(key[i]))) % 26
        cipher_char += ord('A')
        cipher_text.append(chr(cipher_char))
    return "".join(cipher_text)

#Decodes message with encoded Vigenere text and key
def v_decipher(text,key):
  cipher_text = [] 
  key = list(gen_key(text,key).upper())
  for i in range(len(text)): 
    x = (ord(text[i]) - ord(key[i]) + 26) % 26
    x += ord('A') 
    cipher_text.append(chr(x)) 
  return("" . join(cipher_text))

#Outputs Vigenere key that repeats until same length as message
def gen_key(text,key):
    if len(text) == len(key):
        return(key)
    else:
        key = list(key)
        for i in range(len(text)- len(key)):
            key.append(key[i])
        return "".join(key) 


print(key_cracker(text,6))