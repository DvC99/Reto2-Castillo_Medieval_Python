""" Reto 2 Protegiendo al castillo medieval  #
    Daniel Valencia Cordero
    Mayo 15-2021 
"""
import math

def mtsTocm(metros):
  return ( (metros*100) )

def velocidad(tiempo, distancia):
  return( distancia//tiempo )

def cuerdaPuerta(cateto, angulo):
  #linspace(desde, hasta, cantidad_de_pasos)
  seno = math.sin(angulo)
  hipotenusa = cateto//seno
  return hipotenusa

def perimetroCirculo(radio):
  return (2*math.pi*radio)

def caluloChewbacca(longitudCuerda, diametroPolea):
  return( (longitudCuerda//(perimetroCirculo(diametroPolea//2)))//3 )

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
diametroPolea = int(input("Digite el diametro de la Polea en cm: \n"))
longitudPuertaMts = int(input("Digite la longitud de la puerta a cerrar en mts: \n"))
tiempoCerrarPuerta = int(input("Digite el tiempo en segundos que desea que se demora la puerta en cerrar: \n"))
#SE SUPONE QUE EL ANGULO SUPERIOR ENTRE EL MURO Y LA CUERUDA QUE TIRA LA PUERTA ES DE 45 GRADOS
anguloSuperior = 45
longitudPuertaCm = mtsTocm(longitudPuertaMts)
longitudCuerdaPuertaCm = cuerdaPuerta(longitudPuertaCm,anguloSuperior)

print("La longitud de la puerta en cm es: "+str(longitudPuertaCm))
print("El valor caluculado del la cuerda que tira de la puerta es: "+str(longitudCuerdaPuertaCm))

#CALCULO DEL NUMERO DE CHEWBACCAS NECESARIO PARA CERRAR LA PUERTA
print("Para poder cerrar la puerta de longitud "+str(longitudPuertaCm)+"cm, se necesitan que "+str(caluloChewbacca(longitudCuerdaPuertaCm, diametroPolea))+" Chewbacca sean usados para cerrarla si cada uno aguanta 3 vueltas antes de caer, para un total de "+str( (caluloChewbacca(longitudCuerdaPuertaCm, diametroPolea))*3)+" vueltas entre todos.")

#SE RALIZA EL CALUDLO DE LA VELOCIDAD PARA QUE SE CIEERE LA PUERTA EN EL TIEMPO DADO
print("Para que la puerta se cierre en "+str(tiempoCerrarPuerta)+"segundos, es necesario que los Chewbacca giren a una velocidad de "+str(velocidad(tiempoCerrarPuerta, longitudCuerdaPuertaCm))+"cms/seg.")