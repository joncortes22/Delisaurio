
#Inicio sesion

usuario1 = "usuario1"
usuario2 = "usuario2"
contra1 = "contra1"
contra2 = "contra2"

def usuario(usuario1, usuario2):
    print() 
    usuarioIngreso = input("Digite un Usuario: ")
    while usuarioIngreso != usuario1 and usuarioIngreso != usuario2:
        print("Usuario Invalido, Por favor ingrese un Usuario: ")
        usuarioIngreso = input("Ingrese el nombre de Usuario: ")
    print("Usuario valido")

def contraseña(contra1, contra2):
    contraseñaIngreso = input("Digite una contraseña: ")
    while contraseñaIngreso != contra1 and contraseñaIngreso != contra2:
        print("Contraseña Invalida, Por favor ingrese una Contraseña: ")
        contraseñaIngreso = input("Ingrese la Contraseña: ")
    print("Bienvenido")

usuario(usuario1,usuario2)
contraseña(contra1,contra2)

def menu_principal():

    print("********************************************************")
    print("\t Bienvenido a la veterinaria de Progra Básica.")
    print("\t          ****MENÚ PRINCIPAL****            \t")
    print()
    print("\t1 - Módulo de registro")
    print("\t2 - Módulo de Clínica")
    print("\t3 - Módulo de Venta de Productos")
    print("\t4 - Historial")
    print("\t5 - Salir")
    print()
    print()
    print("********************************************************")  
    
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            modulo_registro()
        elif opcion == "2":
            modulo_clinica()
        elif opcion == "3":
            vender_productos()
        elif opcion == "4":
            modulo_historial()
        elif opcion == "5":
            print("Gracias por utilizar nuestro programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione otra opción.")

#Definición de variables

medicos = []
duenos = []
mascotas = []
citas = []
productos = []
facturas = []
historial = []

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


citas = []
vacunas = []
 
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

def vender_productos():
    nombre_cliente = input("Ingrese su nombre: ")

    total_pagar = 0
    productos_comprados = []
    cantidad_productos = []
    descuento = 0

    while True:
        print()
        print("\tBienvenido a venta de productos")
        print()
        print("Contamos con los siguientes productos disponibles - " "\n(Por la compra de 3 o mas productos, se le aplica un 10% de descuento):")
        print()
        print("\t1 - Alimento para chachorros ¢16.000")
        print("\t2 - Alimento para adultos ¢34.000")
        print("\t3 - Alimento para felinos ¢20.000")
        print("\t4 - Desparasitantes ¢30.000")
        print("\t5 - Vacunas ¢30.000")
        print("\t6 - Shampoo para mascotas ¢15.000")
        print("\t7 - Juguetes para mascota ¢5.000")
        print("\t8 - Snacks para mascotas ¢8.000")
        print("\t9 - Collares y accesorios ¢10.000")
        print("\t10 - Grooming para su mascota ¢25.000")
        print("\t-----")
        print("\t11 - Factura")
        print("\t12 - Salir")
        print ()
        
        opcion = int(input("Digite la opción deseada: "))

        if opcion == 1:
            precio = 16000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Alimento para cachorros*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Alimento para cachorros")
            cantidad_productos.append(cantidad)
        elif opcion == 2:
            precio = 34000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Alimento para adultos*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Alimento para adultos")
            cantidad_productos.append(cantidad)
        elif opcion == 3:
            precio = 20000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Alimento para felinos*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Alimento para felinos")
            cantidad_productos.append(cantidad)
        elif opcion == 4:
            precio = 30000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Desparasitante*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Desparasitantes")
            cantidad_productos.append(cantidad)
        elif opcion == 5:
            precio = 30000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Vacunas*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Vacunas")
            cantidad_productos.append(cantidad)
        elif opcion == 6:
            precio = 15000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Shampoo de mascotas*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Shampoo para mascotas")
            cantidad_productos.append(cantidad)
        elif opcion == 7:
            precio = 5000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Juguete para mascota*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Juguete para mascota")
            cantidad_productos.append(cantidad)
        elif opcion == 8:
            precio = 8000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Snack para mascotas*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Snacks para mascotas")
            cantidad_productos.append(cantidad)
        elif opcion == 9:
            precio = 10000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Collares y accesorios*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Collares y accesorios")
            cantidad_productos.append(cantidad)
        elif opcion == 10:
            precio = 25000
            cantidad = int(input("Cuantos desea llevar?: "))
            print("\n****Se ha agregado: *Grooming*\n")
            total_pagar += precio * cantidad
            productos_comprados.append("Grooming para su mascota")
            cantidad_productos.append(cantidad)
        elif opcion == 11:
            impuesto = total_pagar * 0.13
            descuento = total_pagar * 0.10
            total = impuesto + total_pagar - descuento
            
            print("\t----- Factura -----")
            print ()
            print("\t-Cliente:",nombre_cliente)
            print("\t-Productos comprados: ")
            for producto in productos_comprados:
                print("\t*",producto)
            print("\t - Cantidad de productos:",cantidad_productos)
            print("\t - Subtotal: ¢",total_pagar)
            print("\t - IVA:",impuesto)
            print("\t - Descuento:",descuento)
            print("\t - Total a pagar: ¢",total)
            print("\t-------------------")
            print()
       
        elif opcion == 12:
            menu_principal()
        else:
            print("La opción que seleccionó es inválida.")

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
        
menu_principal()

 




