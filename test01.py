# 2023-09-04 python 프로그래밍

# print("파이짐")
# 한글도됨 = 100
# print(한글도됨)

a = (100, 200, 400, "hi", False)
b = a + (500, 600)
print(b)
print(b[3:])

s = "가나다라마바사"
print(s[0])
print(s[0:2])
print(s[1:2])
print(s[5:6])
print(s[-1])
print(s[-1:-5])
print(s[-1:])
print(s[-3:-2])

a = "REMEMBER NOVEMBER"
b = a[:3] + a[12:15]
print(b) # REMEMB
c = "R AND %s" % "STR"
print(c) # R AND STR
print(b+c) #REMEMBR AND STR