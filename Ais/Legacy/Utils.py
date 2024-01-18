
def condense(listofstr:list) -> list:
    ll = []
    for l in listofstr:
        for s in l:
            ll += [int(s)]
    return ll

# * encoder
def no_list_to_str(l:list) -> str:
    s = ""
    assert len(l) == 10
    for i in range(len(l)):
        x = l[i]
        s = s + str(x)
        if i == 2 or i == 2 + 3:
            s += "-"
    # return s.join(l)
    return s