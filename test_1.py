def hitung_maksimal_kemahiran(m, Ai, Bi):
    """
        Menghitung tingkat kemahiran maksimal Juned
    """
    res = m
    enemy = sorted(zip(Ai, Bi)) 
    for ai, bi in enemy:
        if ai <= res:
            res += bi
    return res

# TEST CASE 1
n = 4
m = 2
Ai = [8, 9, 3, 2]
Bi = [5, 4, 1, 3]
# Expected output : 6
print(hitung_maksimal_kemahiran(m,Ai,Bi))

# TEST CASE 2
n = 5
m = 3
Ai = [8, 4, 5, 6, 7]
Bi = [9, 8, 7, 5, 6]
# Expected output : 3
print(hitung_maksimal_kemahiran(m,Ai,Bi))

# TEST CASE 3
n = 5
m = 9
Ai = [2, 3, 6, 7, 8]
Bi = [3, 4, 2, 2, 3]
# Expected output : 23
print(hitung_maksimal_kemahiran(m,Ai,Bi))