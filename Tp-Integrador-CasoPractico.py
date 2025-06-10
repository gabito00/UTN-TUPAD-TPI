import random
import time

# --------- Generar lista de productos ---------
def generar_productos(n):
    return [{'codigo': i, 'nombre': f'Prod{i}', 'precio': random.randint(100, 1000)} for i in range(n)]

# --------- Búsqueda lineal ---------
def busqueda_lineal(lista, campo, valor):
    for p in lista:
        if str(p[campo]) == str(valor):
            return p
    return None

# --------- Búsqueda lineal todos ---------
def busqueda_lineal_todos(lista, campo, valor):
    resultados = []
    for p in lista:
        if str(p[campo]) == str(valor):
            resultados.append(p)
    return resultados

# --------- Búsqueda binaria ---------
def busqueda_binaria(lista, campo, valor):
    izq, der = 0, len(lista)-1
    while izq <= der:
        medio = (izq+der)//2
        actual = lista[medio][campo]
        if str(actual) == str(valor):
            return lista[medio]
        elif str(actual) < str(valor):
            izq = medio+1
        else:
            der = medio-1
    return None

# --------- Búsqueda binaria todos ---------
def busqueda_binaria_todos(lista, campo, valor):
    izq, der = 0, len(lista)-1
    valor = str(valor)
    resultados = []
    while izq <= der:
        medio = (izq + der) // 2
        actual = str(lista[medio][campo])
        if actual == valor:
            # Encontrado: buscar a izquierda y derecha
            # Izquierda
            i = medio
            while i >= 0 and str(lista[i][campo]) == valor:
                i -= 1
            i += 1
            while i < len(lista) and str(lista[i][campo]) == valor:
                resultados.append(lista[i])
                i += 1
            break
        elif actual < valor:
            izq = medio + 1
        else:
            der = medio - 1
    return resultados if resultados else None


# --------- Ordenamientos ---------
def merge_sort(lista, campo):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izquierda = merge_sort(lista[:mid], campo)
    derecha = merge_sort(lista[mid:], campo)
    return merge(izquierda, derecha, campo)

def merge(izq, der, campo):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i][campo] <= der[j][campo]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# --------- Función para medir tiempo ---------
def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

# --------- Mostrar lista ordenada ---------
def mostrar_lista(lista, campo, cantidad=10):
    print(f"\nPrimeros {cantidad} productos ordenados por '{campo}':")
    for p in lista[:cantidad]:
        print(p)

# --------- Ejemplo de uso ---------
def main():
    campos = {
    "1": "nombre",
    "2": "precio",
    "3": "codigo"
    }

    n = int(input("¿Cuántos productos querés generar? (ej: 1000): "))
    productos = generar_productos(n)

    # Elegir campo de ordenamiento
    print("¿Por qué campo querés ordenar? (nombre, precio, codigo): ")
    for k, v in campos.items():
        print(f"{k}. {v.capitalize()}")

    while True:
        opcion = input("Elegí una opción (1-3): ").strip()
        if opcion in campos:
            campo_orden = campos[opcion]
            break
        else:
            print("Opción inválida. Elegí 1, 2 o 3.")

    print("\nMidiendo tiempos de ordenamiento por", campo_orden)
    ordenados_merge, tiempo_merge = medir_tiempo(merge_sort, productos, campo_orden)
    campo_orden_actual = campo_orden

    print(f"MergeSort: {tiempo_merge:.4f} seg")

    # Opción para mostrar la lista ordenada
    opcion = input(f"\n¿Querés ver la lista ordenada por '{campo_orden}'? (s/n): ").strip().lower()
    if opcion == 's':
        while True:
            try:
                cantidad = int(input(f"¿Cuántos productos querés ver? (1-{n}): "))
                if 1 <= cantidad <= n:
                    break
                else:
                    print(f"Por favor, ingresá un número entre 1 y {n}.")
            except ValueError:
                print("Por favor, ingresá un número válido.")
        mostrar_lista(ordenados_merge, campo_orden, cantidad=cantidad)

    # Elegir tipo y campo de búsqueda
    print("\n¿Por qué campo querés buscar?")
    for k, v in campos.items():
        print(f"{k}. {v.capitalize()}")

    while True:
        opcion = input("Elegí una opción (1-3): ").strip()
        if opcion in campos:
            campo_busqueda = campos[opcion]
            valor = input(f"Ingresá el valor a buscar en '{campo_busqueda}': ").strip()
            break
        else:
            print("Opción inválida. Elegí 1, 2 o 3.")

    # VERIFICAR si la lista está ordenada por el campo de búsqueda antes de binaria
    if campo_orden_actual == campo_busqueda:
        buscarTodos= input("Desea buscar todos? (s/n)").strip()
        if buscarTodos=='s':
            _, tiempo_binaria = medir_tiempo(busqueda_binaria_todos, ordenados_merge, campo_busqueda, valor)
            res_bin = busqueda_binaria_todos(ordenados_merge, campo_busqueda, valor)
        else:
            _, tiempo_binaria = medir_tiempo(busqueda_binaria, ordenados_merge, campo_busqueda, valor)
            res_bin = busqueda_binaria(ordenados_merge, campo_busqueda, valor)
        
        print(f"Búsqueda Binaria (lista ordenada): {tiempo_binaria:.6f} seg")
        print(f"Se encontraron {len(res_bin)} resultados:")
        mostrar_lista(res_bin, campo_busqueda, cantidad=len(res_bin))  # Mostramos todos los resultados encontrados
    else:
        print(f"\n[AVISO] La búsqueda binaria requiere que la lista esté ordenada por '{campo_busqueda}'.")
        print(f"Actualmente está ordenada por '{campo_orden_actual}'. No es posible aplicar búsqueda binaria.")

if __name__ == "__main__":
    main()
