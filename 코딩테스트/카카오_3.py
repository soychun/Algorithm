b = [12,13,13]
avg = int(round(sum(b)/len(b)))
tmp = [avg for _ in range(len(b))]
sum_tmp = [abs(b[i]-tmp[i]) for i in range(len(b))]
sum(sum_tmp)