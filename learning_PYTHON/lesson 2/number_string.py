#數字運算
x = 3 + 6
print ("3 + 6 = ",x)
# 用兩個乘法符號代表A的B次方 A**B
x = 3**2
print ("3的2次方 = ",x)
# 用B小於1的次方數代表開根號
x = 2**0.5
print ("2的開根號 = ",x)
# 用一個斜線代表小數除法
x = 3/6
print ("3除以6的小數除法 = ",x)
# 用兩個斜線代表整數除法
x = 3//6
print ("3除以6的整數除法 = ",x)

#字串運算
s = 'Hello'
s1 = "World"
print( s, s1 )
print (s +s1)

s2 = """it
is 
a 
test 
string"""
print (s2)

s3 = "hello "*3 + "world"
print (s3)

#印出字串的開頭s[1]，但不包含結尾s[4]
print(s[1:4])
#可以只給開頭或只給結尾
print (s[:4])
print (s[1:])
