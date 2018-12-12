#!/usr/bin/env python3

'''tile.py:
可以通过输入的墙面长宽和瓷砖的长宽计算所有铺瓷砖的方法
从输出的方法中选择一种，可以画出其示意图
__author__ = "Zhujiajie"
__pkuid__  = "1800011794"
__email__  = "zhujiajie@pku.edu.cn"
'''
import turtle

def input_it():
    '''该函数用于输入并计算一些全局变量
    '''
    global m
    global n
    global a
    global b
    global lis_tile
    global num_tile
    global ans
    global d
    m=int(input('Please enter length of the wall:'))
    n=int(input('Please enter height of the wall:'))
    a=int(input('Please enter length of the tile:'))
    b=int(input('Please enter width of the tile:'))
    m,n=max([m,n]),min([m,n])
    a,b=max([a,b]),min([a,b])
    lis_tile=[]
    ans=[]
    num_tile=int(m*n/(a*b))
    d=2**num_tile

def bin_gen(x):
    '''该函数为辅助函数
    '''
    lis_gen=[]
    for i in range(num_tile):
        if x>=2**(num_tile-i-1):
            lis_gen.append(1)
            x-=2**(num_tile-i-1)
        else:
            lis_gen.append(0)
    return lis_gen    
def print_tile():
    '''该函数可以计算出所有的铺瓷砖方案，并且画出所选择的方案
    '''
    for p in range(d):
        lis_tile.append([])
        lis_space=[[x,y,False] for x in range(m) for y in range(n)]
        j=0
        k=0
        for z in bin_gen(p):
            if k>=n:
                break
            if j>=m:
                j,k=0,k+1
            if k>=n:
                break
            
            g=lis_space[j+m*k]
            while g[2]==True:
                j+=1
                if j>=m:
                    j=0
                    k+=1
                if k>=n:
                    break
                g=lis_space[j+m*k]

            if z==1:
                for i in range(j,m):
                    e=m
                    r=lis_space[i+m*k]
                    if r[2]==True:
                        e=i
                        break
                if j+a<=e and k+b<=n:
                    for x in range(j,j+a):
                        for y in range(k,k+b):
                            t=lis_space[x+m*y]
                            t[2]=True
                    lis_tile[p].append([x+m*y for x in range(j,j+a) for y in range(k,k+b)])
                    j+=a
                else:
                    break
            elif z==0:
                for i in range(j,m):
                    e=m
                    r=lis_space[i+m*k]
                    if r[2]==True:
                        e=i
                        break
                if j+b<=e and k+a<=n:
                    for x in range(j,j+b):
                        for y in range(k,k+a):
                            t=lis_space[x+m*y]
                            t[2]=True
                    lis_tile[p].append([x+m*y for x in range(j,j+b) for y in range(k,k+a)])
                    j+=b
                else:
                    break
    for solution in lis_tile:
        if len(solution)==num_tile:
            ans.append(solution)
    print('You have',len(ans),'plan to choose.')
    for i in ans:
        print(i)
    orde=int(input('Please enter ordinal number of the chosen plan:'))
    draw_plan=ans[orde-1]
    tu=turtle.Pen()
    for item in draw_plan:
        tu.pu()
        zn=item[0]
        xn=zn%m
        yn=zn//m
        tu.setpos(xn*30,yn*30)
        tu.setheading(0)
        tu.pd()
        if item[-1]-item[0]==m*(a-1)+b-1:
            tu.fd(b*30)
            tu.lt(90)
            tu.fd(a*30)
            tu.lt(90)
            tu.fd(b*30)
            tu.lt(90)
            tu.fd(a*30)
        else:
            tu.fd(a*30)
            tu.lt(90)
            tu.fd(b*30)
            tu.lt(90)
            tu.fd(a*30)
            tu.lt(90)
            tu.fd(b*30)
            
def main():
    input_it()
    print_tile()
if __name__ == '__main__':
    main()

    
