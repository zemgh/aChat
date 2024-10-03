class Message {
    element;
    text;

    constructor(text) {
        this.element = window.baseMessageElement.cloneNode(true);
        this.element.textContent = text;
        this.text = text;
    }
}


class Chat {
    #node;
    #messages;
    #messageClass

    constructor(node, messageClass) {
        this.#node = node;
        this.#messageClass = messageClass
        this.#messages = [];
    }

    addMessage(text) {
        const chatMessage = this.#createChatMessage(text);
        const messageElement = new this.#messageClass(chatMessage);
        this.#node.appendChild(messageElement.element);
        this.#messages.push(chatMessage);
    }

    clear () {
        this.#node.innerHTML = '';
        this.#messages = []
    }

    #createChatMessage(text) {
        return `${this.#getCurrentTime()} ${text}`
    }

    #getCurrentTime() {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');

        return `[ ${hours}:${minutes}:${seconds} ]`;
    }
}
