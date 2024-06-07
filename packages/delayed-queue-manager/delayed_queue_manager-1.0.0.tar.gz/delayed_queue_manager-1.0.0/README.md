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

## Installation

```sh
pip install delayed_queue_manager
```

## ChangeLog

### v1.0.0

1. Allow messages to be added to the queue with a delay (in seconds).
2. Messages are available after the specified delay.