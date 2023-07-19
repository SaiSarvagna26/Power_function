def power_function(A,B,C):
    if B==0:
        return 1%C
    else:
        temp=power_function(A,B-1,C)
        return (A*temp)%C
A=int(input())
B=int(input())
C=int(input())
result=power_function(A,B,C)
print(result)
