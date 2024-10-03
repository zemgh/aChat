class WebSocketConnectionManager {
    #websocket;
    #handler;

    constructor(handler, user_id=1) {
        this.#handler = handler;

        const ws_url = `ws://${window.location.host}/ws/${user_id}`;
        this.#websocket = new WebSocket(ws_url);

        window.addEventListener('beforeunload', () => this.#close());

        this.#websocket.onmessage = (message) => this.#handler.handleMessage(message);
    }

    send(message) {
        const json_data = JSON.stringify(message);
        this.#websocket.send(json_data);
    }

    #close = () => {
        this.#websocket.close()
    }
}


class WebSocketMessagesHandler {
    #chat

    constructor(chat) {
        this.#chat = chat;
    }

    handleMessage(json_data) {
        const data = JSON.parse(json_data.data);
        console.log(data);

        switch (data.type) {
            case 'chat_message':
                this.#addChatMessage(data.text);
                console.log('text:', data.text)
                break;
            default:
                console.log('no text');

        }
    }

    #addChatMessage(text) {
        this.#chat.addMessage(text);
    }
}
