#按任务顺序排时间
import copy
import time


def get_least_arr(arr):
    for ii in range(len(arr)):
        if len(arr[-1]) == 0:
            arr.pop(len(arr) - 1)
    return arr


def check_valid(state, all_max_num, all_cost):
    for i, elem in enumerate(state):
        score = sum([all_cost[label] for label in elem])
        if score > all_max_num[i]:
            return False
    return True


def generate_whole_state(start_state, all_day, all_gap_seq):
    res = [[] for i in range(all_day)]
    for i, elem in enumerate(start_state):
        for e in elem:
            for gap in all_gap_seq[e]:
                if i + gap >= all_day:
                    return None
                res[i + gap].append(e)
    return res


# n:安排完前n个任务
# all_max_num:每天剩余时间
# all_cost:每个任务时间
# all_gap_seq:每个任务周期所有时间点
# start_state:现在已有任务安排
# start_i:开始处理第几个任务
# start_j:从天数位置j开始
def get_valid_state(n=0, start_state=[], start_i=1, start_j=0, all_max_num=[], all_cost=[], all_gap_seq=[], keep_num=1):
    res = []
    def insert_i_part(i, current_max_pos, arr):
        if len(res) >= keep_num:
            return
        if i == n:
            least_arr = get_least_arr(arr)
            whole_state = generate_whole_state(least_arr, len(all_max_num), all_gap_seq)
            if whole_state:
                valid = check_valid(whole_state, all_max_num, all_cost)
                if valid:
                    res.append(least_arr)
        else:
            for j in range(current_max_pos, min(current_max_pos + max(int(n / 2), 3), len(start_state))):
                arr_copy = copy.deepcopy(arr)
                arr_copy[j].append(i)
                insert_i_part(i + 1, j, arr_copy)

    insert_i_part(start_i, start_j, start_state.copy())
    return res


def split_states(all_max_num=[], all_cost=[], all_gap_seq=[], split_base=4):
    expand_num = 3
    n = len(all_cost)
    part_num = int(n / split_base)
    split_index_seq = [(i * split_base, i * split_base + split_base) for i in range(part_num)]
    if n % split_base != 0: split_index_seq.append((part_num * split_base, len(all_cost)))

    start_state = [[] for i in range(split_base * expand_num)]
    start_state[0].append(0)

    start_i = 1
    start_j = 0
    for start_end in split_index_seq:
        start, end = start_end[0], start_end[1]
        ss = get_valid_state(n=end, start_state=start_state, start_i=start_i, start_j=start_j, all_max_num=all_max_num, all_cost=all_cost, all_gap_seq=all_gap_seq, keep_num=1)
        #暂时取第一个，此处可择优？
        ss = ss[0]
        start_i = end
        start_j = len(ss) - 1
        start_state = ss + [[] for i in range(end * expand_num - start * expand_num)]
    whole_state = generate_whole_state(start_state, len(all_max_num), all_gap_seq)
    return start_state, whole_state



def get_plan(n=None, all_cost=None, all_max=None, all_gap_seq=None):
    if n is None:
        print("Parameter n not set! Use default n = 10.")
        n = 10

    if all_cost is None:
        print("Parameter all_cost not set! Use default all_cost = [1,...,1], which means it cost 1 time for every task.")
        all_cost = [1 for i in range(n)]
    elif isinstance(all_cost, int) or isinstance(all_cost, float):
        print("Parameter all_cost is set for one task! Extend it to all days.")
        all_cost = [all_cost for i in range(n)]

    #todo:默认一个列表
    if all_gap_seq is None:
        print("Parameter all_gap_seq not set! Use default all_gap_seq = [[0, 0, 0, 1, 2, 4, 7, 15],...,[0, 0, 0, 1, 2, 4, 7, 15]],"
              " which means the gap sequence for every task is [0, 0, 0, 1, 2, 4, 7, 15]. Note that this sequence is based "
              "on The Ebbinghaus Forgetting Curve.")
        all_gap_seq = [[0, 0, 0, 1, 2, 4, 7, 15] for i in range(n)]

    if all_max is None:
        print("Parameter all_max_num not set! Use default all_max_num = [5,....,5], which means the max time for every day "
              "is 5.")
        all_max = [5 for i in range(365)]
    elif isinstance(all_max, int) or isinstance(all_max, float):
        print("Parameter all_max_num is set for one day! Extend it to all days.")
        all_max = [all_max for i in range(365)]

    start_state, whole_state = split_states(all_max_num=all_max, all_cost=all_cost, all_gap_seq=all_gap_seq,
                                            split_base=4)
    whole_state = get_least_arr(whole_state)
    for i, elem in enumerate(whole_state):
        print("第" + str(i+1) + "天  ", elem)
    return whole_state

# n = 100
# all_cost = [1 for i in range(n)]
# all_gap_seq = [[0, 0, 0, 1, 2, 4, 7, 15] for i in range(n)]
# array = [[4, 4, 3, 4, 4, 6, 8] for i in range(52)]
# all_max_num = [num for sublist in array for num in sublist]
# start_state, whole_state = split_states(all_max_num=all_max_num, all_cost=all_cost, all_gap_seq=all_gap_seq, split_base=4)
# #print(start_state)
# whole_state = get_least_arr(whole_state)
# for i, elem in enumerate(whole_state):
#     print("第" + str(i+1) + "天  ", elem)
#res = get_plan(n=10, all_cost=1, all_max=5)
# res = get_plan()
# print(res)












