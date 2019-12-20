print("******请选择您输入的关系R形式：1、集合；2、关系矩阵******")
choose=input()
if(choose=='1'):
    print("*****请输入R中元素的个数：******")
    n = int(input())        
    r = [[0]*2]*n        

    print("******输入格式说明：同组元素用空格分隔，不同行则用回车换行******")

    for i in range(n):
        r[i] = input().split(" ")  
    print("******您输入的关系R为：******",r)         
                
    r_dict = {}
    r_index = 0
    for element_tuple in r:
        for element in element_tuple:
            if element in r_dict:
                continue
            r_dict[element] = r_index
            r_index += 1

    r_matrix = [[0 for i in range(len(r_dict))]
                       for i in range(len(r_dict))]

    for (x, y) in r:
        x_index = r_dict[x]
        y_index = r_dict[y]
        r_matrix[x_index][y_index] = 1

    print("******关系R的关系矩阵为:******",r_matrix)

elif(choose=='2'):
    print("******请输入关系矩阵的行列数：******")
    n = int(input())        
    r = [[0]*n]*n        
    print("******输入格式说明：同行元素用空格分隔，不同行则用回车换行******")
    for i in range(n):
        r[i]= input().split(" ")
    print("******您输入的关系矩阵为：******",r)
    r_matrix=r
    

n=len(r_matrix)-1
r1=[[0]*n]*n 
for i in range(n):
    if(int(r_matrix[i][i])!=1):
        print("******此关系不满足自反性，不是等价关系******")
        flag=1
    break


for i in range(n):
    for j in range(n):
        if (r_matrix[i][j]!=r_matrix[j][i]):
            print("******此关系不满足对称性，不是等价关系******")
            flag=1
        break

for i in range(n):
    for j in range(n):
        temp=0
        for t in range(n):
            temp=temp+int(r_matrix[i][t])*int(r_matrix[t][j])
            if (temp>0):
                temp=1
        r1[i][j]=temp
for i in range(n):
    for j in range(n):
        if(r1[i][j]>int(r_matrix[i][j])):
            print("******此关系不满足传递性，不是等价关系******")
            flag=1
            break

if(flag==0):
    print("******此关系是等价关系******")