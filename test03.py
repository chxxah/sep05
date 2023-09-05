lol = [[1,2,3],[4,5],[6,7,8,9]]
print(lol[0]) # [1, 2, 3]
print(lol[2]) # [6, 7, 8, 9]
print(lol[2][2]) # 8

print(lol[0]) # [1, 2, 3]
print(lol[2][1]) # 7
for sub in lol:
    for item in sub:
        print(item, end=' ')
    print()
# 1 2 3
# 4 5
# 6 7 8 9

def exam(num1, num2=2):
    print('a=', num1, 'b=', num2)
exam(20)
# a= 20 b= 2

class MyPass:
    def byPass(self): # 기본적으로 자기 자신이라는 뜻으로 self를 붙여줌
        print("pass")

myPass = MyPass()
myPass.byPass()  # pass

class good:
    li = ["seoul","kyeonggi","inchon","daejeon","daegu","pusan"]

g = good()
str01 = ''
for i in g.li:
    str01 = str01 + i[0]

print(str01) # skiddp