import os
#Inicio sesion

def creacion():
    global usuario1, usuario2, contra1, contra2
    usuario1 = "usuario1"
    usuario2 = "usuario2"
    contra1 = "contra1"
    contra2 = "contra2"
    
    global medicos, duenos, mascotas, citas, productos, facturas, historial
    medicos = []
    duenos = []
    mascotas = []
    citas = []
    productos = []
    facturas = []
    historial = []

    global vacunas
    vacunas = []    

def login():
    os.system('cls')
    usuarioIngreso = input("Digite un Usuario: ")
    while usuarioIngreso != usuario1 and usuarioIngreso != usuario2:
        print("Usuario Invalido, Por favor ingrese un Usuario: ")
        usuarioIngreso = input("Ingrese el nombre de Usuario: ")
    print("Usuario valido")

    #password
    contraseñaIngreso = input("Digite una contraseña: ")
    while contraseñaIngreso != contra1 and contraseñaIngreso != contra2:
        print("Contraseña Invalida, Por favor ingrese una Contraseña: ")
        contraseñaIngreso = input("Ingrese la Contraseña: ")
    print("Bienvenido")



def menu_principal():
    os.system('clear' if os.name == 'posix' else 'cls')
    opcion = input("""
********************************************************
Bienvenido a la veterinaria de Progra Básica
         ****MENÚ PRINCIPAL****            
1 - Módulo de registro
2 - Módulo de Clínica
3 - Módulo de Venta de Productos
4 - Historial
5 - Salir

Opción: """)
    match opcion:
        case '1': modulo_registro()
        case '2': modulo_clinica()
        case '3': vender_productos()
        case '4': modulo_historial()
        case '5':
            print("Gracias por utilizar nuestro programa!")
            exit()
        case _: menu_principal()

#Definición de variables



def modulo_registro():
    print()
    while True:
        print("\t Seleccione una opción:")
        print("\t1 - Registrar médico")
        print("\t2 - Registrar dueño")
        print("\t3 - Registrar mascota")
        print("\t4 - Salir")
        opcion = input("\nIngrese una Opción: ")
        if opcion == "1":
            registrar_medico()
        elif opcion == "2":
            registrar_dueno()
        elif opcion == "3":
            registrar_mascota()
        elif opcion == "4":
            menu_principal()
        else:
            print("Opción inválida. Por favor, seleccione otra opción.")

def registrar_medico():
    nombre = input("Digite el nombre del médico: ")
    codigo = int(input("Digite el codigo del médico: "))
    especialidad = input("Digite la especialidad del médico: ")
    telefono = int(input("Digite el numero telefonico del médico: "))
    correo = input ("Digite el correo del médico: ")
    dispo = input ("Digite la disponibilidad de horario del médico: [Solamente uno por jornada laboral] ((1) Mañanas: L-V, (2) Tardes: L-V, (3) Fines de semana: S-D): ")
    
    if dispo == "1":
        print ()
        print ("Disponibilidad en las mañanas guardada.")
    elif dispo == "2":
        print ()
        print ("Disponibilidad en las tardes guardada.")
    elif dispo == "3":
        print ()
        print ("Disponibilidad los fines de semana guardada.")
    
    medico = {"Nombre del médico": nombre, "Especialidad": especialidad, "Codigo": codigo, "Numero telefonico": telefono, "Correo electronico": correo, "Disposicion": dispo}
    medicos.append(medico)
    
    print ()
    print("Nombre del médico:", nombre, "\nEspecialidad:", especialidad, "\nCodigo:", codigo, "\nNumero telefonico:", telefono, "\nCorreo electronico:", correo, "\nDisposicion:", dispo)
    print("\nEl médico ha sido registrado exitosamente.\n")

def registrar_dueno():

    global duenos

    nombre = input("Digite el nombre completo del dueño: ")
    cedula = input("Digite la cédula del dueño: ")
    telefono = int(input("Digite el numero telefonico del dueño: "))
    correo = input("Digite el correo del dueño: ")
    direccion = input("Digite la dirección del dueño: ")
    
    dueno = {"Nombre completo": nombre, "Cedula": cedula, "Numero telefonico": telefono, "Correo electronico": correo, "Direccion": direccion, "Mascotas": []}
    duenos.append(dueno)
    
    print()
    print("Nombre del dueño:", nombre, "\nCédula:", cedula, "\nNumero telefonico:", telefono, "\nCorreo electronico:", correo, "\nDireccion:", direccion)
    print("\nLos datos del dueño han sido registrados exitosamente.\n")

