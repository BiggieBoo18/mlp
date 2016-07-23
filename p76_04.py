#coding: UTF-8

import numpy as np

def sigmoid(u, gain):
    ret = 1/(1+np.exp(-gain*u))

    return (ret)

def d_sigmoid(u, gain):
    ret = gain*sigmoid(u, gain)*(1-sigmoid(u, gain))
    
    return (ret)

def tanh(u):
    ret = np.tanh(u)
    
    return (ret)

def d_tanh(u):
    ret = 1.0 - (tanh(u))**2
    
    return (ret)

def main():
    x     = np.array(
            [[0,0,0],
             [1,0,1],
             [1,1,1],
             [1,1,0],
             [1,0,0],
             [0,0,1]]
            )     # 入力
    d     = np.array([0,0,1,0,1,1]) # 目標出力
    e     = 0.05  # 学習率
    epoch = 1000  # 学習数
    i_num = 3+1   # 入力層数
    h_num = 100+1 # 隠れ層数
    o_num = 1     # 出力層数
    gain  = 1     # ゲイン
    w1    = np.random.uniform(-1.0, 1.0, (h_num,i_num))
    #print w1
    w2    = np.random.uniform(-1.0, 1.0, (o_num,h_num))
    #print w2
    
    for k in range(epoch):
        print "epoch", k
        i  = np.random.randint(x.shape[0])
        X  = np.hstack([x[i],1.0])         # ランダムに入力値選択
        D  = np.array(d[i])                # 目標出力
        #print "input =", X
        #print "target=", D
        u1 = np.dot(w1, X)                 # ここから順伝播
        #print u1
        #z  = sigmoid(u1, gain)   # sigmoidの場合
        z  = tanh(u1)             # tanhの場合
        #print z
        u2 = np.dot(w2, z)
        y  = sigmoid(u2, gain)             # ここまで
        #print y
        delta_2 = y-D                      # ここから逆伝播
        #print np.dot(np.atleast_2d(delta_2), np.atleast_2d(z.T))
        #print delta_2
        #print d_sigmoid(u1, gain)
        #print np.dot(w2.T, delta_2)
        #delta_1 = d_sigmoid(u1, gain)*np.dot(w2.T, delta_2) # delta1(sigmoidの場合)
        delta_1 = d_tanh(u1)*np.dot(w2.T, delta_2)           # delta1(tanhの場合)
        #print delta_1
        X       = np.atleast_2d(X)
        delta_1 = np.atleast_2d(delta_1)
        #print delta_1.T
        #print X
        #print e*np.dot(delta_1.T, X)
        #print w1
        w1 -= e*np.dot(delta_1.T, X)
        #print w1
        delta_2 = np.atleast_2d(delta_2)
        z       = np.atleast_2d(z)
        #print delta_2.T
        #print z
        w2 -= e*np.dot(delta_2.T, z)        # ここまで
        #print w2

    for k in range(6):
    #for k in range(1):
        print "------------"
        print "epoch", k
        X  = np.hstack([x[k],1.0])    # 既知のデータ
        #X  = np.array([0, 1, 0, 1])  # 未知のデータ1
        #X   = np.array([0, 1, 1, 1]) # 未知のデータ2
        D  = np.array(d[k])           # 既知のデータに対する目標出力
        #D  = np.array[[1])           # 未知のデータ1に対する目標出力
        #D  = np.array([0])           # 未知のデータ2に対する目標出力
        print "input =", X
        print "target=", D
        u1 = np.dot(w1, X)
        #print u1
        #z  = sigmoid(u1, gain)
        z  = tanh(u1)
        #print z
        u2 = np.dot(w2, z)
        y  = sigmoid(u2, gain)
        delta_2 = y-D
        print "out   =",  y[0]
        print "loss  =", delta_2[0]
        print "------------"

if __name__ == "__main__":
    main()
