from flask import Flask
import motors as motors
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route("/test")
def test():
    motors.test_motors()

    templateData = {
      'title' : 'Test Motors',
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)

@app.route("/reset")
def reset():
    motors.reset()

    templateData = {
      'title' : 'Reset',
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)

@app.route("/left/<delay>/<throttle>")
def left(delay, throttle):
    motors.left_motors(delay, throttle)

    templateData = {
      'title' : 'Left motors ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)

@app.route("/right/<delay>/<throttle>")
def right(delay, throttle):
    motors.right_motors(delay, throttle)

    templateData = {
      'title' : 'Right motors ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)

@app.route("/forward/<delay>/<throttle>")
def forward(delay, throttle):
    motors.forward(delay, throttle)

    templateData = {
      'title' : 'Forward ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)

@app.route("/backward/<delay>/<throttle>")
def backward(delay, throttle):
    motors.backward(delay, throttle)

    templateData = {
      'title' : 'Backward ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)

@app.route("/ccw/<delay>/<throttle>")
def turn_CCW(delay, throttle):
    motors.turn_CCW(delay, throttle)

    templateData = {
      'title' : 'Turn CCW ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)

@app.route("/cw/<delay>/<throttle>")
def turn_CW(delay, throttle):
    motors.turn_CW(delay, throttle)

    templateData = {
      'title' : 'Turn CW ' + delay + ' ' + throttle,
      'response' : ':0'
      }

    return render_template('cmd.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
