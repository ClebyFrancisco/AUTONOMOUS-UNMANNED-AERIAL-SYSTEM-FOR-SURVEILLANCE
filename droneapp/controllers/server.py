import logging
import uuid

from flask import jsonify
from flask import render_template
from flask import request
from flask import Response

from droneapp.models.drone_manager import DroneManager

import config


logger = logging.getLogger(__name__)
app = config.app


def get_drone():
    return DroneManager()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/controller/")
def controller():
    return render_template("controller.html")


@app.route("/api/command/", methods=["POST"])
def command():
    cmd = request.form.get("command")
    logger.info({"action": "command", "cmd": cmd})
    drone = get_drone()
    if cmd == "takeOff":
        drone.takeoff()
    if cmd == "land":
        drone.land()
    if cmd == "speed":
        speed = request.form.get("speed")
        logger.info({"action": "command", "cmd": cmd, "speed": speed})
        if speed:
            drone.set_speed(int(speed))

    if cmd == "up":
        drone.up()
    if cmd == "down":
        drone.down()
    if cmd == "forward":
        drone.forward()
    if cmd == "back":
        drone.back()
    if cmd == "clockwise":
        drone.clockwise()
    if cmd == "counterClockwise":
        drone.counter_clockwise()
    if cmd == "left":
        drone.left()
    if cmd == "right":
        drone.right()
    if cmd == "flipFront":
        drone.flip_front()
    if cmd == "flipBack":
        drone.flip_back()
    if cmd == "flipLeft":
        drone.flip_left()
    if cmd == "flipRight":
        drone.flip_right()
    if cmd == "patrol":
        drone.patrol()
    if cmd == "stopPatrol":
        drone.stop_patrol()
    if cmd == "squareFlight":
        drone.square_flight() 
    if cmd == "startRecording":
        start_recording()
    if cmd == "stopRecording":
        stop_recording()

    return jsonify(status="success"), 200


def video_generator():
    drone = get_drone()
    for jpeg in drone.video_jpeg_generator():
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + jpeg + b"\r\n\r\n")


@app.route("/video/streaming")
def video_feed():
    return Response(
        video_generator(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )
    
    
# @app.route("/start_recording", methods=["POST"])
def start_recording():
    vd_id = uuid.uuid4()
    print(f"vd_id: {vd_id}")
    
    drone = get_drone()
    output_file = request.form.get("output_file", f"{vd_id}.avi")
    drone.start_recording(output_file=output_file)
    return jsonify(status="recording_started", output_file=output_file), 200


# @app.route("/stop_recording", methods=["POST"])
def stop_recording():
    drone = get_drone()
    drone.stop_recording()
    return jsonify(status="recording_stopped"), 200



def run():
    app.run(host=config.WEB_ADDRESS, port=config.WEB_PORT, threaded=True)
