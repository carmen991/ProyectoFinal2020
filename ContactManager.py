#Contact Book

import pandas as pd
url='http://demo7130536.mockable.io/contacts'
contactos=pd.read_json(url)
print(contactos)


exit = False

def agregar_contacto():
    input_nom = input("Ingrese nombre del nuevo contacto\n")
    input_tel = input("Ingrese telefono del nuevo contacto\n")
    contactos[input_nom] = input_tel  

def buscar_contacto():
    input_nom = input("Ingrese nombre del contacto que quiere buscar\n")
    existe = input_nom in contactos

    if existe:
        print(input_nom + " " + contactos[input_nom])
    else:
        print("El contacto no existe, intentelo de nuevo\n")

def listar_contacto():
    input_nom = input("Ingrese nombre del contacto que quiere editar\n")
    input_tel = input("Ingrese nuevo telefono del contacto\n")

    existe = input_nom in contactos

    if existe:
        contactos[input_nom] = input_tel
    else:
        print("El contacto no existe, intentelo de nuevo\n")

def eliminar_contacto():
    input_nom = input("Ingrese nombre del contacto que quiere eliminar\n")
    existe = input_nom in contactos

    if existe:
        del contactos[input_nom]
        print("Contacto eliminado con exito!!\n")
    else:
        print("El contacto no existe, intentelo de nuevo\n")

def llamar_contactos():
    

def enviar_mensaje_contactos():
    

def enviar_correo_contactos():
    

def exportar_contactos():
    

while not exit:

    input_menu = int(input(" 1. Agregar Contacto \n 2. Buscar Contacto\n 3. Listar Contacto\n 4. Eliminar Contacto\n 5. Llamar Contactos\n 6. Enviar mensaje a contacto\n 7. Enviar correo a contacto\n 8. Exportar Contactos"))
    if input_menu == 1:
        agregar_contacto()
    if input_menu == 2:
        buscar_contacto()
    if input_menu == 3:
        listar_contacto()
    if input_menu == 4:
        eliminar_contacto()
    if input_menu == 5:
        llamar_contactos()
    if input_menu == 6:
        enviar_mensaje_contactos()
    if input_menu == 7:
        enviar_correo_contactos()
    if input_menu == 8:
        exportar_contactos()            
    elif input_menu == 9:
        exit = True