compañeros = {
    "Franco":{ "edad": 18 , "curso": "7mo 4ta GB"},
    "Carlos":{ "edad": 19 , "curso": "7mo 4ta GA"},
    "Gaspar":{ "edad": 18 , "curso": "7mo 4ta GA"},
    "Maximiliano": { "edad": 15 , "curso": "7mo 4ta GA"},
    "Francisco": { "edad": 19 , "curso": "7mo 2da GB"},
    "Gonzalono": { "edad": 18 , "curso": "7mo 4ta GA"},
    "Cristofer": { "edad": 18 , "curso": "7mo 4ta GB"},
    "Ivan": { "edad": 18 , "curso": "7mo 4ta GB"},
    "Giuliano":{ "edad": 21 , "curso": "7mo 4ta GB"},
    "Juan Manuel":{ "edad": 18 , "curso": "7mo 4ta GB"}
}
edades = [compañero["edad"] for compañero in compañeros.values()]

#Promedio edad
promedio = sum(edades) / len(edades)
print(promedio)

