
from clases.persona import Persona
from clases.pelota import Pelota
from clases.celular import celular
from clases.vaso import vaso



persona1 = Persona("Juan", 30)
persona1.saludar()


pelota2 = Pelota("Fútbol", "rojo")
pelota2.rebotar()

celular3 = Telefono("Xioami", "Note", "789-654-3210")
celular3.hacer_llamada()

vaso4 = vaso("vidrio", 2)
vaso4.llenar()

emocion5 = emocion("felicidad", 8)
emocion5.cambiar_emocion()
