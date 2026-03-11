from funcoes import *

def main():

    imagem = carregar_img("img.png")

    if imagem is None:
        return
    
    hsv = converter_para_hsv(imagem)

    # primeiro intervalo de vermelho
    limite_inferior1 = np.array([0,120,70])
    limite_superior1 = np.array([10,255,255])

    # segundo intervalo de vermelho
    limite_inferior2 = np.array([170,120,70])
    limite_superior2 = np.array([180,255,255])

    mascara1 = criar_mascara_cor(hsv, limite_inferior1, limite_superior1)
    mascara2 = criar_mascara_cor(hsv, limite_inferior2, limite_superior2)

    # juntar as duas máscaras
    mascara = cv2.bitwise_or(mascara1, mascara2)

    # gerar resultado com vermelho colorido e resto cinza
    resultado = destacar_vermelho(imagem, mascara)

    cv2.imshow("Imagem original", imagem)
    cv2.imshow("Máscara da cor", mascara)
    cv2.imshow("Resultado final", resultado)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()