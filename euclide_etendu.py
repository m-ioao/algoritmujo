def euclideetendu(a,b):
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

print(euclideetendu(85,27))

