class WebSocketConnectionManager {
    #websocket;
    #handler;

    constructor(user_id=1) {
        let ws_url = `ws://${window.location.host}/ws/${user_id}`;
        this.#handler = new MessagesHandler();

        this.#websocket = new WebSocket(ws_url);

        this.#websocket.onmessage = (message) => {
            this.#handler.handleMessage(message);
        }
    }

    close = () => {
        this.#websocket.close()
    }
}


class MessagesHandler {
    handleMessage = function(message) {
        let data = JSON.parse(message.data);
        console.log(data.message);
    }
}


