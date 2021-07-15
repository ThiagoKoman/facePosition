import cv2
import math

#Configurando as variaveis de texto
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (20,20)
fontScale              = .8
fontColor              = (255,255,255)
lineType               = 1


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

cap.set( 5 ,8)

while True:

    cont = 0

    # Ler frame
    _, img = cap.read()

    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width = img.shape[:2]

    # Detectar faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    cv2.line(img,(int((width/2) -5),int(height/2)),(int((width/2) +5),int(height/2)),(0,0,255),2)
    cv2.line(img,(int(width/2),int((height/2)-5)),(int(width/2),int((height/2)+5)),(0,0,255),2)
    
    # Calculo das áreas em valor métrico
    for (x, y, w, h) in faces:
        cont = cont+1
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        z = math.pow(w, -1.01) * 150

        lx = (((x+(w/2)) / width ) - 0.5) * (z - 0.1)
        ly = (((y+(h/2)) / height ) - 0.5) * (z * 0.6)

        cv2.line(img,(int(width/2),int(height/2)),(int(x+(w/2)),int(y+(h/2))),(0,255,0),1)
        cv2.putText(img,'('+str('%.2f' % lx)+', '+str('%.2f' % ly)+', '+str('%.2f' % z)+')', (int(x+(w/2)),int(y+(h/2))), font, .4,(0,255,0), 1)
        
        print('%.2f' % lx,'%.2f' % ly,'%.2f' % z)


    cv2.putText(img,'Faces : '+str(cont), (20,20), font, .8,(255,255,255), 2)

    # Display
    cv2.imshow('img', img)

    # Para de rodar o programa ao pressionar a tecla ESC
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
cap.release()