def registrar_mascota():
    nombre_dueno = input("Digite el nombre del dueño de la mascota: ")
    dueno = None
    
    global mascotas
    
    mascotas=[]
    for d in duenos:
        if d["Nombre completo"] == nombre_dueno:
            dueno = d
            break
    if dueno is None:
        print("El dueño no existe.")
        return

    nombre = input("Digite el nombre de la mascota: ")
    raza = input("Digite la raza de la mascota: ")
    fecha_nacimiento = input("Digite la fecha de nacimiento de la mascota: ")
    sexo = input("Digite el sexo de la mascota: ")
    peso = float(input("Digite el peso de la mascota: "))
    caracteristicas = input("Digite las características de la mascota: ")
    alimento = input("Digite el alimento que consume la mascota: ")
    observaciones_generales = input("Digite observaciones generales sobre la mascota: ")
    
    mascota = {"Nombre:": nombre, "\nRaza de la mascota:": raza, "\nFecha de nacimiento:": fecha_nacimiento, "\nSexo de la mascota:": sexo, "\nPeso de la mascota:": peso, "\nCaracteristicas de la mascota:": caracteristicas, "\nObservaciones extra:": observaciones_generales}
    
    mascotas.append(mascota)

    print()
    print("Nombre de la mascota:", nombre)
    print("Raza de la mascota:", raza)
    print("Fecha de nacimiento de la mascota:", fecha_nacimiento)
    print("Sexo de la mascota:", sexo)
    print("Peso de la mascota:", peso)
    print("Características de la mascota:", caracteristicas)
    print("Alimento que consume la mascota:", alimento)
    print("Observaciones generales sobre la mascota:", observaciones_generales)
    print("\nLa mascota ha sido registrada exitosamente.\n")


def modulo_clinica():
    while True:
        print("\t\nBienvenido al módulo de clínica\n")
        print("\t¿Qué acción desea realizar?\n")
        print("\t1 - Control de citas")
        print("\t2 - Agendar cita")
        print("\t3 - Vacunación")
        print("\t4 - Cancelación de cita")
        print("\t5 - Salir\n")
        
        opcion = int(input("Digite el número correspondiente a la opción que desea seleccionar: "))

        if opcion == 1:
            print("\n***Control de citas***\n")
            if len(citas) == 0:
                print("\n***No hay citas agendadas***")
            else:
                print("\n****Las citas agendadas son las siguientes:****")
                for cita in citas:
                    print(cita)
                    
        elif opcion == 2:
            print("\n***Agendar cita***\n")
            nombre = input("Digite el nombre del paciente: ")
            fecha = input("Digite la fecha de la cita (dd/mm/aaaa): ") 
            hora = input("Digite la hora de la cita (hh:mm): ")
            nueva_cita = (nombre, fecha, hora)
            citas.append(nueva_cita)

            
            registro = {"Nombre:",nombre,"\nHora de la cita:",hora,"\nFecha de la cita:",fecha}
            historial.append(registro)
            print ("\nNombre del paciente:",nombre,"\nHora de la cita:",hora,"\nFecha de la cita:",fecha)
            print("\n**Cita agendada exitosamente**")

        elif opcion == 3:
            print("\n***Vacunación***\n")
            print ("\n * Contamos con los siguientes tipos de vacunas * ")
            print ()
            print ("\t1 -- Vacuna Tipo1")
            print ("\t2 -- Vacuna Tipo2")
            print ("\t3 -- Vacuna Tipo3")
            print ()
            
            nombre = input("Digite el nombre del paciente: ")
            vacuna = int(input("Digite el tipo de vacuna que desea: "))
            if vacuna == 1:
                print ("Ha escogido la vacuna: Tipo1. (3 dosis) (Una dosis por semana)")
            elif vacuna == 2:
                print ("Ha escogido la vacuna: Tipo2. (2 dosis) (Una dosis por mes)")
            elif vacuna == 3:
                print ("Ha escogido la vacuna: Tipo3. (5 dosis) (Todos los dias, durante una semana")
            else:
                print("La vacuna indicada no se encuentra disponible")
            print ("A continuacion se presenta la disponibilidad para agendar una cita de vacunacion:" "\n(1) Mañanas: L-V" "\n(2) Tardes: L-V" "\n(3) Fines de semana: S-D")
            agenda = int(input("Digite el numero correspondiente a los dias en los que desee agendar su cita: "))
            if agenda == 1:
                print ("Cita agendada en la opcion #1: *Mañanas: L-V *")
            elif agenda == 2:
                print ("Cita agendada en la opcion #2: *Tardes: L-V *")
            elif agenda == 3:
                print ("Cita agendada en la opcion #3: *Fines de semana: S-D *")
            else:
                print ("La opcion indicada no se encuentra disponible.")
            
            nueva_vacuna = (nombre, vacuna)
            vacunas.append(nueva_vacuna)
            print("\n**Vacuna registrada exitosamente**")
    
        elif opcion == 4:
            print("\n***Cancelación de cita***\n")
            if len(citas) == 0:
                print("\n***No hay citas agendadas para cancelar***")
    
            else:
                print ("Estas son las citas agendadas:")
                print ()
                print ("Nombre del paciente:",nombre)
                print ("Fecha de la cita:",fecha)
                print ("Hora de la cita:",hora)
                print ()
                nombre = input("Digite el nombre del paciente que posee la cita que desee cancelar: ")
                for cita in citas:
                    if cita[0] == nombre:
                        citas.remove(cita)
                        print("**Cita cancelada exitosamente**")
                        break
                else:
                    print("***No se encontró una cita para el paciente especificado***")
        
        elif opcion == 5:
            menu_principal()    
        
        else:
            print("\n***La opción ingresada no se encuentra dentro de las disponibles, por favor, inténtelo de nuevo.***")

