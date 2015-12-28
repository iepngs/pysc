#encoding:utf8
from functools import reduce

def multi(n):
    num = 1
    if n > 1:
        for i in range(2, n+1):
            num *= i
    return num


def multiMulti(num):
    if not num:
        print(0)
        exit()
    resultNum = 1
    if num > 1:
        resultNum = 0
        for smnum in range(1,num+1):
            flag = 0
            if smnum > 7:
                break
            for i in range(1,smnum):
                if not smnum%i:
                    flag +=1
            if flag == 1:
                resultNum += multi(smnum)
                if resultNum > 9:
                    resultNum = str(resultNum)
                    resultNum = int(resultNum[-2:])
    print('Result: ',resultNum)


multiMulti(10000)
