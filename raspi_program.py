import cv2
import zmq
import base64 
import time

IP = '192.168.1.254'

cap = cv2.VideoCapture(10)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))

context = zmq.Context()
footage_socket=context.socket(zmq.PAIR)
footage_socket.connect('tcp://%s:5555'%IP)
print(IP)
 
while True:
 
    time_temp=time.time()
 
    ret,frame = cap.read()
    
    encoded,buffer = cv2.imencode('.jpg',frame);
    
    jpg_as_text=base64.b64encode(buffer)
    
    #print(jpg_as_text)

    footage_socket.send(jpg_as_text)
    #cv2.imshow("test", frame)
    
    time_per=time.time()-time_temp
 
    print("FPS:",1/time_per)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()

