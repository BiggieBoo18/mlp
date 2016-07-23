#coding:UTF-8

def main():
    x     = [[1,1],[2,2.5],[3,2.5],[4,4.5],[5,4.5]]
    a     = 0
    e     = 0.01
    epoch = 100
    error = 0

    print "一括更新学習法"
    for i in range(epoch):
        g = 0
        for j in x:
            g = g + (j[1]-a*j[0])*j[0]
            #print "g=",g
        a = a+e*g

        #print "a=",a
        
        error = 0
        for j in x:
            error = error + (j[1]-a*j[0])**2

    print "error=",error

    print "逐次更新学習法"
    for i in range(epoch):
        g = 0
        for j in x:
            g = g + (j[1]-a*j[0])*j[0]
            #print "g=",g
            a = a+e*g
            #print "a=",a
            
        error = 0
        for j in x:
            error = error + (j[1]-a*j[0])**2

    print "error=",error

if __name__ == "__main__":
    main()
