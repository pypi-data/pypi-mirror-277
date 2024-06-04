import copy

def get_least_arr(arr):
    for ii in range(len(arr)):
        if len(arr[-1]) == 0:
            arr.pop(len(arr) - 1)
    return arr


#n:平分成几份工作量
#one_max_num:一天中最大工作量限制
def get_all_start_state(n=5, one_max_num=3, keep_num=1000):
    #此处暂定*2的初始长度，实际上需要探究一下
    start_state_max_num = n * 2
    start_state = [[] for i in range(start_state_max_num)]
    start_state[0] = [1]
    res = []

    def insert_i_part(i, current_max_pos, arr):
        if i == n:
            least_arr = get_least_arr(arr)
            res.append(least_arr)
            # if len(res) > keep_num:
            #     return
        else:
            for j in range(current_max_pos, min(current_max_pos + max(int(n / 2), 3), start_state_max_num)):
                arr_copy = copy.deepcopy(arr)
                arr_copy[j].append(i+1)
                if len(arr_copy[j]) > one_max_num:
                    continue
                insert_i_part(i+1, j, arr_copy)

    insert_i_part(1, 0, start_state.copy())
    return res


def check_valid(state, one_max_num=3, duplicate_weight=0.5):
    for elem in state:
        score = len(set(elem)) + (len(elem) - len(set(elem))) * duplicate_weight
        if score > one_max_num:
            return False
    return True


def generate_whole_state(start_state):
    gap_seq = [0, 0, 0, 1, 2, 4, 7, 15]
    res = [[] for i in range(len(start_state) + gap_seq[-1])]
    for i, elem in enumerate(start_state):
        for e in elem:
            for gap in gap_seq:
                res[i + gap].append(e)
    return res


#duplicate_weight:重复的工作量 取值0-1，0代表重复的工作量不算，1代表重复的工作量按不重复来算
def get_greedy_result(part_num, one_max_num, duplicate_weight=0.5):
    if part_num < 0 or part_num > 10 or one_max_num > part_num or one_max_num < 3:
        return
    all_start_state = get_all_start_state(part_num, one_max_num)
    for start_state in all_start_state:
        whole_state = generate_whole_state(start_state)
        valid = check_valid(whole_state, one_max_num, duplicate_weight)
        if valid:
            print(start_state)
            print(whole_state)
            print("\n")


# res = get_all_start_state(6, 2)
# for arr in res:
#     print(arr)
# print(len(res))
get_greedy_result(10, 4)