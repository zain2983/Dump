import streamlit as st # type: ignore
from streamlit.components.v1 import html # type: ignore

def main():
    st.title("Simple Speech Recognition")
    st.write("Click 'Start' and begin speaking. Your speech will be transcribed below.")

    html_code = """
    <div>
        <button onclick="startRecognition()">Start</button>
        <button onclick="stopRecognition()">Stop</button>
        <p id="output"></p>
    </div>

    <script>
    let recognition;

    function startRecognition() {
        if ('webkitSpeechRecognition' in window) {
            recognition = new webkitSpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = true;

            recognition.onresult = function(event) {
                let transcript = Array.from(event.results)
                    .map(result => result[0].transcript)
                    .join('');
                document.getElementById('output').textContent = transcript;
            };

            recognition.onerror = function(event) {
                console.error('Error:', event.error);
            };

            recognition.start();
        } else {
            alert('Speech recognition is not supported in this browser.');
        }
    }

    function stopRecognition() {
        if (recognition) {
            recognition.stop();
        }
    }
    </script>
    """

    html(html_code, height=300)

if __name__ == "__main__":
    main()