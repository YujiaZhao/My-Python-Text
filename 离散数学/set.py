import itertools

def getArrayAnd(array1,array2):           #求并集
    result1=set(array1)|set(array2)       #符号方法
    result2=set(array1).union(array2)     #函数方法
    print("A∪B=",result1)
    #print("A∪B=",result2)

def getArrayPlus(array1,array2):             #求交集
    result1=set(array1)&set(array2)          #符号方法
    result2=set(array1).intersection(array2) #函数方法
    print("A∩B=",result1)
    #print("A∩B=",result2)

def getArraySub(array1,array2):              #求差集
    result=set(array1).difference(array2)
    print("A-B=",result)


def getArraySubSet(array):                   #求幂集

    result = [[]]
    for i in range(len(array)):
        for j in range(len(result)): 
            result.append(result[j]+[array[i]]) #现有每个子集中添加新元素，作为新子集加入结果集中
    print("P(A)=",result)

def getArrayDkr(array1,array2):              #求笛卡儿积
    print("AB的笛卡儿积为：")
    for Dkr in itertools.product(array1,array2):
        print(Dkr)

 
# 测试
a=[1,2,3,4]
b=[1,2,5]

getArrayAnd(a,b)
getArrayPlus(a,b)
getArraySub(a,b)
getArraySubSet(a)
getArrayDkr(a,b)
