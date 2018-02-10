#a = [‘hello’, 1, ‘my’, 2, ‘dear’, 3, ‘friend’] -> b = [‘hello’, ‘my’,  ‘dear’, ‘friend’]

#a = [‘hello’, 1, ‘my’, 2, ‘dear’, 3, ‘friend’] -> b = [1,2,3]

#есть список  a = [1,2,3,4,5,6] из него сделать список b -> b = [1, 2, 3, [1, 2, 3, 4, 5, 6], 5, 6]
a = [1,2,3,4,5,6]
c = [1,2,3,4,5,6]
b = a.insert(3,c)
print(a)

#a = [1,2,3,4,5,6] -> b = ‘1,2,3,4,5,6’
a = [1,2,3,4,5,6]
a= map(str,a)
b = ','.join(a)
print(b)

#a = [‘ba’, ‘e’, ‘wqrt’, ‘frt’, ‘povrt’] -> b = [‘e’, ‘ba’, ‘frt’, ‘wqrt’, ‘povrt’]
a = ['ba', 'e', 'wqrt', 'frt', 'povrt']
def sorti(i):
    return len(i)
a.sort(key=sorti)
print(a)

#a = [‘ba’, ‘e’, ‘wqrt’, ‘frt’, ‘povrt’] -> b = [‘ba’, ‘e’, ‘frt’, ‘povrt’, ‘wqrt’]
a1 = ['ba', 'e', 'wqrt', 'frt', 'povrt']
a1 = sorted(a1)
print(a1)