import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video_path = "bb3.mp4"

# Tente abrir o vídeo
video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print(f"Erro ao abrir o vídeo em {video_path}")
    exit()

# Leia o primeiro quadro do vídeo
returned, img = video.read()

if not returned:
    print("Erro ao ler o primeiro quadro do vídeo")
    exit()

# Selecione a caixa delimitadora na imagem
bbox = cv2.selectROI("Rastreando", img, False)

# Inicialize o rastreador em img e na caixa delimitadora
tracker = cv2.TrackerKCF_create()
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    #função para desenhar a caixa delimitadora

def goal_track(img, bbox):
    # função para rastrear o objeto do ponto que ele sai para onde ele vai

while True:
    check, img = video.read()

    # Atualize o rastreador em img e na caixa delimitadora
    success, bbox = tracker.update(img)

    # Chame drawBox()
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Errou", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Chame goal_track()
    goal_track(img, bbox)

    # Exiba o vídeo
    cv2.imshow("resultado", img)

    # Saia da janela de exibição quando a barra de espaço for pressionada
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break

video.release()
cv2.destroyAllWindows()
