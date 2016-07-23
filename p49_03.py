#coding:utf-8

def function(x):
    ret = 2*x**2-3*x+5
    return (ret)

def d_function(x):
    ret = 4*x-3
    return (ret)

def main():
    e     = 1
    epoch = 5
    x     = 0

    print "---------"
    while (True):
        g = function(x)
        if   (function(x+e) < g):
            x = x + e
        elif (function(x-e) < g):
            x = x - e
        else:
            print "x=",x
            print "g=",g
            break
    print "--------"

    e      = 0.1
    epoch  = 1500
    x      = 0
    print "--------"
    for i in range(epoch):
        print "x=",x
        print "d_function(x)=",d_function(x)
        g = d_function(x)
        x = x - e*g

    print function(x)
    print "--------"

if __name__ == "__main__":
    main()
