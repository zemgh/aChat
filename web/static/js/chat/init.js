function init() {
    const chatElement = document.querySelector('#messages');
    const chat = new Chat(chatElement, Message);

    const messages_handler = new WebSocketMessagesHandler(chat);
    const connection = new WebSocketConnectionManager(messages_handler);
}

document.addEventListener("DOMContentLoaded", init);