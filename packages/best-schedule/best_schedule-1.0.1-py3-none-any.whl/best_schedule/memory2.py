import copy

def get_least_arr(arr):
    for ii in range(len(arr)):
        if len(arr[-1]) == 0:
            arr.pop(len(arr) - 1)
    return arr


# def check_valid(state, one_max_num=3, duplicate_weight=0.5):
#     for elem in state:
#         score = len(set(elem)) + (len(elem) - len(set(elem))) * duplicate_weight
#         if score > one_max_num:
#             return False
#     return True


def check_valid(state, one_max_num=3, duplicate_weight=0.5, tolerance=0, tolerance_times=0):
    invalid_times = 0
    for elem in state:
        score = len(set(elem)) + (len(elem) - len(set(elem))) * duplicate_weight
        if score > one_max_num:
            if score < one_max_num + tolerance:
                invalid_times += 1
                if invalid_times > tolerance_times:
                    return False
            else:
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


#n:平分成几份工作量
#one_max_num:一天中最大工作量限制
def get_valid_state(n=5, one_max_num=3, duplicate_weight=0.5, keep_num=10):
    #此处暂定*2的初始长度，实际上需要探究一下
    start_state_max_num = n * 2
    start_state = [[] for i in range(start_state_max_num)]
    start_state[0] = [1]
    res = []

    def insert_i_part(i, current_max_pos, arr):
        if len(res) >= keep_num:
            return
        if i == n:
            least_arr = get_least_arr(arr)
            whole_state = generate_whole_state(least_arr)
            valid = check_valid(whole_state, one_max_num, duplicate_weight)
            if valid:
                res.append(least_arr)
        else:
            for j in range(current_max_pos, min(current_max_pos + max(int(n / 2), 3), start_state_max_num)):
                arr_copy = copy.deepcopy(arr)
                arr_copy[j].append(i+1)
                if len(arr_copy[j]) > one_max_num:
                    continue
                insert_i_part(i+1, j, arr_copy)

    insert_i_part(1, 0, start_state.copy())
    return res


res = get_valid_state(n=5, one_max_num=5, duplicate_weight=1, keep_num=1000)
min_len = 10000
for elem in res:
    if len(elem) < min_len:
        min_len = len(elem)

        print(elem)
        print(generate_whole_state(elem))
        print("\n")