#Contact Book
import requests, json 
import validators
import sys
import time

def importar_dic(urlGet,contactos):
    #Recibe contactos de un URL y los ingresa al diccionario
    getResponse=requests.get(urlGet)
    dataGet=getResponse.json()
    contactos = dataGet  
    return contactos

def AgregarContactos(input_nom, input_tel, input_email,input_comp,input_extra,contactos):
    #Con esto agregamos contactos nuevos al diccionario
    diccionario_nombre={}
    key = letra(input_nom)
    key2=input_nom
    nestedDictionary = {"telefono":input_tel,"email":input_email,"company":input_comp,"extra":input_extra}
    diccionario_nombre[key2] = nestedDictionary
    contactos[key]=diccionario_nombre
    return print("Contacto agregado exitosamente\n")

def letra(input_nom):
    #Tomamos primera letra del nombre
    nombre=input_nom.upper()
    key=nombre[0]
    return key

def agregar_contacto(contactos):
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
    else:
        input_comp=""    

    respuesta=input("Desea ingresar informacion extra del nuevo contacto? (y/n) ").lower()
    if respuesta == "y" or respuesta == "yes":
        input_extra = input("Ingrese informacion extra del nuevo contacto\n")
    else:
        input_extra=""    
    AgregarContactos(input_nom,input_tel,input_email,input_comp,input_extra,contactos)


def buscar_contacto(contactos):
    input_nom = input("Ingrese nombre del contacto que quiere buscar\n")
    nombre=input_nom.upper()
    letra=nombre[0]
    existe = letra in contactos
    if existe:
        letra2=contactos[letra]
        listSplit = input_nom.split(',')
        verifiedSplit = []
        invalidSplit = []
        iteration1 = 0
        for items in listSplit:
            if listSplit[iteration1] in letra2:
                verifiedSplit.append(listSplit[iteration1])
            else:
                invalidSplit.append(listSplit[iteration1])
            iteration1 = iteration1 + 1
        
        if len(invalidSplit) != 0:
            print('El contacto {} parece no existir en la lista de contactos'.format(', '.join(invalidSplit)))
            print("Asegúrese de haber escrito el contacto correctamente")

        elif len(invalidSplit) == 0:
            print('Contacto {} encontrado'.format(', '.join(verifiedSplit)))
    else:
        print("El contacto no existe, intentelo de nuevo\n")


def listar_contacto(contactos,indent=0):
   for key, value in contactos.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         listar_contacto(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def eliminar_contacto(contactos):
    input_nom = input("Ingrese nombre del contacto que quiere eliminar\n")
    existe = input_nom in contactos

    if existe:
        del contactos[input_nom]
        print("Contacto eliminado con exito!!\n")
    else:
        print("El contacto no existe, intentelo de nuevo\n")

def llamar_contactos(contactos):
    #Llama al contacto ingresado
    input_nom = input("Ingrese nombre del contacto que quiere llamar\n")
    nombre=input_nom.upper()
    letra=nombre[0]
    existe = letra in contactos
    if existe:
      letra2=contactos[letra]
      if  input_nom in letra2:
          key = letra2[input_nom] #se ingresa el ID para que llame a la persona que desea 
          print("Llamando a: {}, con el numero: {}".format(input_nom, key['telefono'])) 
          for restantes in range(3, 0, -1): #contador de en retroseso de 60 segundos 
              sys.stdout.write("\r")
              sys.stdout.write("{:2d} Segundos restantes".format(restantes)) #se utilizo sys,stdout porque se pueden combinar int y string
              sys.stdout.flush()
              time.sleep(1)
          sys.stdout.write("\rSe realizo la llamada con éxito!!            \n")
      else:
          print('\nEl contacto está mal escrito o no existe.')
    else:
        print("El contacto no existe, intentelo de nuevo\n")


def enviar_mensaje_contactos():
    print('Vamos a llamar')

def enviar_correo_contactos():
    print('Vamos a llamar')

def exportar_contactos():
    print('Vamos a llamar')


def main():
    contactos={}
    urlGet="http://demo7130536.mockable.io/contacts"
    contactos = importar_dic(urlGet,contactos)
    exit=False

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
            agregar_contacto(contactos)
        if input_menu == 2:
            buscar_contacto(contactos)
        if input_menu == 3:
            listar_contacto(contactos)
        if input_menu == 4:
            eliminar_contacto(contactos)
        if input_menu == 5:
            llamar_contactos(contactos)
        if input_menu == 6:
            enviar_mensaje_contactos(contactos)
        if input_menu == 7:
            enviar_correo_contactos(contactos)
        if input_menu == 8:
            exportar_contactos(contactos)            
        elif input_menu == 9:
            exit = True

if __name__ == "__main__":
    main()            