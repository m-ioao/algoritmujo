import numpy as np                                                  # La librairie math aurait aussi marché

# FONCTION DONNANT UN ENCADREMENT DE LA MOYENNE ARITHMÉTICO-GÉOMÉTRIQUE D'UN NOMBRE

def moyenneAG(a, b, ecart):
    u_n, v_n = a, b                                                 # Initialisation de u_0 et v_0
    n = 0                                                           # Compteur de rang (facultatif)
    ampli = u_n - v_n                                               # Initialisation de l'amplitude
    
    while ampli > ecart:                                            # Condition sur l'amplitude pour finir la boucle
        n += 1                                                      # Incrément du rang
        u_n, v_n = (u_n + v_n)/2,  np.sqrt(u_n * v_n)               # Màj u_n et v_n pour ce rang en simultanée / ! \ important
        ampli = u_n - v_n                                           # Màj de l'amplitude
        
    return (f"Pour une amplitude inférieure ou égale à {ecart}, on obtient l'encadrement :"
            f"\n v_{n} = {v_n} <= M({a},{b}) <= {u_n} = u_{n}")

"""
/ ! \ Si l'on ne souhaite pas faire le calcul en simultané, il faudra introduire une variable pour 
stocker la valeur du rang précédent de u_n ou v_n selon celui que l'on calcule en premier. 
Puisque sinon, le calcul du second se ferait alors avec la valeur du rang n+1 de l'autre.
"""



print(moyenneAG(51, 34, .0001))