def write(nombre_cliente, productos_comprados, cant, total_pagar, impuesto, descuento, total):
    if os.path.isfile("facturas.txt") == False: open("facturas.txt", "w+").close()
    with open("facturas.txt", 'a') as f: #se abre el documento
        f.write(f"Cliente: {nombre_cliente}\n")
        f.write(f"Productos:\n")
        for producto in productos_comprados:
            f.write(f"{producto}\n")
        f.write(f"Cantidad de productos: {cant}\n")
        f.write(f"Subtotal: {total_pagar}\n")
        f.write(f"IVA: {impuesto}\n")
        f.write(f"Descuento: {descuento}\n")
        f.write(f"Total a pagar: {total}\n")
        f.write("---------------------------------\n")

def transaccion(prod, cant):
    productos=[16000,34000,20000,30000,30000,15000.5000,8000,10000,25000]
    productos = [["Alimento para cachorros", 16000],["Alimento para adultos", 34000],
                 ["Alimento para felinos", 20000],["Desparasitantes", 30000],
                 ["Vacunas", 30000],["Shampoo para mascotas", 15000],
                 ["Juguete para mascota", 5000],["Snacks para mascotas", 8000],
                 ["Collares y accesorios", 10000],["Grooming para su mascota", 25000]]
    compra = []
    compra.append(productos[prod-1][0])
    compra.append(productos[prod-1][1]*cant)
    return compra

def factura(nombre_cliente, productos_comprados, cant, total_pagar):
    impuesto = total_pagar * 0.13
    descuento = total_pagar * 0.10
    total = impuesto + total_pagar - descuento
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\t----- Factura -----")
    print ()
    print("\t-Cliente:",nombre_cliente)
    print("\t-Productos comprados: ")
    for producto in productos_comprados:
        print("\t*",producto)
    print("\t - Cantidad de productos:",cant)
    print("\t - Subtotal: ¢",total_pagar)
    print("\t - IVA:",impuesto)
    print("\t - Descuento:",descuento)
    print("\t - Total a pagar: ¢",total)
    print("\t-------------------")
    input("*presione enter para continuar*")
    write(nombre_cliente, productos_comprados, cant, total_pagar, impuesto, descuento, total)

def vender_productos():
    os.system('clear' if os.name == 'posix' else 'cls')
    nombre_cliente = input("Ingrese su nombre: ")

    total_pagar = 0
    productos_comprados = []
    cantidad_productos = 0

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        opcion = int(input("""
1-Alimento para chachorros ¢16.000
2-Alimento para adultos ¢34.000
3-Alimento para felinos ¢20.000
4-Desparasitantes ¢30.000
5-Vacunas ¢30.000
6-Shampoo para mascotas ¢15.000
7-Juguetes para mascota ¢5.000
8-Snacks para mascotas ¢8.000
9-Collares y accesorios ¢10.000
10-Grooming para su mascota ¢25.000
---------
11-Factura
12-Salir

Opcion: """))

        if opcion > 0 and opcion < 11: cant = int(input("Cantidad que desea llevar: "))

        match opcion:
            case 1: compra = transaccion(1,cant)
            case 2: compra = transaccion(2,cant)
            case 3: compra = transaccion(3,cant)
            case 4: compra = transaccion(4,cant)
            case 5: compra = transaccion(5,cant)
            case 6: compra = transaccion(6,cant)
            case 7: compra = transaccion(7,cant)
            case 8: compra = transaccion(8,cant)
            case 9: compra = transaccion(9,cant)
            case 10: compra = transaccion(10,cant)
            case 11: 
                compra = factura(nombre_cliente, productos_comprados, cantidad_productos, total_pagar)
                vender_productos()
            case 12: menu_principal()
            case _: continue
        
        total_pagar += compra[1]
        productos_comprados.append(compra[0])
        cantidad_productos += cant

def modulo_historial():
    while True:
        print("\tSeleccione una opción:")
        print("\t1 - Ver Ficha Clínica")
        print("\t2 - Ver Citas Programadas")
        print("\t4 - Salir")
        opcion = input("\nIngrese una Opción: ")
        if opcion == "1":      
            ver_historial_completo()            
        elif opcion == "2":
            ver_historial_paciente()                
        elif opcion == "4":
            menu_principal()
        else:
            print("Opción inválida. Por favor, seleccione otra opción.")

#Para el historial
            
def ver_historial_completo():
    if len(historial) == 0:
        print("El historial está vacío.")
    else:
        for registro in historial:
            print(registro)
           
def ver_historial_paciente():
    paciente = input("Ingrese el nombre del paciente: ")
    encontrados = False
    for registro in historial:
        if registro ["nombre"] == paciente:
            encontrados = True
            print(registro)
    if not encontrados:
        print("No se encontraron registros para ese paciente.")

#Llamada a la función para mostrar el menú
creacion()
login()
menu_principal()