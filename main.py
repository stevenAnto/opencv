import cv2
import numpy as np

print('version',cv2.__version__)
print('version',np.__version__)

#usa la escala grises
#lo hace en matrices con IMREAD_GRAYSCALE
tarjeta = cv2.imread('tarejta.jpg',cv2.IMREAD_GRAYSCALE)
plantilla = cv2.imread('circuito_integrado.jpg',cv2.IMREAD_GRAYSCALE)
alto, ancho =  np.shape(tarjeta)
altop, anchop =  np.shape(plantilla)

print('ancho y alto',alto,ancho)
print('ancho y alto',altop,anchop)

#Si tiende a 1 se tiene semejanza
#devuelve una matriz
resultado =cv2.matchTemplate(tarjeta,plantilla,cv2.TM_CCOEFF_NORMED)
print('que tipo es ',type(resultado))
print('num de dimerisones',resultado.ndim)
print('num de elementos en cada dimension',resultado.shape)

print('Que es resultado',resultado)
#busca en la matriz de resultados los valores max y mininimos y sus posiciones
min,max,pos_min,pos_max= cv2.minMaxLoc(resultado)
print('miniomo,maximo,posmix,posmax',min,max,pos_min,pos_max)
pixel_superior_iz =pos_max
pixel_superior_derecha = (pos_max[0]+anchop,pos_max[1]+altop)
cv2.imshow('sin dibujo',tarjeta)
cv2.imshow('plantilla',plantilla)
cv2.waitKey(0)
cv2.destroyAllWindows()
tarjeta = cv2.imread('tarejta.jpg')

cv2.rectangle(tarjeta,pixel_superior_iz,pixel_superior_derecha,70,4)

cv2.imshow('resultado',tarjeta)
cv2.waitKey(0)

print(alto,ancho)

#cv2.imshow('Tarjeta',tarjeta)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imshow('Circuito',plantilla)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
