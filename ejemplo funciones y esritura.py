def preguntar_nombre():
    nombre= input(" Ingrese su nombre aqui: ")
    return nombre
def calcular_edad(año_nacimiento):
    edad= 2020 - año_nacimiento
    return edad
def preguntar_edad():
    año_nacimiento= input (" Ingrese su año de nacimiento: " )
    edad=calcular_edad(int(año_nacimiento))
    return edad
def preguntar_informacion():
    nombre=preguntar_nombre()
    edad=preguntar_edad()
    persona= {
        "nombre":nombre,
        "edad":edad
    }
    return persona
def iterar_lista(lista_personas):
    file=open('lista_personas.txt', 'w')
    for persona in lista_personas:
        file.write(persona["nombre"] + " " + str(persona["edad"]) + "\n")

lista_personas=[]
continuar="y"
while continuar == "y" or continuar== "Y":
    persona = preguntar_informacion()
    lista_personas.append(persona)
    continuar= input (" Ingresar otra persona ?  y/n: ")
    if continuar=="n" or continuar== "N":
        iterar_lista(lista_personas)
