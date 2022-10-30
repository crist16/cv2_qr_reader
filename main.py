import qrcode

print("Ingrese codigo a convertir")
diccionario = {
    "nombre" : "Cristobal",
    "apellido" : "Apellido"
}
aConvertir = input()

imagen = qrcode.make(diccionario)

imagen.save("cristobal.jpg")
