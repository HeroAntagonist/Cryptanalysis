#Ci = (Ti + Ki) mod(m)
#Ci - i-th character of the ciphertext
#Ti - i-th character of the open text
#Ki - i-th character of the key phrase (if the key phrase is shorter than the open text, which is usual, than the keyphrase is reapeated to math the length of the open text)
#m - length of the alphabet

#Creates a key with same len as text, easier to apply cipher this way


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

print(v_cipher("IfthekeysizehappenstohavebeenthesameastheassumednumberofcolumnsthenalltheletterswithinasinglecolumnwillhavebeenencipheredusingthesamekeyletterineffectasimpleCaesarcipherappliedtoarandomselectionofEnglishplaintextcharacters","testkey"))
print(v_decipher("AAZIQSTZZLHFTDBLRKKTMWBNECMEELHTBWVFTPVXVKPPIGRXUWIRQATDUMFKIZVMFWSDMRGAAWJYGATTAXUWDPIHYAEDBQNUHTVIUMMLVMGQHLAIIWRNZINLEO","ALIENS"))


    



