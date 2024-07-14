import os
import json

# Cambiar al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

generos = [
    "Fantasia juvenil", "Distopia", "Novela romantica clasica", "Realismo magico", "Fantasia", 
    "Novela psicologica", "Fantasia epica", "Ensayo historico", "Novela historica", 
    "Ficcion literaria", "Novela realista", "Novela gotica", "Literatura infantil", 
    "Ficcion contemporanea", "Divulgacion cientifica", "Ficcion surrealista", 
    "Novela de desarrollo personal", "Ciencia ficcion distopica"
]

def cargar_libros():
    try:
        with open("datos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Archivo 'datos.json' no encontrado en el directorio actual.")
        print("Directorio actual:", os.getcwd())
        exit()

def grabar_libros():
    with open("datos.json", 'w') as file:
        json.dump(libros, file, indent=4)

libros = cargar_libros()

def enter_para_continuar():
    input("Presione enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")

def credenciales():
    usuario_valido = "admin"
    pass_valido = "1234"
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese el Usuario: ")
        passw = input("Ingrese pass: ")
        if usuario == usuario_valido and passw == pass_valido:
            print("Bienvenido al sistema")
            enter_para_continuar()
            return True
        else:
            print("Ingreso incorrecto")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
            if intentos == 0:
                print("Usted supero el numero de intentos validos")
                return False

def menu_principal():
    print("\nMenu de Opciones:\n")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Modificar libro")
    print("4. Eliminar libro")
    print("5. Buscar libro")
    print("6. Salir")

def listar_generos():
    print("\nLista de generos:\n")
    for genero in generos:
        print(genero)
    print("")

def agregar_libro():
    print("\n*** Agregar Libro ***\n")
    ultimo_libro = libros[-1]
    ultimo_codigo = ultimo_libro.get("codigo")
    
    nuevo_codigo_num = int(ultimo_codigo) + 1
    
    nuevo_codigo = nuevo_codigo_num
    nom = input("Ingrese el nombre: ")

    listar_generos()
    gen = input("Ingrese el genero: ")

    print("")

    anio_publicacion = int(input("Ingrese el año de publicacion: "))

    autor = input("Ingrese el autor: ")

    nuevo_libro = {
        "codigo": nuevo_codigo,
        "nombre": nom,
        "genero": gen,
        "anio_publicacion": anio_publicacion,
        "autor": autor
    }

    libros.append(nuevo_libro)
    grabar_libros()
    print("Libro ingresado correctamente")
    enter_para_continuar()

def listar_libros():
    print("")
    print("*** Listado de Libros ***")
    for libro in libros:
        print(f"codigo: {libro['codigo']} - nombre: {libro['nombre']} - genero: {libro['genero']} - año: {libro['anio_publicacion']}")
    

    print("****")
    enter_para_continuar()
    
def encontrar_libro_por_codigo(libros, codigo):
    for libro in libros:
        if libro["codigo"] == codigo:
            return libro
    return None
def modificar_libro():
    listar_libros()
    codigo = int(input("Ingrese el número de código del libro a modificar: "))
    
    libro = encontrar_libro_por_codigo(libros, codigo)

    respuesta = input ("Desea modificar el nombre (S/N)? ")
    if respuesta == "S":
        nuevo_nombre = input ("Ingrese el nuevo nombre:  ")
        libro["nombre"] = nuevo_nombre

    respuesta = input ("Desea modificar el genero (S/N)? ")
    if respuesta == "S":
        nuevo_genero = input ("Ingrese el nuevo genero:  ")
        libro["genero"] = nuevo_genero
    
    respuesta = input ("Desea modificar el anio de publicacion (S/N)? ")
    if respuesta == "S":
        nuevo_anio_de_publicacion = input ("Ingrese el nuevo anio:  ")
        libro["anio de publicacion"] = nuevo_anio_de_publicacion


    respuesta = input ("Desea modificar el autor (S/N)? ")
    if respuesta == "S":
        nuevo_autor = input ("Ingrese el nuevo autor:  ")
        libro["autor"] = nuevo_autor

    grabar_libros()
    
    print("Libro modificado exitosamente!")
    enter_para_continuar()

def eliminar_libro():
    listar_libros()

    codigo = int(input("Ingrese el número de código del libro a eliminar: "))
    
    libro = encontrar_libro_por_codigo(libros, codigo)

    if libro is not None:
        libros.remove(libro)
        grabar_libros()
        print("Libro eliminado con éxito.")
    else:
        print("Código de libro no válido.")
    
    enter_para_continuar()

def buscar_libro():
    nombre_a_buscar = input("Ingrese el nombre del libro a buscar: ")
    resultados = [libro for libro in libros if nombre_a_buscar.lower() in libro["nombre"].lower()]
    if resultados:
        print("\n*** Resultados de la Busqueda ***")
        for i, libro in enumerate(resultados):
            print(f"{libro['codigo']} - {libro['nombre']} - {libro['genero']} - {libro['anio_publicacion']} - {libro['autor']}")
        print("****")
    else:
        print("No se encontraron libros con ese nombre.")
    enter_para_continuar()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    if credenciales():
        while True:
            menu_principal()
            opcion = int(input("Ingrese el numero de opcion elegida (fin: 6): "))
            if opcion == 6:
                break
            elif opcion == 1:
                agregar_libro()
            elif opcion == 2:
                listar_libros()
            elif opcion == 3:
                modificar_libro()
            elif opcion == 4:
                eliminar_libro()
            elif opcion == 5:
                buscar_libro()
            else:
                print("Opcion invalida")
                enter_para_continuar()
    
    print("Gracias por usar nuestra biblioteca virtual!")