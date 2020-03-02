#Los sets son muy similares a las listas, pero estas no permiten elementos repetidos

#las operaciones principales son la unión, intersección y diferencia

#unión
s = set([1, 2, 3])
t = set([3, 4, 5])
print(s.union(t))

#intersección
s = set([1, 2, 3])
t = set([3, 4, 5])
print(s.intersection(t))

#diferencia
s = set([1, 2, 3])
t = set([3, 4, 5])
print(s.difference(t)) #que elementos tiene s que no tiene t
print(t.difference(s)) #que elementos tiene t que no tiene s

1 in s #True
1 not in t #True
1 in t #False