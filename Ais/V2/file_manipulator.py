from EncoderDecoder import decoder, encoder
from typing import List
file_path = "/Users/rio/Desktop/SideWorks/InternetProviderPhoneNumberExtracter/data.txt"

def listnumbers_to_encoded_string(numb_list:List[List[int]]):
    s = ""
    for nb in numb_list:
        # x = encoder(nb) + "\n"
        # x += s
        # s = x
        s += encoder(nb)
        s += '\n'
    # print(s)
    return s

    



def writefile(s):
    with open(file_path, "w") as f:
        f.write(s)
    # print("wrote file to ", file_path)



def readfile():
    s = "Reading file from " + file_path
    print(s)
    ret = []
    with open(file_path, "r") as f:
        ls = f.readlines()
        for l in ls:
            r = decoder(l)
            ret += [r]
    return ret
        

# dec = decoder("085-345-031")
# print(dec)