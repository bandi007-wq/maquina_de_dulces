saldo = 5.0
papas = 0
chocolate = 0
refresco = 0

opcion = 0

print("=================================")
print("      MAQUINA DE SNACKS")
print("=================================")
print("Saldo inicial: Bs.", saldo)


while True:

    print("\nProductos disponibles:")
    print("1. Papas      Bs. 1.50")
    print("2. Chocolate  Bs. 2.00")
    print("3. Refresco   Bs. 2.50")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))


    if opcion == 1:
        if saldo >= 1.50:
            saldo = saldo - 1.50
            papas = papas + 1
            print("Compra realizada.")
            print("Saldo restante: Bs.", round(saldo, 2))
        else:
            print("Saldo insuficiente.")


    elif opcion == 2:
        if saldo >= 2.00:
            saldo = saldo - 2.00
            chocolate = chocolate + 1
            print("Compra realizada.")
            print("Saldo restante: Bs.", round(saldo, 2))
        else:
            print("Saldo insuficiente.")


    elif opcion == 3:
        if saldo >= 2.50:
            saldo = saldo - 2.50
            refresco = refresco + 1
            print("Compra realizada.")
            print("Saldo restante: Bs.", round(saldo, 2))
        else:
            print("Saldo insuficiente.")

    elif opcion == 4:
        break

    else:
        print("Opción inválida.")

    if saldo < 1.50:
        print("\nYa no tiene saldo suficiente para comprar más productos.")
        break

print("\n========== RESUMEN ==========")
print("Papas compradas:", papas)
print("Chocolate comprados:", chocolate)
print("Refrescos comprados:", refresco)

total_productos = papas + chocolate + refresco

print("Total de productos comprados:", total_productos)
print("Saldo final: Bs.", round(saldo, 2))