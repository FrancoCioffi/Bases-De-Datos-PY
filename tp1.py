empleados = []
def agregarEmpleado(nombre, edad, puesto):
    empleado = {"nombre": nombre, "edad": edad, "puesto": puesto}
    empleados.append(empleado)

def listarEmpleados():
    if empleados:
        for numEmpleado, empleado in enumerate(empleados, start=1):
            print(f"{numEmpleado}. Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Puesto: {empleado['puesto']}")

def actualizarEmpleado(indice, nuevaEdad, nuevoPuesto):
    if 0 <= indice < len(empleados):
        if nuevaEdad:
            empleados[indice]['edad'] = nuevaEdad
        if nuevoPuesto:
            empleados[indice]['puesto'] = nuevoPuesto
        print(f"Empleado {empleados[indice]['nombre']} actualizado.")

def eliminarEmpleado(indice):
    if 0 <= indice < len(empleados):
        eliminado = empleados.pop(indice)
        print(f"Empleado {eliminado['nombre']} eliminado.")

def calcularPromedio():
    if empleados:
        totalEdad = sum(empleado['edad'] for empleado in empleados)
        promedio = totalEdad / len(empleados)
        print(f"La edad promedio es: {promedio:.2f} años.")

while True:
    print("\n")
    print("1. Agregar empleado")
    print("2. Listar empleados")
    print("3. Actualizar empleado")
    print("4. Eliminar empleado")
    print("5. Calcular edad promedio (opcional)")
    print("6. Salir.")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        nombre = input("Ingrese el nombre del empleado: ")
        edad = int(input("Ingrese la edad del empleado: "))
        puesto = input("Ingrese el puesto del empleado: ")
        agregarEmpleado(nombre, edad, puesto)
        
    elif opcion == '2':
        listarEmpleados()
        
    elif opcion == '3':
        listarEmpleados()
        indice = int(input("Seleccione el número del empleado a actualizar: ")) - 1
        nueva_edad = input("Ingrese la nueva edad (dejar vacío si no desea cambiar): ")
        nuevo_puesto = input("Ingrese el nuevo puesto (dejar vacío si no desea cambiar): ")
        actualizarEmpleado(indice, int(nueva_edad) if nueva_edad else None, nuevo_puesto if nuevo_puesto else None)
        
    elif opcion == '4':
        listarEmpleados()
        indice = int(input("Seleccione el número del empleado a eliminar: ")) - 1
        eliminarEmpleado(indice)
        
    elif opcion == '5':
        calcularPromedio()
        
    elif opcion == '6':
        break