#Tuplas inmutables

tupla1 = ("uno", "dos","tres")
print(tupla1)
print(type(tupla1))

tuplaVariosDatos=(12,True,23.6,"Nombre",12+3j)
print(tuplaVariosDatos)

tuplaConTuplas=(1,2,3,4,(1,2,3))
print(tuplaConTuplas)

print(tuplaConTuplas[3])
print(tuplaConTuplas[-2])
print(tuplaConTuplas[0:2])

a,b,c = tupla1
print(a)
print(b)
print(c)

# print("dos" in tupla1)

