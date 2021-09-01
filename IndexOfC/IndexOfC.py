import argparse
import sys

def indexOfC():
    #Creates dict of all chars used in text, count starts at 0
    try:
        text = str(sys.argv[1])
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
        return total_index_of_c
    except IndexError:
        raise Exception("Script requires input text, e.x. IndexOfC.py 'lorem ipsum, etc etc'")


print(indexOfC())