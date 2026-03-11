import cv2
import numpy as np

# função para caregar a imagem
def carregar_img(img_png):
    imagem = cv2.imread(img_png)

    if imagem is None:
        print("Erro ao carregar a imagem")
        return None
    
    return imagem

# função para converter a imagem para o espeço de cores HSV
def converter_para_hsv(imagem):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    return hsv

# cria a máscara de cor para detectar a cor 
def criar_mascara_cor(imagem_hsv, limite_inferior, limite_superior):
    mascara = cv2.inRange(imagem_hsv, limite_inferior, limite_superior) #verificar se cada pixel da imagem está dentro de um intervalo de cor
    return mascara

# função que aplica a máscara na imagem original
def aplicar_mascara(imagem, mascara):
    resultado = cv2.bitwise_and(imagem, imagem, mask=mascara) #manter apenas os pixels que são brancos
    return resultado


def destacar_vermelho(imagem, mascara):

    # converter a imagem para a escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # converter de volta para bgr
    cinza_bgr = cv2.cvtColor(cinza, cv2.COLOR_GRAY2BGR)

    # pegar as partes vermelhas da imagem original
    vermelho = cv2.bitwise_and(imagem, imagem, mask=mascara)

    # inverter máscara para pegar o fundo
    mascara_invertida = cv2.bitwise_not(mascara)

    # pegar fundo em cinza
    fundo = cv2.bitwise_and(cinza_bgr, cinza_bgr, mask=mascara_invertida)

    # juntar vermelho com o fundo cinza
    resultado = cv2.add(vermelho, fundo)

    return resultado