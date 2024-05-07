import cv2
import numpy as np

#Tentar escurecer uma imagem(baixar o contraste) e bagunçar  e aplicar a transformada

def log_transform(image, c):
    # Copia a imagem original para evitar alterações na imagem original
    img_contrast = image.copy()

    # Aplicar a transformação logarítmica para cada pixel da imagem
    for i in range(image.shape[0]): # Linhas
        for j in range(image.shape[1]): # Colunas
            for k in range(image.shape[2]): # Canais
                img_contrast[i, j, k] = int(np.clip(c * np.log(1 + image[i, j, k]), 0, 255))

    return img_contrast

# Ler a imagem em cores
img = cv2.imread("fusca2.png")

# Definir o valor de c para controle da escala logarítmica de contraste

#No valor de entrada, eu achei o que teve melhor resultado foi o 50
c = float(input('Digite um valor: '))

# Aplicar a transformação de escala logarítmica de contraste
img_contrast = log_transform(img, c)

cv2.imwrite("img_EscalaLogaritmica.png", img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()


