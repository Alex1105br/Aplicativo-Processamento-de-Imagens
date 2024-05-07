import cv2
import numpy as np

def dente_de_serra(image):
    # Copia a imagem original para evitar alterações na imagem original
    img_contrast = image.copy()

    # Aplicar a transformação do dente de serra para cada pixel da imagem
    for i in range(image.shape[0]): # Linhas
        for j in range(image.shape[1]): # Colunas
            for k in range(image.shape[2]): # Canais
                if img[i, j, k] < 63:
                    img_contrast[i, j, k] = int(255 * img[i, j, k] / 62)
                elif img[i, j, k] < 127:
                    img_contrast[i, j, k] = int(255 * (img[i, j, k] - 63) / 63)
                elif img[i, j, k] < 191:
                    img_contrast[i, j, k] = int(255 * (img[i, j, k] - 127) / 63)
                else:
                    img_contrast[i, j, k] = int(255 * (img[i, j, k] - 191) / 64)

    return img_contrast

# Ler a imagem em cores
img = cv2.imread('imagemSerra.png')

# Aplicar a transformação do dente de serra
img_dente_de_serra = dente_de_serra(img)

cv2.imwrite("img_DenteDeSerra_imagemSerra.png", img_dente_de_serra)
cv2.waitKey(0)
cv2.destroyAllWindows()