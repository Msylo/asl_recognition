import cv2
import datetime
import time

print(cv2.__version__)


#camera selection
cap = cv2.VideoCapture(0);
#getting video resolution and dimensions etc
print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()) :
    ret, frame = cap.read()
    #colour overlay
    timeDate = str(datetime.datetime.now())
    #put text on video capture
    frame = cv2.putText(frame, timeDate, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)

    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grayScale)
    #end cam capture on key prompt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()