# stact sample
#
# word = input('input a word : ')
# word_list = list(word)
# for _ in range(len(word_list)):
#     print(word_list.pop())
#     print(word_list)

# queue
# a = [1,2,3,4,5]
# for _ in range(len(a)):
#     print(a.pop(0))
#     print(a)

# tuple
# t = (1,2,3)
# print(type(t))
# print(t[1])
# t[1] = 5  #할당이 안된다 (처음 선언한 것 그대로)
#
# t_1 = (3,) #튜플로 인식하려면 컴마가 반드시

# set
# 값을 순서없이 저장, 중복 불허하는 자료형
# set 객체 선언을 이용하여 객체 생성
# 자동정렬 역할
# a = set([1,2,3,4,3,5,4])
# print(a)
# add, update, remove,discard,clear
# 교집합, 합집합, 차집합 가능


# dict
# c_code = dict({'america':34,'korea':82})
# print(c_code)
# c_code["german"] = 49
# print(c_code)
# c_code["german"] = 50
# print(c_code)
# # keys,items,values
# for dict_items in c_code.items():
#     print(dict_items)
#     print(type(dict_items))  # : ('german', 50)  <class 'tuple'> 튜플 형해로 나온다.
#     # key 따로 value 따로는 수정 가능하지만 들어내는건 어려울 듯
# for k,v in c_code.items():
#     print('key : ',k,end=' ,')
#     print('value : ',v)
# # 언패킹 가능
# print('korea' in c_code.keys())


# rainbow csv라는 플러그인 설치함
# import csv
# command_data = []
# with open('command_data.csv','r',encoding='utf8') as csvfile:
#     spamreader = csv.reader(csvfile,delimiter=',',quotechar='"')
#     for row in spamreader:
#         command_data.append(row)
# print(command_data)


# collections
from collections import deque
deque_list = deque()
for i in range(5):
    deque_list.append(i)
deque_list.appendleft(10)
deque_list.extend([8,9,11])
print(deque_list)
deque_list.rotate(1)
print(deque_list)

# 주피터 노트북 시간재기 : %timeit 함수()