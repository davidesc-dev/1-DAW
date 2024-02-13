beatles = []
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

print("Añade a Stu Sutcliffe, y Pete Best")
for i in range (2):
    añadir = input("Añadir a: ")
    beatles.append(añadir)
print("Paso 3:", beatles)

del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

beatles.insert(0,"Ringo Star")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))