def presupuesto_de_ventas():
    unidades = int(input("Unidades: "))
    precio_de_venta = float(input("Precio de venta: $ "))
    operacion_2 = multiplicacion(unidades, precio_de_venta)
    print(f"Ventas: $ {operacion_2}")

def presupuesto_de_procuccion():
    unidades = int(input("Unidades a vender: "))
    inv_final = int(input("Inventario final: "))
    total_unidades = suma(unidades, inv_final)
    print(f"Total de unidades: {total_unidades}")
    inv_inicial = int(input("Inventario inicial: "))
    unidades_producir = resta(total_unidades, inv_inicial)
    print(f"Unidades a producir: {unidades_producir}")

def presupuesto_requerimiento_materiales():
    unidades_producir = int(input("Unidades a producir: "))
    materia_a = int(input("Material A: "))
    materia_b = int(input("Material B: "))
    total_a = multiplicacion(unidades_producir, materia_a)
    print(f"Total requerido A: ${total_a}")
    total_b = multiplicacion(unidades_producir, materia_b)
    print(f"Total requerido A: ${total_b}")

def presupuesto_compra_materiales():
    requerimiento_material = int(input("Requerimiento de material: "))
    inv_final = int(input("Inventario final: "))
    total_material = suma(requerimiento_material, inv_final)
    print(f"Total de material: {total_material}")
    inv_incial = int(input("Inventario inicial: "))
    material_comprar = resta(total_material, inv_incial)
    print(f"Material a comprar: {material_comprar}")
    precio_compra = float(input("Precio de compra: $"))
    material_a_total = multiplicacion(material_comprar, precio_compra)
    print(f"Total: ${material_a_total}")

def presupuesto_mano_obra():
    unidades_producir = int(input("Unidades a producir: "))
    horas_de_mo = float(input("Horas de M.O: "))
    total_horas = multiplicacion(unidades_producir, horas_de_mo)
    print(f"Total de horas: {total_horas}")
    precio_hora = float(input("Precio por hora: $"))
    costo_mo = multiplicacion(total_horas, precio_hora)
    print(f"Costo de M.O: ${costo_mo}")

def presupuesto_gasto_fabricacion():
    depreciacion = float(input("Depreciación: $"))
    seguros = float(input("Seguros: $"))
    mantenimiento = float(input("Mantenimiento: $"))
    energeticos = float(input("Energeticos: $"))
    varios = float(input("Varios: $"))
    total = depreciacion + seguros + mantenimiento + energeticos + varios
    print(f"Total: ${total}")

def presupuesto_gastos_admyvent():
    depreciacion = float(input("Depreciación: $ "))
    sueldos_salarios = float(input("Sueldos y Salarios: $ "))
    comisiones = float(input("Comisiones: $ "))
    varios = float(input("Varios: $ "))
    intereses = float(input("Intereses por obligaciones: $ "))
    operacion = depreciacion + sueldos_salarios + comisiones + varios + intereses
    print(f"Total: $ {operacion}")

def determinacion_costo():
    materialA = int(input("Material A: "))
    materialB = float(input("Material B: "))
    mo = int(input("Mano de Obra: "))
    gif = int(input("Gastos Indirectos de Fabricación: "))
    return materialA, materialB, mo, gif

def valuacion_inventariof():
    materialA = float(input("Material A: "))
    materialB = float(input("Material B: "))
    return materialA, materialB

def operacion_total(materialA, materialB):
    operacion = materialA + materialB
    return operacion

def operacion_costo(materialA, materialB, mo, gif):
    operacion = materialA + materialB + mo + gif
    return operacion

def multiplicacion(valor1, valor2):
    operacion = valor1 * valor2
    return operacion

def suma(valor1, valor2):
    suma = valor1 + valor2
    return suma

def resta(valor1, valor2):
    resta = valor1 - valor2
    return resta

meses = "Enero", "Febrero", "Marzo"
ciclo_presupues_financiero = False

casos = "Costo", "Cantidad", "Costo por unidad"

print(f"{'PRESUPUESTO MAESTRO':-^60}\n")

