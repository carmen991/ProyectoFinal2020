#Contact Book
import urllib.request, json 
import validators
import sys
contactos={}
def agregar_contacto():
    while(True):
        input_nom = input("Ingrese nombre y apellido del nuevo contacto\n")
        listaPalabras = input_nom.split()
        if len(listaPalabras) == 2:
            break

        else:
            print("\nNombre invalido, vuelva a intentarlo")
            print("\nEl contacto debe tener nombre y apellido")

            continue

    while(True):
        input_tel = input("Ingrese telefono del nuevo contacto\n")
        if input_tel.isdigit():
            break

        else:
            print("\nNumero Invalido, vuelva a intentarlo")

            print("\nEl numero solo debe tener digitos")

            continue

    while(True):
        input_email = input("Ingrese el correo del nuevo contacto\n")
        if validators.email(input_email):
            break
        else:

            print("\nCorreo Invalido, vuelva a intentarlo")

            print("\nEs necesario que ingrese correo")

            continue

    
    respuesta=input("Desea ingresar nombre de la empresa en la que trabaja el nuevo contacto? (y/n) ").lower()
    if respuesta == "y" or respuesta == "yes":
        input_comp = input("Ingrese la empresa en la que trabaja el nuevo contacto\n")

    respuesta=input("Desea ingresar informacion extra del nuevo contacto? (y/n) ").lower()
    if respuesta == "y" or respuesta == "yes":
        input_extra = input("Ingrese informacion extra del nuevo contacto\n")
        return
    else:
        return  
    

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
    print('Vamos a llamar')

def enviar_mensaje_contactos():
    print('Vamos a llamar')

def enviar_correo_contactos():
    print('Vamos a llamar')

def exportar_contactos():
    print('Vamos a llamar')


def main():
    with urllib.request.urlopen("http://demo7130536.mockable.io/contacts") as url:
        contactos = json.loads(url.read().decode())
        print(json.dumps(contactos,indent=4))
        exit = False

    while not exit:
        input_menu = int(input(''' Bienvenido a su Contact Manager, seleccione una opcion:
                                   1. Agregar Contacto 
                                   2. Buscar Contacto 
                                   3. Listar Contacto 
                                   4. Eliminar Contacto
                                   5. Llamar Contactos 
                                   6. Enviar mensaje a contacto 
                                   7. Enviar correo a contacto 
                                   8. Exportar Contactos\n'''))
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

if __name__ == "__main__":
    main()            