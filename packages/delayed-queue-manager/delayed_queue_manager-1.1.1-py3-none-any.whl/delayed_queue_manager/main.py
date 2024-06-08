import queue
import threading
import time

from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from loguru import logger

from configuration import lstr_host_ip, lint_host_port, lstr_log_path, lstr_log_file_name, lbool_debug_mode

"""Initialize the log path"""
logger.add(f"{str(lstr_log_path)}{str(lstr_log_file_name)}.log")

"""Create a Flask application instance"""
app = Flask(__name__)

"""Bind Socket.IO to the Flask application"""
socketio = SocketIO(app)

# Create a queue to hold messages and their delays
message_queue = queue.Queue()


@app.route('/')
def index():
    """
    Description: This function loads the index.html page.
    """
    try:
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

        """Submit the task to the queue"""
        print(f"Message received - {str(lstr_message)}, delay in seconds - {str(lint_delay_in_seconds)}")
        logger.info(f"Message received - {str(lstr_message)}, delay in seconds - {str(lint_delay_in_seconds)}")
        message_queue.put((lstr_message, lint_delay_in_seconds))
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
        with app.app_context():
            socketio.emit("new_message", {"message": pstr_message}, namespace="/")
        print(f"Processed message: {pstr_message}")
        logger.info(f"Processed message: {pstr_message}")
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


def process_queue():
    """
    Description: This function continuously processes messages from the queue.
    """
    while True:
        message, delay = message_queue.get()
        if message is None:
            break
        threading.Thread(target=process_message, args=(delay, message)).start()
        message_queue.task_done()


"""Start the queue processing thread"""
queue_thread = threading.Thread(target=process_queue)
queue_thread.start()

if __name__ == "__main__":
    try:
        socketio.run(app, debug=lbool_debug_mode, host=lstr_host_ip, port=lint_host_port, allow_unsafe_werkzeug=True)
    finally:
        """Signal the queue processing thread to exit"""
        message_queue.put((None, 0))
        queue_thread.join()
