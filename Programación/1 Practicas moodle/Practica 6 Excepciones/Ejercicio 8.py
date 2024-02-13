'''
Descripción del programa: 
Defina una excepción para impedir que un usuario digite más de 20 caracteres cómo
número de teléfono. Adicionalmente identifique flujos excepcionales en el programa y
capture las excepciones que pueden ocurrir.
agenda = {}
def process_numbers(person, number):
agenda[person] = number
def main():
n = int(input('Digite el número de contactos:'))
print('Agregando ' + str(n) + ' personas...')
for i in range(n):
nombre = input('Digite el nombre del contacto {}:'.format(i+1))
numero = int(input('Digite el número de contacto {}:'.format(i+1)))
process_numbers(nombre, numero)
print('Así va la agenda:' + str(agenda))
main()
Digite el número de contactos:3
Agregando 3 personas...
Digite el nombre del contacto 1:Arles
Digite el número de contacto 1:723847832
Digite el nombre del contacto 2:Pedro
Digite el número de contacto 2:238942894
Digite el nombre del contacto 3:Juan
Digite el número de contacto 3:23894289048290
Así va la agenda:{'Arles': 723847832, 'Pedro': 238942894, 'Juan': 23894289048290}



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
agenda = {}

###### Fuciones y Procedimientos (Subprogramas) ######
def process_numbers(person, number):
  agenda[person] = number
def main():
  n = int(input('Digite el número de contactos:'))
  print('Agregando ' + str(n) + ' personas...')
  for i in range(n):
    nombre = input('Digite el nombre del contacto {}:'.format(i+1))
    numero = int(input('Digite el número de contacto {}:'.format(i+1)))
    process_numbers(nombre, numero)
  print('Así va la agenda:' + str(agenda))

###### Programa Principal #############
if __name__ == "__main__":
  main()