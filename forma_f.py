import os
os.system("cls")


productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
} 

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una de las opciones disponibles: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_categoria(categoria):
    total = 0
    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total += stock[codigo][1]
            print(f"El total de unidades disponibles es: {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo in stock:
        precio = stock[codigo][0]
        disponible = stock[codigo][1]
        if p_min <= precio <= p_max and disponible != 0:
            resultados.append(productos[codigo][0] + "--" + codigo)
            resultados.sort()
            if len(resultados) == 0:
                print("No hay productos en ese rango de precio.")
            else:
                for elemento in resultados:
                    print(elemento)

def actualizar_precio(codigo, nuevo_precio):
    for clave in stock:
        if clave.lower() == codigo.lower():
            stock[clave][0] = nuevo_precio
            return True
        return False
    
def validar_codigo(codigo):
    if codigo.strip() == '':
        return False
    for clave in productos:
        if clave.lower() == codigo.lower():
            return False
        return True

def validar_nombre(nombre):
    return nombre.strip() != ''

def validar_categoria(categoria):
    return categoria.strip() != ''

def validar_marca(marca):
    return marca.strip() != ''

def validar_peso(peso_kg):
    return peso_kg > 0

def validar_es_importado(es_importado):
    return es_importado.lower() in ('s', 'n')

def validar_es_para_cachorro(es_para_cachorro):
    return es_para_cachorro.lower() in ('s', 'n')

def validar_precio(precio):
    return precio > 0

def validar_unidades(unidades):
    return unidades >= 0

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    for clave in productos:
        if clave.lower() == codigo.lower():
            return False
        productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
        stock[codigo] = [precio, unidades]
        return True

def eliminar_producto(codigo):
    for clave in productos:
        if clave.lower() == codigo.lower():
            del productos[clave]
            del stock[clave]
            return True
        return False
    
menu()
opcion = leer_opcion()

match opcion:
    case 1: 
        valor = input("Ingrese categoría a consultar: ")
        unidades_categoria(valor)
    case 2:
        while True:
            try:
                p_max = 0
                p_min = int(input("Precio minimo: "))
                p_max = int(input("Precio maximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros. ")
            if p_min >= 0 and p_min <= p_max:
                busqueda_precio(p_min, p_max)
            else:
                print("El rango ingresado no es valido. ")
    case 3:
        while True:
            codigo = input("Ingrese código del producto: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                print("Ingrese un valor valido.")
                continue
            if nuevo_precio <= 0:
                print("El precio debe ser un numero Entero positivo")
                continue
            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado.")
            else:
                print("El codigo no existe")
                repetir = input("¿Desea actualizar otro precio (s/n)?: ")
                if repetir.lower() != "s":
                    break
    case 4:
        codigo = input("Codigo: ").strip()
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        marca = input("Marca: ")
        peso_kg = float(input("Peso: "))
        es_importado = input("¿Es importado (s/n)?: ")
        es_para_cachorro = input("¿Es para cachorro (s/n)?: ")
        precio = int(input("Precio: "))
        unidades = ("Unidades: ")





    case 6:
        print("Programa finalizado.")
        
        