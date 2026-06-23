def mostrar_menu():
    print(" MENÚ PRINCIPAL ")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    

def leer_opcion():
    while True:
        try:
            opcion = int(input("elije una opción: "))

            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Ingrese un número del 1 al 6")

        except:
            print("Debe ingresar un número válido")


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_stock(stock):
    return stock >= 0


def validar_precio(precio):
    return precio > 0


def agregar_producto(productos):

    nombre = input("Nombre: ")

    if not validar_nombre(nombre):
        print("el Nombre es inválido")
        return

    try:
        stock = int(input("Stock: "))
    except:
        print("Stock inválido")
        return

    if not validar_stock(stock):
        print("Stock inválido")
        return

    try:
        precio = float(input("Precio: "))
    except:
        print("Precio inválido")
        return

    if not validar_precio(precio):
        print("Precio inválido")
        return

    producto = {
        "nombre": nombre,
        "stock": stock,
        "precio": precio,
        "disponible": False
    }

    productos.append(producto)
    print("el Producto fue agregado correctamente")


def buscar_producto(productos, nombre):

    for i in range(len(productos)):
        if productos[i]["nombre"] == nombre:
            return i

    return -1


def eliminar_producto(productos):

    nombre = input("Ingrese el nombre del producto: ")

    posicion = buscar_producto(productos, nombre)

    if posicion != -1:
        productos.pop(posicion)
        print("Producto eliminado correctamente")
    else:
        print(f"El producto '{nombre}' no se encuentra registrado.")


def actualizar_disponibilidad(productos):

    for producto in productos:

        if producto["stock"] > 0:
            producto["disponible"] = True
        else:
            producto["disponible"] = False

    print("Disponibilidad actualizada")


def mostrar_productos(productos):

    actualizar_disponibilidad(productos)

    print(" LISTA DE los PRODUCTOS ")

    for producto in productos:

        print("Nombre:", producto["nombre"])
        print("Stock:", producto["stock"])
        print("Precio:", producto["precio"])

        if producto["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN STOCK")    


productos = []

while True:

    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:

        agregar_producto(productos)

    elif opcion == 2:

        nombre = input("Ingrese el nombre del producto: ")

        posicion = buscar_producto(productos, nombre)

        if posicion != -1:

            print("Producto encontrado")
            print("Posición:", posicion)
            print("Nombre:", productos[posicion]["nombre"])
            print("Stock:", productos[posicion]["stock"])
            print("Precio:", productos[posicion]["precio"])

        else:
            print("el Producto no fue encontrado")

    elif opcion == 3:

        eliminar_producto(productos)

    elif opcion == 4:

        actualizar_disponibilidad(productos)

    elif opcion == 5:

        mostrar_productos(productos)

    elif opcion == 6:

        print("muchas Gracias por usar el sistema. Vuelva pronto")
        break