while True:
    inicio = input("Presione ENTER para continuar con el presupuesto de operación(o presione cualquier otra letra para salir)...")
    print()

    if not inicio == "":
        break
    # Presupuesto de ventas
    for mes in meses:
        print(f"{'--Presupuesto de ventas (' + mes + ')--':^60}")
        print("-" * 60)
        print("PRODUCTO A")
        print("-" * 60)
        presupuesto_de_ventas()
        print("-" * 60)
        print("PRODUCTO B")
        print("-" * 60)
        presupuesto_de_ventas()

    # Determinación de saldo clientes y flujo de entradas
    print(f"\n{'--Determinación de saldo clientes y flujo de entradas--':^60}")
    print("-" * 60)
    saldo_cliente_2019 = float(input("Saldo de clientes 2019: $"))
    saldo_cliente_2020 = float(input("Saldo de clientes 2020: $"))
    entradas_efectivo = suma(saldo_cliente_2019, saldo_cliente_2020)
    print(f"Entradas de efectivo: ${entradas_efectivo}")
    cobranza_2019 = float(input("Cobranza 2019: $"))
    cobranza_2020 = float(input("Cobranza 2020: $"))
    total_de_entradas_2020 = suma(cobranza_2019, cobranza_2020)
    print(f"Total de entradas 2020: ${total_de_entradas_2020}")
    total_de_saldo_clientes_2020 = resta(entradas_efectivo, total_de_entradas_2020)
    print(f"Total de saldo de clientes 2020: ${total_de_saldo_clientes_2020}")
    print("-" * 60)

    # Presupuesto de produccion
    for mes in meses:
        print(f"\n{'--Presupuesto de produccion (' + mes + ')--':^60}")
        print("-" * 60)
        print("PRODUCTO A")
        print("-" * 60)
        presupuesto_de_procuccion()
        print("-" * 60)
        print("PRODUCTO B")
        print("-" * 60)
        presupuesto_de_procuccion()
        print("-" * 60)

    # Presupuesto de requerimiento de materiales
    for mes in meses:
        print(f"\n{'--Presupuesto de requerimiento de materiales (' + mes + ')--':^60}")
        print("-" * 60)
        print("PRODUCTO A")
        print("-" * 60)
        presupuesto_requerimiento_materiales()
        print("-" * 60)
        print("PRODUCTO B")
        print("-" * 60)
        presupuesto_requerimiento_materiales()
        print("-" * 60)
    
    # Presupuesto compra de materiales
    for mes in meses:
        print(f"\n{'--Presupuesto compra de materiales (' + mes + ')--':^60}")
        print("-" * 60)
        print("MATERIAL A")
        print("-" * 60)
        presupuesto_compra_materiales()
        print("-" * 60)
        print("MATERIAL B")
        print("-" * 60)
        presupuesto_compra_materiales()
        print("-" * 60)

    # Determinacion de saldo de proveedores y flujo de salidas
    print(f"\n{'--Determinación de saldo de proveedores y flujo de salidas--':^60}")
    print("-" * 60)
    saldo_proveedores_2019 = float(input("Saldo de proveedores 2019: $"))
    compras_2020 = float(input("Compras 2020: $"))
    saldo_proveedores_2020 = suma(saldo_proveedores_2019, compras_2020)
    print(f"Saldo de proveedores 2020: ${saldo_proveedores_2020}")
    print("-" * 60)
    print("Salida de efectivo")
    print("-" * 60)
    cobranza_proveedores_2019 = float(input("Pago a proveedores 2019: $"))
    cobranza_proveedores_2020 = float(input("Pago a proveedores 2020: $"))
    total_de_pagos_2020 = suma(cobranza_proveedores_2019, cobranza_proveedores_2020)
    print(f"Total pagos 2020: ${total_de_pagos_2020}")
    saldo_proveedores_2020_total = resta(saldo_proveedores_2020, total_de_pagos_2020)
    print(f"Total de saldo de proveedores 2020: ${saldo_proveedores_2020_total}")
    print("-" * 60)

    # Presupuestos de mano de obra
    for mes in meses:
        print(f"\n{'--Presupuesto de mano de obra (' + mes + ')--':^60}")
        print("-" * 60)
        print("PRODUCTO A")
        print("-" * 60)
        presupuesto_mano_obra()
        print("-" * 60)
        print("PRODUCTO B")
        print("-" * 60)
        presupuesto_mano_obra()
        print("-" * 60)

    # Presupuesto de gastos de fabricacion
    for mes in meses:
        print(f"\n{'--Presupuesto de gastos de fabricación--':^60}")
        print("-" * 60)
        print(mes.upper())
        print("-" * 60)
        presupuesto_gasto_fabricacion()
        print("-" * 60)

    # Presupuesto de gastos de administracion y ventas
    for mes in meses:
        print(f"\n{'Presupuesto de Gastos de Administración y Ventas (' + mes + ')':^60}")
        print("-" * 60)
        presupuesto_gastos_admyvent()
        print("-" * 60)
    
    # Determinacion del costo unitario de productos terminados
    for caso in casos:
        print(f"{'Determinación del Costo Unitario de Productos Terminados (' + caso + ')':^80}")
        print("-" * 80)
        print("PRODUCTO A")
        print("-" * 80)
        materialA, materialB, mo, gif  = determinacion_costo()
        
    operacion = operacion_costo(materialA, materialB, mo, gif)
        
    print(f"Total de Gastos por Unidad:  {operacion}")

    situaciones = "Costo", "Cantidad", "Costo por unidad"
    total_costo = list()

    for situacion in situaciones:
        print(f"{'Determinación del Costo Unitario de Productos Terminados (' + situacion + ')':^80}")
        print("-" * 80)
        print("PRODUCTO B")
        print("-" * 80)
        materialA, materialB, mo, gif  = determinacion_costo()
    
    operacion = operacion_costo(materialA, materialB, mo, gif)

    print(f"Total de Gastos por Unidad:  {operacion}")
    print("-" * 80)

    # Valuacion de inventario finales			
    for caso in casos:
        print("-" * 50)
        print(f"{'Valuación de Inventarios Finales (' + caso + ')':^50}")
        print("-" * 50)
        print("INVENTARIO FINAL DE MATERIALES")
        print("-" * 50)
        materialA, materialB  = valuacion_inventariof()

    operacion = operacion_total(materialA, materialB)
        
    print(f"Total de Gastos por Unidad: $ {operacion}")

    situaciones = "Costo", "Cantidad", "Costo por unidad"
    total_costo = list()

    for situacion in situaciones:
        print("-" * 50)
        print(f"{'Valuación de Inventarios Finales (' + situacion + ')':^50}")
        print("-" * 50)
        print("INVENTARIO FINAL DE PRODUCTOS TERMINADOS")
        print("-" * 50)
        materialA, materialB  = valuacion_inventariof()

    operacion = operacion_total(materialA, materialB)

    print(f"Total de Gastos por Unidad: $ {operacion}")
    print("-" * 80)

    ciclo_presupues_financiero = True
    break

