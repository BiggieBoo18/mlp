#coding: UTF-8

def function(x1, x2, x3, x4, x5):
    ret = (x1-x3)**2 + (x1+x2)**2 + (x2-1)**2 + (2*x4+x1-x2)**2 + (x5+x1-x3)**2
    return (ret)

def d_function1(x1, x2, x3, x4, x5):
    ret = 2 * (4*x1-2*x3+2*x4+x5)
    return (ret)

def d_function2(x1, x2, x3, x4, x5):
    ret = 2 * (3*x2-2*x4-1)
    return (ret)

def d_function3(x1, x2, x3, x4, x5):
    ret = 2 * (-2*x1+2*x3-x5)
    return (ret)

def d_function4(x1, x2, x3, x4, x5):
    ret = 4 * (2*x4+x1-x2)
    return (ret)

def d_function5(x1, x2, x3, x4, x5):
    ret = 2 * (x5+x1-x3)
    return (ret)

def main():
    epoch = 1000
    e     = 0.01
    x1    = 0
    x2    = 0
    x3    = 0
    x4    = 0
    x5    = 0
    g_old = 0
    for i in range(epoch):
        print "epoch{0}".format(i)
        g1 = d_function1(x1,x2,x3,x4,x5)      # 勾配計算1
        g2 = d_function2(x1,x2,x3,x4,x5)      # 勾配計算2
        g3 = d_function3(x1,x2,x3,x4,x5)      # 勾配計算3
        g4 = d_function4(x1,x2,x3,x4,x5)      # 勾配計算4
        g5 = d_function5(x1,x2,x3,x4,x5)      # 勾配計算5
        g  = g1+g2+g3+g4+g5
        if (g<=(g_old+e) and g>=(g_old-e)):   # 学習率倍の範囲なら終了
            print "g1,g2,g3,g4,g5=", g1,g2,g3,g4,g5
            print "x1,x2,x3,x4,x5=", x1,x2,x3,x4,x5
            print "function(x1,x2,x3,x4,x5)=", function(x1,x2,x3,x4,x5)

        x1 = x1 - e*g1                        # x1更新
        x2 = x2 - e*g2                        # x2更新
        x3 = x3 - e*g3                        # x3更新
        x4 = x4 - e*g4                        # x4更新
        x5 = x5 - e*g5                        # x5更新
        g_old = g


if __name__ == "__main__":
    main()
