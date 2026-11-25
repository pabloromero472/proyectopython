import dataset

miBase = dataset.connect("sqlite:///base.db")
tabla = miBase["Productos"]




usuario_correcto = "admin"
contraseña_correcta = "1234"

while True:
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Ingreso al sistema.\n")
        break
    else:
        print("Usuario o contraseña incorrecta.\n")

# --- MENÚ PRINCIPAL ---
while True:
    opcion = input(
        "\nA - Agregar"
        "\nL - Listar"
        "\nB / BT - Buscar por nombre"
        "\nAC - Actualizar por ID"
        "\nR - Remover por nombre"
        "\nID - Remover por ID"
        "\nS - Salir"
        "\nElija una opción: "
    ).strip().upper()

    match opcion:
        case "A":
            nombre = input("Producto: ").strip()
            precio = float(input("Precio: ").strip())
            categoria = input("Categoría: ").strip()

            tabla.insert({"Nombre": nombre, "Precio": precio, "Categoria": categoria})
            print("Producto agregado.")

        case "L":
            print("\n--- PRODUCTOS ---")
            for item in tabla:
                print(f'ID: {item["id"]} | Producto: {item["Nombre"]} | Precio: ${item["Precio"]} | Categoría: {item["Categoria"]}')

        case "B" | "BT":
            buscar = input("Producto a buscar: ").strip()
            encontrado = list(tabla.find(Nombre=buscar))

            if encontrado:
                for prod in encontrado:
                    print(f'ID: {prod["id"]} | Producto: {prod["Nombre"]} | Precio: ${prod["Precio"]} | Categoría: {prod["Categoria"]}')
            else:
                print("no se encontro el producto.")

        case "AC":
            id_actualizar = int(input("ID  actualizar: ").strip())
            nombre_nuevo = input("Nombre nuevo: ").strip()
            precio_nuevo = float(input("Precio nuevo: ").strip())
            cat_nueva = input("Categoría nueva: ").strip()

            tabla.upsert(
                {"id": id_actualizar, "Nombre": nombre_nuevo, "Precio": precio_nuevo, "Categoria": cat_nueva},
                ["id"]
            )
            print("Producto actualizado.")

        case "R":
            remover = input("Producto a remover: ").strip()
            tabla.delete(Nombre=remover)
            print(f'"{remover}" eliminado si existía en la base.')

        case "ID":
            borrar_id = int(input("ID del producto a remover: ").strip())
            tabla.delete(id=borrar_id)
            print(f"Producto con ID {borrar_id} eliminado si existía.")

        case "S":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción incorrecta.")