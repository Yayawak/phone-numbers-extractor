from gen_random_number import gen_unique_random_numbers, get_one_random_number, sort_numbers, pretty_print

def find(all_numbers_in_system, pattern_single_list):
    # * pattern_single_list is like [0, x, x, y, y, y, z, z, z, z] this is dont want 0
    # * pattern_single_list is like [x, x, y, y, y, z, z, z, z]
    ret = []
    for numbs in all_numbers_in_system:
        this_nb_pass = True
        for j in range(len(numbs)):
            digit = numbs[j]
            test = pattern_single_list[j]

            # any_digit = False
            if test == -1:
                # any_digit = True
                continue

            if digit != test:
                this_nb_pass = False
                break
        if this_nb_pass:
            ret += [numbs]
            
            # if 
            # if test == -1:
            #     ret += [numbs]
            #     break
            # elif (digit == test):
            #     continue
    return ret


def rec(nb:list, pivot_index):
    ...
    print("----------")
    global all_numbers_in_system
    founded_result = find(all_numbers_in_system, 
        # []
        nb
    )
    # print(founded_result)
    # pretty_print(founded_result)
    # print()
    # * not found on web
    if founded_result == []:
        # * overflow bottom
        if nb[pivot_index] < 9:
            nb[pivot_index] = nb[pivot_index] + 1
            # pretty_print(founded_result)
            print("go down -> ", nb)
            rec(nb, pivot_index)
    # * found on web
    else:
        # pivot_index += 1
        
            # if pivot_index > 0
            # if nb[pivot_index] == -1:
        print("pivot_index = ", pivot_index)
        if nb[pivot_index] == 9:
            pivot_index =+ 1
            print("\tgo right -> ", nb)
            nb[pivot_index] = 0
            rec(nb, pivot_index)
        # * 0 to 8
        else: 
            if pivot_index < 6 - 1:
                pivot_index += 1
                # rec(nb, pivot_index)

            nb[pivot_index] += 1
            print("\tgo down -> ", nb)

            rec(nb, pivot_index)
        # if nb[pivot_index + 1] == -1:
        #     # if pivot_index > 0
        #     # if nb[pivot_index] == -1:
        #     print("pivot_index = ", pivot_index)
        #     if nb[pivot_index] == 9:
        #         pivot_index =+ 1
        #         print("\tgo right -> ", nb)
        #         nb[pivot_index] = 0
        #         rec(nb, pivot_index)
        #     # * 0 to 8
        #     else: 
        #         pivot_index += 1
        #         # nb[pivot_index] += 1
        #         nb[pivot_index] += 1
        #         print("\tgo down -> ", nb)
        #         rec(nb, pivot_index)


            # nb[pivot_index + 1] = 0
            # rec()


        # if pivot_index < 9:
        # if pivot_index < 6 - 1:
        # if pivot_index < 6 - 1:
        #     pivot_index += 1
        #     # nb[pivot_index] = 0
        #     nb[pivot_index] += 1
        #     print("\tgo right -> ", nb)
        #     rec(nb, pivot_index)
        # # * overflow right
        # else:
        # rec(nb)
            # print("founded all digits = ", nb)
            ...

    # pretty_print(founded_result)
    # if 


if __name__ == '__main__':
    ...

    all_numbers_in_system = sort_numbers(gen_unique_random_numbers(1000))
    # pretty_print(all_numbers_in_system)
    r = find(all_numbers_in_system,
        [8, 0, -1, -1, -1, -1]
        # [8, 0, -1, -1, 0, -1]
    )
    # pretty_print(r)
    # pretty_print(all_numbers_in_system)

    # init_nb = [-1, -1, -1, -1, -1]
    init_nb = [0, -1, -1, -1, -1, -1]
    rec(init_nb, 0)
    print(r)
