import cv2, os, time
# open stream
cap = cv2.VideoCapture('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov')
# (rtsp://ness:ILoveNESS2020@79.143.34.244:554/Streaming/Channels/1601) - not working
# print(cap.get(3))
# print(cap.get(4))

# read stream
while(cap.isOpened()):
    cv2.waitKey(10)

    ret, frame = cap.read()
    # set dimention
    cap.set(3,cap.get(3));
    cap.set(4,cap.get(4));

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    # comment this for You not see picture in window
    cv2.imshow('frame',gray)
    cv2.resizeWindow('frame', int(cap.get(3)), int(cap.get(4)))
    # set file path
    dirname = 'd:\\Projects\\test_rtcp\\test_kness\\static'
    cv2.imwrite(os.path.join(dirname,'screen.png'), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# cap.set(3, 5500)
# cap.set(4, 6000)
# # Default resolutions of the frame are obtained (system dependent)
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))

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

# while(cap.isOpened()):
#     cv2.waitKey(10)
#
#     ret, frame = cap.read()
#     cap.set(3, 800)
#     cap.set(4, 600)
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
#     cap.get(3)  # return default 1280
#
#     cv2.imshow('frame', gray)
#     cv2.resizeWindow('frame', 1600, 1200)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     # cap.set(3, 5500)
#     # ret, frame = cap.read()
#     #
#     # if not ret:
#     #
#     #     break
#     # else:
#     #
#     #
#     #     cv2.imshow('frame', frame)
#     #     #The received "frame" will be saved. Or you can manipulate "frame" as per your needs.
#     #     # name = "rec_frame"+str(count)+".jpg"
#     #     dirname = 'd:\\Projects\\test_rtcp\\browser_rtcp\\static'
#     #     cv2.imwrite(os.path.join(dirname,'huinya.png'), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
#     #     time.sleep(1)
#     #     # count += 1
#     # if cv2.waitKey(20) & 0xFF == ord('q'):
#     #     break
#
# cap.release()
# cv2.destroyAllWindows()
