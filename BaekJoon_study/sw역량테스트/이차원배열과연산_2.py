'''A = [[2, 1, 1, 2, 0, 0],
[1, 1, 2, 1, 3, 1],
[3, 3, 0, 0, 0, 0]]
def sort_r(a):
    remove_set = {0}
    a =[i for i in a if i not in remove_set]
    num_tmp = list(set(a))
    bag = []
    for i in range(len(num_tmp)):
        bag.append((num_tmp[i], a.count(num_tmp[i])))
    bag = sorted(bag, key=lambda x: (x[1], x[0]))
    sorted_a = []
    for i in range(len(bag)):
        sorted_a.append(bag[i][0])
        sorted_a.append(bag[i][1])
    # for i in range(len(bag)):
    #     sorted_a.append(bag[i][1])
    return sorted_a


if len(A) >= len(A[0]):
    tmp_A = []
    for i in range(len(A)):
        tmp_A.append(sort_r(A[i]))
    print('tmp_A', tmp_A)
    tmp_len = [len(i) for i in tmp_A]
    print('tmp_len', tmp_len)
    A = [[0] * (max(tmp_len)) for _ in range(len(tmp_A))]
    print('A', A)
    for i in range(len(A)):
        for j in range(len(tmp_A[i])):
            A[i][j] = tmp_A[i][j]
    print('A', A)
else:
    tmp_A = []
    for i in range(len(A[0])):
        print([j[i] for j in A])
        tmp_A.append(sort_r([j[i] for j in A]))
    print('tmp_A', tmp_A)
    tmp_len = [len(i) for i in tmp_A]
    print('tmp_len', tmp_len)
    A = [[0] * (len(tmp_A)) for _ in range(max(tmp_len))]
    print('A', A)
    for i in range(len(A[0])):
        for j in range(len(tmp_A[i])):
            A[j][i] = tmp_A[i][j]
    print('A', A)

'''


a = [1,2,3,4,5,6,7,8,9]
for i in range(20):

        try:#에러로부터 보호되는 코드부분
            if a[10] == 3:
                print(a[i])
            else:
                print('small',a[i])
            a.append(3)
            a.append(3)
            print(a)
        except: #에러가 발생하면 실행되는 부분
            pass