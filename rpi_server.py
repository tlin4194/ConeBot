from flask import Flask, jsonify, Response
import motors
import arm
import datetime
from camera import Camera

app = Flask(__name__, static_url_path='', static_folder='www')

@app.route("/")
def index(methods=['GET']):
    return app.send_static_file('index.html')

@app.route("/test")
def test(methods=['GET']):
    motors.test_motors()

    return jsonify({})

@app.route("/reset")
def reset(methods=['GET']):
    motors.reset_motors()

    return jsonify({})

@app.route("/teleop/<cmd>")
def teleop(cmd, methods=['GET']):
    if (cmd == 'fwd'):
        motors.tele_forward()
    if (cmd == 'bck'):
        motors.tele_backward()
    if (cmd == 'ccw'):
        motors.tele_turnCCW()
    if (cmd == 'cw'):
        motors.tele_turnCW()
    if (cmd == 'armup'):
        arm.arm_up()
    if (cmd == 'armdown'):
        arm.arm_down()
    if (cmd == 'armrelease'):
        arm.arm_release()

    return jsonify({})

@app.route("/left/<delay>/<throttle>")
def left(delay, throttle, methods=['GET']):
    delay = int(delay)
    throttle = int(throttle)
    motors.left_motors(delay, throttle)

    return jsonify({})

@app.route("/right/<delay>/<throttle>")
def right(delay, throttle, methods=['GET']):
    delay = int(delay)
    throttle = int(throttle)
    motors.right_motors(delay, throttle)

    return jsonify({})

@app.route("/forward/<delay>/<throttle>")
def forward(delay, throttle, methods=['GET']):
    delay = int(delay)
    throttle = int(throttle)
    motors.forward(delay, throttle)

    return jsonify({})

@app.route("/backward/<delay>/<throttle>")
def backward(delay, throttle, methods=['GET']):
    delay = int(delay)
    throttle = int(throttle)
    motors.backward(delay, throttle)

    return jsonify({})

@app.route("/ccw/<delay>/<throttle>")
def turn_CCW(delay, throttle, methods=['GET']):
    delay = int(delay)
    throttle = int(throttle)
    motors.turn_CCW(delay, throttle)

    return jsonify({})

@app.route("/cw/<delay>/<throttle>")
def turn_CW(delay, throttle, methods=['GET']):
    delay = int(delay)
    throttle = int(throttle)
    motors.turn_CW(delay, throttle)

    return jsonify({})

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video")
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
