"""
Module for capturing video from a camera device using OpenCV.

This module creates a unique class, CameraStream, which encapsulates the connection to a video source (Webcam or IP Camera on RTSP).
The rest of the project (AI Pipeline,  zone manager, ect.) will use this class to get frames from the camera. 
"""

import cv2 
class CameraStream:
    """
    Represents a video source

    Attriutes:
    source: int or srt
    0 for local webcam 
    RSTP URL (ex: "rstp://192.168.1.64.554:stream1") For IP camera.
    """

    def __init__(self, source):
        self.source = source
        self.capture = cv2.VideoCapture(source)

        if not self.capture.isOpened():
            raise RuntimeError(f"Impossible d'ouvrir la source vidéo : {source}")

    def read_frame(self):
        """
        Reads a frame from the video source.

        Returns:
            frame: The captured frame as a NumPy array.
        """
        succes, frame = self.capture.read()
        if not succes:
            return None
        return frame

    def release(self):
        """
        Releases the video source.
        """
        self.capture.release()

if __name__ == "__main__":
    cam = CameraStream(0)  # 0 for local webcam
    while True:
        frame = cam.read_frame()

        if frame is None:
            break
        cv2.imshow("Test Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

        