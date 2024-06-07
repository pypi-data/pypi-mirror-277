import concurrent.futures
import time

from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from loguru import logger

from configuration import lstr_host_ip, lint_host_port, lint_max_workers, lstr_log_path, lstr_log_file_name

"""Initialize the log path"""
logger.add(f"{str(lstr_log_path)}{str(lstr_log_file_name)}.log")

"""Create a Flask application instance"""
app = Flask(__name__)

"""Bind Socket.IO to the Flask application"""
socketio = SocketIO(app)

"""ThreadPoolExecutor with maximum number of workers"""
executor = concurrent.futures.ThreadPoolExecutor(max_workers=lint_max_workers)


@app.route('/')
def index():
    """
    Description: This function loads the index.html page.
    """
    try:
        """Render the HTML template for the index page"""
        return render_template("index.html")
    except Exception as exception:
        logger.exception(f"Exception - {str(exception)}")


@app.route("/add_to_queue", methods=["POST"])
def add_to_queue():
    """
    Description: This function is used to add message to the queue, extract the required information and submit the
    task in the thread pool.
    """
    try:
        ldict_data = request.json
        lstr_message = ldict_data["message"]
        lint_delay_in_seconds = ldict_data["delay"]

        """Submit the task to the thread pool"""
        print(f"Message received - {str(lstr_message)}, delay in seconds - {str(lint_delay_in_seconds)}")
        logger.info(f"Message received - {str(lstr_message)}, delay in seconds - {str(lint_delay_in_seconds)}")
        executor.submit(process_message, lint_delay_in_seconds, lstr_message)
        return jsonify({"status": "queued",
                        "message": lstr_message,
                        "delay": lint_delay_in_seconds})
    except Exception as exception:
        logger.exception(f"Exception - {str(exception)}")


def process_message(pint_delay_in_seconds: int,
                    pstr_message: str):
    """
    Description: This function received the message, simulates the time and emits the message via socket.io

    :param pint_delay_in_seconds: delay given by the user.
    :param pstr_message: message typed by the user.
    """
    try:
        time.sleep(pint_delay_in_seconds)
        print(f"Processed message: {pstr_message}")
        logger.info(f"Processed message: {pstr_message}")
        with app.app_context():
            socketio.emit("new_message", {"message": pstr_message}, namespace="/")
    except Exception as exception:
        logger.exception(f"Exception - {str(exception)}")


@socketio.on("connect", namespace="/")
def test_connect():
    """
    Description: This function is a event handler for client connection.
    """
    try:
        print("Client connected")
        logger.info("Client connected")
    except Exception as exception:
        logger.exception(f"Exception - {str(exception)}")


if __name__ == "__main__":
    socketio.run(app, debug=True, host=lstr_host_ip, port=lint_host_port, allow_unsafe_werkzeug=True)
