n = 5
a = [1, 2, 3, 4, 5]
a = a + a
query = [[1, 3], [3, 0, 2], [2, 1], [3, 1, 4]]
prefix_sum = []
for i in range(1,n+1):
    prefix_sum.append(sum(a[0:i]))
    # print(prefix_sum[i-1])
for i in range(n+1,2*n+1):
    prefix_sum.append(sum(a[0:i]))
    # print(prefix_sum[i-1])
    
rota_r = 0
rota_l = 0
for q in query:
    if(q[0] == 1):
        rota_r += q[1]
    elif(q[0] == 2):
        rota_l += q[1] 
        # print(a)
    else:
        rota_r %= n
        rota_l %= n
        rota = rota_l-rota_r
        if(rota <=0):
            l = q[1] + n + rota
            r = q[2] + n + rota
        else:
            l = q[1] +  rota
            r = q[1] + rota
        print(prefix_sum[r]-prefix_sum[l-1])



# =============================================================================
# def left_rotate(a, i):
#     return a[i:n] + a[0:i]
# 
# 
# def right_rotate(a, j):
#     return a[n-j:n] + a[0:n-j]
# 
# 
# def print_array(a, k, l):
#     return sum(a[k:l])
# 
# 
# for q in query:
#     # print(q)
#     if(q[0] == 1):
#         a = right_rotate(a, q[1])
#         print(a)
#     elif(q[0] == 2):
#         a = left_rotate(a, q[1])
#         print(a)
#     else:
#         print(print_array(a, q[1], q[2]+1))
# =============================================================================
