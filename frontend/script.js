document.getElementById('startButton').addEventListener('click', function() {
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'en-US'; // Set the language
        recognition.interimResults = false;

        recognition.start();
        recognition.onstart = function() {
            document.getElementById('formOutput').style.display = 'block';
            document.getElementById('formOutput').innerHTML = '<p>Listening...</p>';
        };

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            document.getElementById('formOutput').innerHTML = `<p>You said: ${transcript}</p>`;
        };

        recognition.onerror = function(event) {
            document.getElementById('formOutput').innerHTML = `<p>Error occurred: ${event.error}</p>`;
        };

        recognition.onend = function() {
            document.getElementById('formOutput').innerHTML += '<p>Listening stopped.</p>';
        };
    } else {
        alert('Speech recognition not supported in this browser.');
    }
});
