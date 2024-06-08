# delayed_queue_manager

## About

- Queue Functionality:

    - Allow items to be added to the queue with a delay (in seconds).
    - Items should only become available after the specified delay.

- User Interface:
    - Develop a simple UI using HTML and JavaScript.
    - The UI should allow users to submit a text string and delay time.
    - On clicking "Run", the app should display the queued items automatically after their respective delays by polling
      the backend.

## Ready to use docker

- Make sure you have docker installed on your machine.
- Follow the steps [here](https://docs.docker.com/engine/install/) for more details on docker installation.
- Follow the below steps after successful installation of docker

```sh
docker compose up
```

- Now you can access the application at `http://localhost:50300/`

## Installation

```sh
pip install delayed_queue_manager
```

## ChangeLog

### v1.1.1

```text
1. Dependencies updated in setup.py.
```

### v1.1.0

```text
1. Queue data structure implemented for storing the queue messages.
2. MAX_WORKERS configuration removed from the config.ini.
3. DEBUG_MODE is now being used in the main code.
```

### v1.0.0

```text
1. Allow messages to be added to the queue with a delay (in seconds).
2. Messages are available after the specified delay.
```
