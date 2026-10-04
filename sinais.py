"""Funções reutilizáveis da Frente 2 (Sinais)."""
import numpy as np
from PIL import Image


def carregar_cinza(caminho, tamanho=256):
    """Carrega a imagem em tons de cinza e faz RECORTE CENTRAL.
    Recorte (e não resize) preserva o espectro de frequência."""
    img = np.asarray(Image.open(caminho).convert("L"), dtype=np.float32)
    h, w = img.shape
    if h < tamanho or w < tamanho:
        raise ValueError(f"{caminho}: {h}x{w} menor que o recorte {tamanho}")
    t, l = (h - tamanho) // 2, (w - tamanho) // 2
    return img[t:t + tamanho, l:l + tamanho]


def espectro_log(img):
    """Espectro de magnitude 2D, centralizado e em escala log."""
    F = np.fft.fftshift(np.fft.fft2(img))
    return np.log1p(np.abs(F))


def perfil_radial(espectro):
    """Média do espectro em anéis concêntricos: curva energia x frequência."""
    h, w = espectro.shape
    y, x = np.indices((h, w))
    r = np.hypot(y - h // 2, x - w // 2).astype(int)
    soma = np.bincount(r.ravel(), espectro.ravel())
    cont = np.bincount(r.ravel())
    return (soma / np.maximum(cont, 1))[: min(h, w) // 2]