import cv2

# variáveis globais para desenho
desenhando = False
x_anterior, y_anterior = -1, -1

# lista de cores para alternar
cores = [
    (0, 0, 255),   # vermelho
    (0, 255, 0),   # verde
    (255, 0, 0),   # azul
    (0, 255, 255), # amarelo
]

indice_cor = 0

def abrir_video(caminho_video):
    captura = cv2.VideoCapture(caminho_video)

    largura = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(captura.get(cv2.CAP_PROP_FPS))

    return captura, largura, altura, fps

# cria o arquivo de vídeo de saída
def criar_escritor_video(nome_saida, largura, altura, fps):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    escritor = cv2.VideoWriter(nome_saida, fourcc, fps, (largura, altura))
    return escritor

#Retorna a cor atual selecionada
def obter_cor_atual():
    global indice_cor
    return cores[indice_cor]

#Alterna entre as cores disponíveis
def trocar_cor():
    global indice_cor
    indice_cor = (indice_cor + 1) % len(cores)


def limpar_desenhos(canvas):
    canvas[:] = 0

#Função chamada quando o mouse é usado
def evento_mouse(evento, x, y, flags, parametros):
    global desenhando, x_anterior, y_anterior

    canvas = parametros["canvas"]

    if evento == cv2.EVENT_LBUTTONDOWN:
        desenhando = True
        x_anterior, y_anterior = x, y

    elif evento == cv2.EVENT_MOUSEMOVE:
        if desenhando:
            cv2.line(canvas,
                     (x_anterior, y_anterior),
                     (x, y),
                     obter_cor_atual(),
                     2)

            x_anterior, y_anterior = x, y

    elif evento == cv2.EVENT_LBUTTONUP:
        desenhando = False
