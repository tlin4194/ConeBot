from flask import Flask, jsonify
import motors as motors
import datetime


app = Flask(__name__)

@app.route("/")
def hello(methods=['GET']):
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return jsonify(templateData)

@app.route("/test")
def test(methods=['GET']):
    motors.test_motors()

    templateData = {
      'title' : 'Test Motors',
      'response' : ':0'
      }

    return jsonify(templateData)

@app.route("/reset")
def reset(methods=['GET']):
    motors.reset()

    templateData = {
      'title' : 'Reset',
      'response' : ':0'
      }

    return jsonify(templateData)

@app.route("/left/<delay>/<throttle>")
def left(delay, throttle, methods=['GET']):
    motors.left_motors(delay, throttle)

    templateData = {
      'title' : 'Left motors ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return jsonify(templateData)

@app.route("/right/<delay>/<throttle>")
def right(delay, throttle, methods=['GET']):
    motors.right_motors(delay, throttle)

    templateData = {
      'title' : 'Right motors ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return jsonify(templateData)

@app.route("/forward/<delay>/<throttle>")
def forward(delay, throttle, methods=['GET']):
    motors.forward(delay, throttle)

    templateData = {
      'title' : 'Forward ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return jsonify(templateData)

@app.route("/backward/<delay>/<throttle>")
def backward(delay, throttle, methods=['GET']):
    motors.backward(delay, throttle)

    templateData = {
      'title' : 'Backward ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return jsonify(templateData)

@app.route("/ccw/<delay>/<throttle>")
def turn_CCW(delay, throttle, methods=['GET']):
    motors.turn_CCW(delay, throttle)

    templateData = {
      'title' : 'Turn CCW ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return jsonify(templateData)

@app.route("/cw/<delay>/<throttle>")
def turn_CW(delay, throttle, methods=['GET']):
    motors.turn_CW(delay, throttle)

    templateData = {
      'title' : 'Turn CW ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return jsonify(templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
