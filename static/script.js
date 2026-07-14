document.getElementById("sendBtn").onclick = sendMessage;

document.getElementById("userInput").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    let userInput = document.getElementById("userInput");
    let userText = userInput.value.trim();

    if (userText === "") return;

    let chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `<div class="user-msg">You: ${userText}</div>`;

    userInput.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    let formData = new FormData();
    formData.append("msg", userText);

    fetch("/get", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        chatbox.innerHTML += `<div class="bot-msg">Bot: ${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;

    });
}