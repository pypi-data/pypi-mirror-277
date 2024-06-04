#不考虑12345按时间顺序
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


def generate_whole_state(start_state, all_day, all_gap_seq):
    res = [[] for i in range(all_day)]
    for i, elem in enumerate(start_state):
        for e in elem:
            for gap in all_gap_seq[e]:
                if i + gap >= all_day:
                    return None
                res[i + gap].append(e)
    return res


# n:共几份工作量
# all_max_num:每天剩余时间
# all_cost:n个任务依次时间
# all_gap_seq:每个任务周期所有时间点
def get_valid_state(all_max_num=[], all_cost=[], all_gap_seq=[], keep_num=10):
    n = len(all_cost)
    start_state_max_num = n * 2
    start_state = [[] for i in range(start_state_max_num)]
    res = []

    def insert_i_part(i, arr):
        # if len(res) >= keep_num:
        #     return
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
                insert_i_part(i + 1, arr_copy)

    insert_i_part(0, start_state.copy())
    return res




# #res = get_valid_state(n=10, one_max_num=5, duplicate_weight=0.5, keep_num=1000)
n = 5
all_cost = [1 for i in range(n)]
all_gap_seq = [[0, 0, 0, 1, 2, 4, 7, 15] for i in range(n)]
all_max_num = [5 for i in range(365)]
res = get_valid_state(all_max_num=all_max_num, all_cost=all_cost, all_gap_seq=all_gap_seq, keep_num=100)
min_len = 10000
for elem in res:
    # if len(elem) < min_len:
    #     min_len = len(elem)

    print(elem)
    print(generate_whole_state(elem, len(all_max_num), all_gap_seq))
    print("\n")