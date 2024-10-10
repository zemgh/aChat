const MESSAGE_CLASS = Message;

function init() {
    const ws_connection = new WebSocketConnectionManager();
    const chat = new Chat(MESSAGE_CLASS, ws_connection);
    const messages_handler = new WebSocketMessagesHandler(chat);

    ws_connection.addHandler(messages_handler);
}

document.addEventListener("DOMContentLoaded", init);