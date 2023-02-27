s1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
s2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
k = "B"

# s1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
# s2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
# k = "G"

g = dict()
for i in range(len(s1)):
    g[s1[i]] =g.get(s1[i],[]) +[s2[i]]
print(g)