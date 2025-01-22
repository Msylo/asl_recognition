import os
import cv2
import time
import uuid

IMAGE_PATH='CollectedImages'

#to be mapped in the future.
labels=['Hello','Yes', 'No']

#Number of images per label/sign
number_of_images = 10

#For loop for creating a directoory for each sign. 
for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(2)
    #Nested loop for saving image as jpg.
    for imgnum in range(number_of_images):
        ret,frame = cap.read()
        #convert to grayscale for normaliziing color channels 
        grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imagename = os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, grayScale)
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows