import cv2, imutils

class camera(object):

    frame_counter = 0

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)

    def __del__(self):
        self.video.release()        

    def get_frame(self):


        ret, frame = self.video.read()
        if ret:
            assert not isinstance(frame,type(None)), 'frame not found'

        frame = imutils.resize(frame, width=500)

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

        ret, jpeg = cv2.imencode('.jpg', frame)   

        return jpeg.tobytes()