from flask import Flask, render_template, redirect, url_for
from gpiozero import LED
from gpiozero.pins.lgpio import LGPIOFactory

factory = LGPIOFactory()

app = Flask(__name__)

led1 = LED(17, pin_factory=factory)
led2 = LED(27, pin_factory=factory)

led_states = {
    "led1": False,
    "led2": False
}

@app.route("/")
def index():
    return render_template("index.html", led_states=led_states)

@app.route("/toggle/<led>")
def toggle(led):
    if led == "led1":
        if led_states["led1"]:
            led1.off()
        else:
            led1.on()
        led_states["led1"] = not led_states["led1"]

    elif led == "led2":
        if led_states["led2"]:
            led2.off()
        else:
            led2.on()
        led_states["led2"] = not led_states["led2"]

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
