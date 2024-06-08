document.addEventListener('DOMContentLoaded', function () {
    // Establishing a connection to the server using Socket.IO
    const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Event listener for when the socket successfully connects to the server
    socket.on('connect', function () {
        console.log('Connected to server');
    });

    // Event listener for when a new message is received from the server
    socket.on('new_message', function (data) {
        console.log('Received new message:', data);
        // Creating a new HTML element to display the received message
        const item = document.createElement('div');
        item.className = 'alert alert-info mt-2';
        item.textContent = data.message;
        // Appending the new message element to the queue container
        document.getElementById('queue').appendChild(item);
    });
});

// Function to add a message to the queue
function addToQueue() {
    // Retrieving input elements
    const messageElement = document.getElementById('message');
    const delayElement = document.getElementById('delay');
    // Extracting values from input elements
    const message = messageElement.value;
    const delay = parseInt(delayElement.value);

    // Sending a POST request to add the message to the queue
    fetch('/add_to_queue', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        // Sending message and delay as JSON data in the request body
        body: JSON.stringify({ message: message, delay: delay })
    })
    // Handling the response from the server
    .then(response => response.json())
    .then(data => {
        console.log('Message added to queue:', data);
        // Clearing the input fields after successfully adding the message
        messageElement.value = '';
        delayElement.value = '';
    });
}