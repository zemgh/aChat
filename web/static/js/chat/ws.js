class WebSocketConnectionManager {
    #websocket;
    #handler;

    constructor(user_id=1) {
        const ws_url = `ws://${window.location.host}/ws/${user_id}`;
        this.#websocket = new WebSocket(ws_url);

        window.addEventListener('beforeunload', () => this.#close());

        this.#websocket.onmessage = (message) => this.#handler.handleMessage(message);
    }

    sendJSON(data) {
        const json_data = JSON.stringify(data);
        console.log('sent:', data);
        this.#websocket.send(json_data);
    }

    addHandler(handler) {
        this.#handler = handler;
    }

    #close = () => {
        this.#websocket.close();
    }
}


class WebSocketMessagesHandler {
    #chat;

    constructor(chat) {
        this.#chat = chat;
    }

    handleMessage(json_data) {
        const data = JSON.parse(json_data.data);
        console.log('received:', data);

        switch (data.type) {
            case 'chat_message':
                this.#chat.addMessage(data.message); break;

            case 'new_chat':
                this.#chat.startChat(); break;

            case 'find_chat':
                this.#chat.findChat(); break;

            case 'cancel_search':
                this.#chat.cancelSearch(); break;

            case 'close_chat':
                this.#chat.closeChat(); break;

        }
    }
}
