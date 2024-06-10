# Libs
import cv2

# Carregar video
video = cv2.VideoCapture('./content/movimento.mp4')
ok, frame = video.read() # ok = se conseguiu ler o frame, frame = o 1º frame

# Criar rastreador
tracker = cv2.TrackerCSRT_create()

# Bounding Box
bbox = cv2.selectROI(frame) # Seleciona objeto a ser rastreado

# Iniciar rastreador
ok = tracker.init(frame, bbox) # Ok = true indica que conseguiu iniciar o rastreador

while True:
    ok, frame = video.read()

    if not ok:
        break # Video concluido

    else:
        # Rastrear objeto
        ok, bbox = tracker.update(frame)

        # Desenhar bounding box
        if ok:
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2, 1)
        else:
            cv2.putText(frame, 'Objeto perdido', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
        
        # Mostrar video
        cv2.imshow('Rastreando', frame)
        if cv2.waitKey(1) & 0xFF == 27: # Fecha se for pressionado ESC
            break

        # Parar rastreamento
        if cv2.waitKey(1) & 0xFF == 27:
            break