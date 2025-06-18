import pygame
import time

# Inicializa o mixer do pygame
pygame.mixer.init()

# Caminho do arquivo MP3 (substitua pelo seu arquivo)
arquivo_mp3 = "musica.mp3"

# Carrega a música
pygame.mixer.music.load('d.mp3')

# Inicia a reprodução
pygame.mixer.music.play()