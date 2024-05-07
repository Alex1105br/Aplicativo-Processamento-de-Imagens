import cv2
import numpy as np

def alterar_brilho(img, valor):
    # Copiar a imagem para não modificar a original
    img_altBrilho = img.copy().astype(np.float32)
    
    # Obter as dimensões da imagem
    altura, largura, canais = img.shape
    
    # Percorrer os pixels da imagem
    for i in range(altura):
        for j in range(largura):
            for k in range(canais):  # Iterar sobre os canais de cor (pode ser 1 para imagens em tons de cinza ou 3 para RGB)
                
                img_altBrilho[i, j, k] += valor
                
                # Limitar o valor resultante para estar entre 0 e 255
                img_altBrilho[i, j, k] = max(img_altBrilho[i, j, k], 0)  # Garantir que não seja menor que 0
                img_altBrilho[i, j, k] = min(img_altBrilho[i, j, k], 255)  # Garantir que não seja maior que 255
    
    # Converter de volta para o tipo uint8 (0-255) para salvar a imagem
    img_altBrilho = img_altBrilho.astype(np.uint8)
    
    return img_altBrilho

# Ler a imagem
img = cv2.imread("londres_salvar.jpg")


valor = 100

img_altBrilho = alterar_brilho(img, valor)

# Salvar a imagem resultante no mesmo diretório
cv2.imwrite("img_altBrilho.jpg", img_altBrilho)
