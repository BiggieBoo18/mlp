#coding: UTF-8

def function(x):
    ret = -2*x**2+5*x+2
    return (ret)

def d_function(x):
    ret = -4*x+5
    return (ret)

def main():
    epoch = 1000
    e     = 0.001
    x     = 0
    g_old = 0
    for i in range(epoch):
        print "epoch{0}".format(i)
        g = d_function(x)                     # 勾配計算
        if (g<=(g_old+e) and g>=(g_old-e)):   # 学習率倍の範囲なら終了
            print "g=", g
            print "x=", x
            print "function(x)=", function(x)
            break
        x = x + e*g                           # x更新
        print "g=", g
        print "x=", x
        g_old = g


if __name__ == "__main__":
    main()
