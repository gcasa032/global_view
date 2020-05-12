from flask import Flask, render_template, url_for, Response
from flask_mysqldb import MySQL
import MySQLdb.cursors
import cv2
from Camera.camera import camera

app = Flask(__name__)

app.secret_key = 'admin'

# Database connection details
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

# initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    cur = mysql.connection.cursor()
    resultsValue = cur.execute("SELECT * FROM locations")
    if resultsValue > 0:
        vidDetails = cur.fetchall()
        return render_template('front_page.html', vidDetails=vidDetails)

    return "ERROR: No data was found"

@app.route('/video/<int:id>', methods=['GET'])
def video(id):

    cur = mysql.connection.cursor()
    resultsValue = cur.execute("SELECT * FROM locations WHERE id=" + str(id))
    if resultsValue > 0:
        location = cur.fetchone()
        id = location[0]
        nextId = getNext(id)
        prevId = getPrev(id)
        return render_template('video_page.html', location=location, nextId=nextId, prevId=prevId)

@app.route('/renderCamera/<path:url>', methods=['GET'])
def renderCamera(url):
    thisCamera = camera(url)
    return Response(generate_video(thisCamera), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_video(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def getNext(id:int):
    lastRowId = getLast()

    if id == lastRowId:
        return 1
    else:
        return (id+1)


def getPrev(id:int):
    lastRowId = getLast()

    if id == 1:
        return lastRowId
    else:
        return (id-1)

def getLast() -> int:
    cur = mysql.connection.cursor()
    query = cur.execute("SELECT id FROM locations WHERE id=(SELECT MAX(id) FROM locations);")
    lastRow = cur.fetchone()
    return lastRow[0]


if __name__ == '__main__':
    app.run()