import cv2
import numpy as np



def radiometric_expansion(image, za, zb, z1, zn):
    # Copia a imagem original para evitar alterações na imagem original
    img_contrast = image.copy()

    # Aplicar a transformação linear para cada pixel da imagem
    for i in range(image.shape[0]): # Linhas
        for j in range(image.shape[1]): # Colunas
            for k in range(image.shape[2]): # Canais
                if image[i, j, k] <= za:
                    img_contrast[i, j, k] = z1
                elif image[i, j, k] >= zb:
                    img_contrast[i, j, k] = zn
                else:
                    img_contrast[i, j, k] = int(((image[i, j, k] - za) / (zb - za)) * (zn - z1) + z1)

    return img_contrast

# Ler a imagem em cores
img = cv2.imread("testefusca.png")

# Obter os valores de za e zb usando a limiarização automática de Otsu
za = int(input('Digite um valor para za: '))
zb = int(input('Digite um valor para zb: '))

# Definir os valores de z1 e zn para o novo intervalo de intensidade desejado
z1 = 0
zn = 255

# Aplicar a transformação radiométrica de expansão de contraste linear
img_contrast = radiometric_expansion(img, za, zb, z1, zn)


cv2.imwrite("img_ExpansaoContraste.png", img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()

