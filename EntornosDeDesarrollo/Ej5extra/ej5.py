import json 

datos = [{
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ciudad Ejemplo",
    "intereses": ["programación", "viajes", "lectura"]
},
{
    "nombre": "Juana",
    "edad": 33,
    "ciudad": "Ciudad Ejemplo",
    "intereses": ["programación", "viajes", "lectura"]
}]

with open("exportado.json", "w") as file:
    json.dump(datos, file, indent=4)