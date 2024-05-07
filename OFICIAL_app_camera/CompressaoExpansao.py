import cv2
import numpy as np

def contrast_transform(image):
    # Copia a imagem original para evitar alterações na imagem original
    img_contrast = image.copy()

    # Aplicar a transformação exponencial para cada pixel da imagem
    for i in range(image.shape[0]): # Linhas
        for j in range(image.shape[1]): # Colunas
            for k in range(image.shape[2]): # Canais
                if(image[i, j, k]<=85):
                    img_contrast[i,j,k] = int(image[i,j,k]/2)
                if(image[i,j,k]>85 and image[i,j,k]<170):
                    img_contrast[i,j,k] = int(2*image[i,j,k]-127)
                if(image[i,j,k]>=170):
                    img_contrast[i,j,k]= int((image[i,j,k]/2)+128)
                #img_contrast[i, j, k] = int(255 * np.power(image[i, j, k] / 255, image[i, j, k]))

    return img_contrast

# Ler a imagem em cores
img = cv2.imread('meme.jpeg')

# Aplicar a transformação de compressão/expansão de contraste
img_contrast = contrast_transform(img)

cv2.imwrite("img_CompressaoExpansao_meme.jpeg", img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()

