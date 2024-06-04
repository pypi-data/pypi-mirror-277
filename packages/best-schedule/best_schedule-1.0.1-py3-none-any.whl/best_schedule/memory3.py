#定制
#编号  任务量  重复seq                     限制条件（之后再说）
#1     4      每周[0, 7, 14, 28...]       只能周一
#2     5      每月[0, 30, 60,...]         只能0-10号
#3     1      每天[0, 1, 2, 3...]
#4     2      每隔3天 [0, 3, 6, 9..]
#考虑最长的seq先排

#每天最大任务量（剩余时间） [8, 8, 6, 0, 5, 4, 8, 8...]

import copy

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


# def check_valid(state, one_max_num=3, duplicate_weight=0.5, tolerance=0, tolerance_times=0):
#     invalid_times = 0
#     for elem in state:
#         score = len(set(elem)) + (len(elem) - len(set(elem))) * duplicate_weight
#         if score > one_max_num:
#             if score < one_max_num + tolerance:
#                 invalid_times += 1
#                 if invalid_times > tolerance_times:
#                     return False
#             else:
#                 return False
#
#     return True


def generate_whole_state(start_state, all_day, all_gap_seq):
    res = [[] for i in range(all_day)]
    for i, elem in enumerate(start_state):
        for e in elem:
            for gap in all_gap_seq[e]:
                if i + gap >= all_day:
                    return None
                res[i + gap].append(e)
    return res


#n:平分成几份工作量
#one_max_num:一天中最大工作量限制
def get_valid_state(n=5, all_max_num=[], all_cost=[], all_gap_seq=[], keep_num=10):
    #此处暂定*2的初始长度，实际上需要探究一下
    start_state_max_num = n * 2
    start_state = [[] for i in range(start_state_max_num)]
    res = []

    def insert_i_part(i, arr):
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
            for j in range(start_state_max_num):
                arr_copy = copy.deepcopy(arr)
                arr_copy[j].append(i)
                insert_i_part(i+1, arr_copy)

    insert_i_part(0, start_state.copy())
    return res


# #res = get_valid_state(n=10, one_max_num=5, duplicate_weight=0.5, keep_num=1000)
all_gap_seq = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
               [0, 3, 6, 9, 12, 15, 18, 21],
               [0, 7, 14, 21, 28],
               [0, 0, 0, 1, 2, 4, 7, 15]]
all_max_num=[8, 8, 7, 8, 8, 8, 8, 8, 8, 7, 8, 8, 4, 5, 8, 8, 7, 2, 3, 4, 5, 8, 8, 7, 2, 3, 4, 5, 8, 8]
res = get_valid_state(n=4, all_max_num=all_max_num, all_cost=[1, 2, 3, 2], all_gap_seq=all_gap_seq, keep_num=100)
min_len = 10000
for elem in res:
    if len(elem) < min_len:
        min_len = len(elem)

        print(elem)
        print(generate_whole_state(elem, len(all_max_num), all_gap_seq))
        print("\n")