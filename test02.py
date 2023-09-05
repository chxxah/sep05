# d = {"name": '한여름', 'age': 20, 'home': False}
# print(d) # {'name': '한여름', 'age': 20, 'home': False}
# print(type(d)) # <class 'dict'>
# print(d['name']) # 한여름
# print(d.keys()) # dict_keys(['name', 'age', 'home'])
# print(d.values()) #d ict_values(['한여름', 20, False])
# print(type(d.keys())) # <class 'dict_keys'>
# print(type(d.values())) # <class 'dict_values'>
# print('addr' in d.keys()) # False
# print('age' in d.keys()) # True
#
# # 추가
# d['addr'] = '서울'
# print(d) # {'name': '한여름', 'age': 20, 'home': False, 'addr': '서울'}
# # 수정
# d['addr'] = '인천'
# print(d) # {'name': '한여름', 'age': 20, 'home': False, 'addr': '인천'}
# # 삭제
# del(d['addr'])
# print(d) # {'name': '한여름', 'age': 20, 'home': False}

# 튜플 ()
# 딕셔너리 {}
# 리스트 []
arr = [10, 20, 30, 40, 50]
# print(type(arr)) # <class 'list'>
# print(arr) # [10, 20, 30, 40, 50]
# print(arr[0]) # 10
# print(arr[3:]) # [40, 50]
# print(arr[3:-1]) # [40]
#
# # 추가
# arr.append(60)
# print(arr) # [10, 20, 30, 40, 50, 60]
# arr.insert(1, 11) # 1 위치에 11을 넣어줌
# print(arr) # [10, 11, 20, 30, 40, 50, 60]
#
# temp = arr + [70, 80]
# print(temp) # [10, 11, 20, 30, 40, 50, 60, 70, 80]
# # arr.extend(11)
# # print(arr)
#
# print(arr)
#
# arr.remove(10)
# print(arr) # [11, 20, 30, 40, 50, 60]

# 역순정렬
arr.reverse()
print(arr) # [50, 40, 30, 20, 10]
# 순차정렬
arr.sort()
print(arr) # [10, 20, 30, 40, 50]

# set
s = {10, 20, 30, 40, 30}
print(s) # {40, 10, 20, 30} 중복값 허용하지 않음
s.add(50)
print(s) # {40, 10, 50, 20, 30} 순서가 없음
print(type(s)) # <class 'set'>
# s.update(60, 70, 80) # 오류
# 추가
s.update([60, 70, 80])
print(s) # {70, 40, 10, 80, 50, 20, 60, 30}
s.remove(70) # 70이라는 값 삭제
print(s) # {40, 10, 80, 50, 20, 60, 30}

# 뽑히는 순서가 없기 때문에 인덱스를 쓸 수가 없음
for i in s:
    print(i)
    # 40
    # 10
    # 80
    # 50
    # 20
    # 60
    # 30

# set에서 값이 있는지 확인
# 70이 s안에 있어?
print(70 in s) # False
print (30 in s) # True
print (11 not in s) # True

# 얕은 복사
s1 = s
s.remove(40)
print(s) # {10, 80, 50, 20, 60, 30}
print(s1) # {10, 80, 50, 20, 60, 30}

# 깊은 복사
s2 = s.copy() # 다른 객체로 만들어줌
s.add(100)
print(s) # {100, 10, 80, 50, 20, 60, 30}
print(s2) # {80, 50, 20, 10, 60, 30} 100의 값이 추가가 안됨

