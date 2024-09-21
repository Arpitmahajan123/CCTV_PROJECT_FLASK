from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)

# Creating Camera
# I Have 1 Webcam So I Select 0th Index
camera = cv2.VideoCapture(0)

# We Have Create A function Which Capture The Frames And Display It On Website 
def cctv_live():
    while True:
        # Read The Images From Our Camera And Store It On These Variables
        success,frame = camera.read()
        if not success:
            break
        else:
            # It Will Convert the JPG Into Frames...
            ret,buffer = cv2.imencode('.jpg', frame)
            # In Opencv We Pass Data In Byte Formats
            frame = buffer.tobytes()
            
        # Now Here, We Will Use The Function Which Helps To Refresh the Frames Every Seconds and Using it We Will Get All The Images In the Form Of video live stream on our website.

        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +frame+ b'\r\n')
        


@app.route('/')
def home():
    return render_template('pageone.html')

@app.route('/video')
def video():
    return Response(cctv_live(), mimetype='multipart/x-mixed-replace; boundary:frame')

if __name__ == "__main__":
    # If Debug Is Equal To True Then No Need Of Reloading...
    app.run(debug=True)










































