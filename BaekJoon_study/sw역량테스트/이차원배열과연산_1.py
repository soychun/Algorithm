# 예외처리 틀림


# a = [(1,30),(2,20),(3,70),(3,40)]
# b = sorted(a,key=lambda x:(x[0],x[1]))
# print(b)


a = [3, 1, 1, 2]
# num_tmp = list(set(a))
# print(a.count(num_tmp[0]))
# bag = []
# for i in range(len(num_tmp)):
#     bag.append((num_tmp[i],a.count(num_tmp[i])))
# bag = sorted(bag,key=lambda x:(x[1],x[0]))
# print(bag)
# print(bag[0][0])
# a_again = []
# for i in range(len(bag)):
#     a_again.append(bag[i][0])
#     a_again.append(bag[i][1])
# print(a_again)

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
    return sorted_a
r,c,k = map(int,input().split())
c = c-1
r = r-1
A = []
for i in range(3):
    A.append(list(map(int,input().split())))
time_stemp = 0

while True:
    if time_stemp > 100: time_stemp = -1; print(time_stemp); break
    if 0<=r<len(A) and 0<=c<len(A[0]) and A[r][c]==k:
        print(time_stemp)
        break

    else:
        if len(A)>=len(A[0]):
            tmp_A = []
            for i in range(len(A)):
                tmp_A.append(sort_r(A[i]))
            tmp_len = [len(i) for i in tmp_A]
            A = [[0] * (max(tmp_len)) for _ in range(len(tmp_A))]
            for i in range(len(A)):

                for j in range(len(tmp_A[i])):
                    A[i][j] = tmp_A[i][j]

        else:
            tmp_A = []
            for i in range(len(A[0])):
                tmp_A.append(sort_r([j[i] for j in A]))
            tmp_len = [len(i) for i in tmp_A]
            A = [[0]*(len(tmp_A)) for _ in range(max(tmp_len))]
            for i in range(len(A[0])):
                for j in range(len(tmp_A[i])):
                    A[j][i] = tmp_A[i][j]


        time_stemp +=1
