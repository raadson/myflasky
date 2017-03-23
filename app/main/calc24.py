#coding=utf-8
from __future__ import division
import itertools as it

fmtList = ["((%d%s%d)%s%d)%s%d","(%d%s%d)%s(%d%s%d)",
"(%d%s(%d%s%d))%s%d","%d%s((%d%s%d)%s%d)","%d%s(%d%s(%d%s%d))"]
opList = list(it.product(["+","-","*","/"],repeat=3))
def  ok(fmt,nums,ops,listsum):
    a,b,c,d =nums
    op1,op2,op3 =ops
    expr = fmt % (a,op1,b,op2,c,op3,d)
    try:
        res = eval(expr)
    except ZeroDivisionError:
        return
    if res==24.0:
        sum = expr+"=24"
        listsum.append(sum)
        # print (expr,"=24")



def  Calc24(numlist,listsum):
    [[ok(fmt,numlist,op,listsum) for fmt in fmtList] for op in opList]

