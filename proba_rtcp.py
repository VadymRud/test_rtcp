import cv2, os, time
cap = cv2.VideoCapture('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov')

# Default resolutions of the frame are obtained (system dependent)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# count = 0
#
# cap.set(cv2.CAP_PROP_BUFFERSIZE, 1); # Where frame_no is the frame you want
# ret, frame = cap.read() # Read the frame
# cv2.imshow('window_name', frame) # show frame on window
# cv2.waitKey()
# cap.set(2, 6)
# # print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
# ret, img = cap.read()
# # cv2.imshow('window_name', img)
# cv2.imwrite('last_frame.jpg', img)
while(cap.isOpened()):

    ret, frame = cap.read()
    if not ret:

        break
    else:
        # cv2.imshow('frame', frame)
        #The received "frame" will be saved. Or you can manipulate "frame" as per your needs.
        # name = "rec_frame"+str(count)+".jpg"
        dirname = 'd:\__TEMP__\__temp'
        cv2.imwrite('img_temp.png', frame)
        time.sleep(3)
        # count += 1
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
