# 有序可變動列表 List
grades = [12, 50, 15, 70, 60]
print(grades)

print(grades[0])

grades[0] = 55

print(grades)

print(grades[1:4]) #將grades[1]到grade[4-1]的元素印出

grades[1:4] = [] #將grades[1]到grade[4-1]的元素刪除

print(grades)

grades = grades + [12, 33]

print(grades)

# 取得列表長度
length = len(grades)
print("列表長度 = ", length)

#巢狀列表
data=[[3,4,5], [6,7,8]]
print(data[0][1])

data[0][0:2] = [5, 5, 5]
print(data)

# 有序不可變動列表 Tuple
data = (3, 4, 5)
print(data[0:2])
# tuple的資料不可變動