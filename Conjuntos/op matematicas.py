A = {1,2,3}
B = {3,4,5}

print(A | B) # Unión, tambien A.union(B)
print(A & B) # Interseción, tambien A.intersection(B)
print(A - B) # Diferencia, tambien A.difference(B)
print(A ^ B) # Diferencia simétrica, tambien A.symmetric_difference(B)

# COMPARACIONES

C = {1,2}
D = {1,2,3}

print(C.issubset(D)) # ¿C esta contenido en D? → True
print(C.issuperset(D)) # ¿C contiene a D? → False
print(C.isdisjoint(D)) # ¿C y D estan desconecatos? → False

E = {5,8}
F = {9,10}
print(E.isdisjoint(F)) # True




# Notas:
#     ^ : Alt + 94
