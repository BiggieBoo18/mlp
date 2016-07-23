#coding:UTF-8
import numpy as np

def sigmoid(u, gain):
    ret = 1.0/(1.0+np.exp(-gain*u))
    return (ret)

def main():
    x     = [[1,0,1,0],[1,1,0,0],[1,0,0,0],[1,1,3,1],[1,2,1,1],[1,1.5,2,1]]
    w     = [0,0,0]
    gain  = 2.0
    e     = 0.5
    epoch = 100
    error = 0

    for i in range(epoch):
        error = 0
        for j in x:
            u = j[0]*w[0]+j[1]*w[1]+j[2]*w[2]
            #print "u=",u
            z = sigmoid(u,gain)
            #print "z=",z

            dEdy = (z-j[3])*(1-z)*z*gain
            #print "dEdy=",dEdy
            for k in range(len(w)):
                #print w[k],j[k]
                w[k] = w[k] - e*dEdy*j[k]

            error = error + (j[3]-z)**2

        print "error=",error

if __name__ == "__main__":
    main()
