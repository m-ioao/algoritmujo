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
    u_i, v_i = 1, 0                         # rang i correspondra à "n-2"
    u_j, v_j = 0, 1                         # rang j correspondra à "n-1"
    
    while b != 0:                           # arrêt pour reste nul
        quotient, reste = a//b , a%b
        
        u_k = u_i - u_j * quotient          # rang k correspondra à "n"
        v_k = v_i - v_j * quotient
        
        a, b = b, reste
        u_i, v_i = u_j, v_j
        u_j, v_j = u_k, v_k
                                            # on doit renvoyer le rang i, vu les réaffectations
    return (u_i, v_i), a                    # renvoie le couple pour bézout et le pgcd


print(euclide_etendu(17,60))
print(euclide_etendu(24,18))


def euclide_simple(a,b):
    if b == 0:
        return a
    else:
        return euclide_simple(b, a%b)



# euclide étendu récursif

def euclet_rec(a,b):
    if b == 0:
        return (a, 1, 0)
    else:
        pgcd, u, v = euclet_rec(b, a%b)
        u, v = v, u - (a//b) * v
        return (pgcd, u, v)