while ciclo_presupues_financiero:
    inicio = input("\nPresione ENTER para continuar con el presupuesto financiero(o presione cualquier otra letra para salir)...")
    print()

    if not inicio == "":
        break

    # Estado de costo produccion y ventas
    print(f"\n{('---Estado de costo produccion y ventas---'):^60}")
    print('-' * 60)
    Saldo_inicial_M = float(input("Saldo inicial materiales: $ "))
    Compra_materiales = float(input("Compra de materiales: $ "))
    Materiales_disponibles = suma(Saldo_inicial_M, Compra_materiales)
    print(f"Materiales disponibles: $ {Materiales_disponibles}")
    Inv_final_M = float(input("Inventario final de materiales: $ "))
    Materiales_Utl = (Materiales_disponibles - Inv_final_M)
    print(f"Materiales utilizados: $ {Materiales_Utl}")
    Mano_Obra = float(input("Mano de obra: $ "))
    GIF = float(input("GIF: $ "))
    Costo_Produccion = (Materiales_Utl + Mano_Obra + GIF)
    print(f"Costo de producción: $ {Costo_Produccion}")
    Inv_Ini_Pro_Ter = float(input("Inv. inicial producto terminado: $ "))
    Total_Pro_disponible = suma(Costo_Produccion, Inv_Ini_Pro_Ter)
    print(f"Total de producción disponible: $ {Total_Pro_disponible}")
    Inv_Final_Pro_Ter = float(input("Inv. final producto terminado: $ "))
    Costo_ventas = resta(Total_Pro_disponible, Inv_Final_Pro_Ter)
    print(f"Costo de ventas: $ {Costo_ventas}")
    print('-' * 60)

    # Estado de resultados
    print(f"\n{('---Estado de resultados---'):^60}")
    print('-' * 60)
    Ventas = float(input("Ventas: $ "))
    print(f"Costo de ventas: $ {Costo_ventas}")
    Utilidad_Neta = resta(Ventas, Costo_ventas)
    print(f"Utilidad Neta: $ {Utilidad_Neta}")
    Gas_Ope = float(input("Gastos de operación: $ "))
    Utilidad_Ope = resta(Utilidad_Neta, Gas_Ope)
    print(f"Utilidad Operativa: $ {Utilidad_Ope}")
    ISR = multiplicacion(Utilidad_Ope, 0.35)
    print(f"ISR 35%: $ {ISR}")
    PTU = multiplicacion(Utilidad_Ope, 0.10)
    print(f"PTU 10%: $ {PTU}")
    Utilidad = (Utilidad_Ope - ISR - PTU)
    print(f"Utilidad: $ {Utilidad}")
    print('-' * 60)

    # Flujo de efectivo
    print(f"\n{('---Flujo de efectivo---'):^60}")
    print('-' * 60)
    Saldo_inicial = float(input("Saldo inicial: $ "))
    Cobranza19 = float(input("Cobranza 2019: $ "))
    Cobranza20 = float(input("Cobranza 2020: $ "))
    Total_Cobranza = suma(Cobranza19, Cobranza20)
    print(f"Total de cobranza: $ {Total_Cobranza}")
    print('-' * 60)
    print("Salidas")
    print('-' * 60)
    Pago_Proveedores19 = float(input("Pago de proveedores 2019: $ "))
    Pago_Proveedores20 = float(input("Pago de proveedores 2020: $ "))
    print(f"Mano de obra: $ {Mano_Obra}")
    print(f"GIF: $ {GIF}")
    print(f"Gastos de operación: $ {Gas_Ope}")
    Compra_Maquinaria = float(input("Compra de maquinaria: $ "))
    ISR19 = float(input("Pago ISR 2019: $ "))
    print(f"Pago ISR 2020: $ {ISR}")
    Total_Salidas = (Pago_Proveedores19 + Pago_Proveedores20 + Mano_Obra + GIF + Gas_Ope + Compra_Maquinaria + ISR19 + ISR)
    print(f"Total de salidas: $ {Total_Salidas}")
    Flujo_efectivo = resta(Total_Cobranza, Total_Salidas)
    print(f"Flujo de efectivo: $ {Flujo_efectivo}")
    print('-' * 60)
    break