import re
from Utils import no_list_to_str

def decoder(l:str):
    # l.split("-")
    ret = []
    listlist = l.split("-")
    for sublist in listlist:
        # for i in range(len(sublist))
        for x in sublist:
            x = int(x)
            ret += [x]
    return ret

def encoder(numb_lst) -> str:
    return no_list_to_str(numb_lst)