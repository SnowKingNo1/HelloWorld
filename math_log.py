import math
def CalEnt(pi):
    Ent = -pi * math.log(pi, 2)
    return Ent

if __name__ == '__main__':
    # print((CalEnt(2/14)+CalEnt(2/9)+CalEnt(3/9)*2)*(9/15)+(CalEnt(1/6)*2+CalEnt(4/6))*(6/15))
    # print((1/3)*(1.5219281+1.3709505+1.3709505))
    # print((CalEnt(2/6)*2+2*CalEnt(1/6))*(6/15)+((CalEnt(2/5)+CalEnt(1/5)*3)*(5/15)))
    # print(CalEnt(1/15)+CalEnt(14/15)+CalEnt(1))
    # a = CalEnt(3/14) + CalEnt(2/14) + CalEnt(7/14) + CalEnt(2/14)
    # b = CalEnt(1) + CalEnt(2/2) + CalEnt(1) + CalEnt(1)
    # print(1.829473-a*14/15-b*1/15)
    # print(0.276406/0.353359)
    print(str(5e-7)[-1])