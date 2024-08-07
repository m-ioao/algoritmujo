import numpy as np
from numpy.linalg import inv


#%% version matricielle
# Renvoie un triplet (pgcd, u, v) où u, v coeff pour relation de bézout

def euclide_etendu_matriciel(a,b):
    M = np.identity(2)
    while b != 0:
        q = a//b
        M = np.dot(M, np.array([[q, 1],
                                [1, 0]]))
        a, b = b, a%b
    M = inv(M)
    return (a, round(M[0][0]), round(M[0][1]))



#%% version standard
def euclide_etendu(a,b):
    u_i, v_i = 1, 0
    u_j, v_j = 0, 1
    
    while b != 1:
        q, r = a//b , a%b
        
        u_k = u_i - u_j*q
        v_k = v_i - v_j*q
        
        a, b = b, r
        u_i, v_i = u_j, v_j
        u_j, v_j = u_k, v_k

    return u_k, v_k

