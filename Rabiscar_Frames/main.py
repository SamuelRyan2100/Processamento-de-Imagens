import cv2
import numpy as np
import funcoes as fv


if __name__ == "__main__":

    caminho_video = "video.mp4"

    captura, largura, altura, fps = fv.abrir_video(caminho_video)

    escritor = fv.criar_escritor_video("video_com_desenho.avi", largura, altura, fps)

    canvas = np.zeros((altura, largura, 3), dtype="uint8")

    cv2.namedWindow("Video")

    cv2.setMouseCallback(
        "Video",
        fv.evento_mouse,
        {"canvas": canvas}
    )

    while captura.isOpened():

        ret, frame = captura.read()

        if not ret:
            break

        frame_saida = cv2.add(frame, canvas)

        cv2.imshow("Video", frame_saida)

        escritor.write(frame_saida)

        tecla = cv2.waitKey(20) & 0xFF

        if tecla == ord('q'):
            break

        elif tecla == ord('c'):
            fv.trocar_cor()

        elif tecla == 32:  # espaço
            fv.limpar_desenhos(canvas)

    captura.release()
    escritor.release()
    cv2.destroyAllWindows()