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
    #input_field;
    #input_button;
    #messages_field;
    #clear_chat_button;
    #new_chat_button;
    #cancel_search_button;
    #close_chat_button;

    #messages_lst;
    #messageClass;

    #active_chat = false;
    #search_chat = false;

    constructor(messageClass, ws_connection) {

        this.#messageClass = messageClass;
        this.#messages_lst = [];

        this.ws_connection = ws_connection;

        this.#setDOMElements();
        this.#addListeners();
    }


    addMessage(text) {
        const chatMessage = this.#createChatMessage(text);
        const messageElement = new this.#messageClass(chatMessage);
        this.#messages_field.appendChild(messageElement.element);
        this.#messages_lst.push(chatMessage);
    }


    findChat() {
        this.#active_chat = false;
        this.#search_chat = true;
        this.#new_chat_button.className = 'menu_button_disabled';
        this.#close_chat_button.className = 'menu_button_disabled';
        this.#cancel_search_button.className = 'menu_button_enabled';
        this.#input_button.className = 'input_button_disabled'
    }

    startChat() {
        this.#active_chat = true;
        this.#search_chat = false;
        this.#new_chat_button.className = 'menu_button_disabled';
        this.#close_chat_button.className = 'menu_button_enabled';
        this.#cancel_search_button.className = 'menu_button_disabled';
        this.#input_button.className = 'input_button_enabled'
    }

    cancelSearch() {
        this.#active_chat = false;
        this.#search_chat = false;
        this.#new_chat_button.className = 'menu_button_enabled';
        this.#cancel_search_button.className = 'menu_button_disabled';
        this.#close_chat_button.className = 'menu_button_disabled';
        this.#input_button.className = 'input_button_disabled'
    }

    closeChat() {
        this.#active_chat = false;
        this.#search_chat = false;
        this.#new_chat_button.className = 'menu_button_enabled';
        this.#cancel_search_button.className = 'menu_button_disabled';
        this.#close_chat_button.className = 'menu_button_disabled';
        this.#input_button.className = 'input_button_disabled'
    }


    #createChatMessage(text) {
        return `${this.#getCurrentTime()} ${text}`
    }


    #clearChatField() {
        this.#messages_field.innerHTML = '';
    }


    #clearInputField() {
        this.#input_field.value = '';
    }


    #sendData(data) {
        this.ws_connection.sendJSON(data);
    }


    #sendChatMessage(text) {
        const data = {
            type: 'chat_message',
            message: text
        }
        this.#sendData(data);
    }


    #find_chat() {
        const data = {
            type: 'find_chat'
        }
        this.#sendData(data);
    }


    #cancel_search() {
        const data = {
            type: 'cancel_search'
        }
        this.#sendData(data);
    }


    #close_chat() {
        const data = {
            type: 'close_chat'
        }
        this.#sendData(data);
    }


    #setDOMElements = () => {
        this.#input_field = window.document.querySelector('#input_field');
        this.#input_button = window.document.querySelector('#input_button');
        this.#messages_field = window.document.querySelector('#messages');
        this.#clear_chat_button = window.document.querySelector('#clear_chat');
        this.#new_chat_button = window.document.querySelector('#new_chat');
        this.#cancel_search_button = window.document.querySelector('#cancel_search');
        this.#close_chat_button = window.document.querySelector('#close_chat');
    }


    #addListeners = () => {
        this.#input_button.addEventListener('click', (event) => {
            const text = this.#input_field.value;
            if (text) {
                this.#sendChatMessage(text);
                this.#clearInputField();
                }
            })

        this.#clear_chat_button.addEventListener('click', (event) => this.#clearChatField());

        this.#new_chat_button.addEventListener('click', (event) => {
            if (!this.#active_chat)
                this.#find_chat();
        })

        this.#cancel_search_button.addEventListener('click', (event) => {
            if (this.#search_chat)
                this.#cancel_search();
        })

        this.#close_chat_button.addEventListener('click', (event) => {
            if (this.#active_chat)
                this.#close_chat();
        })

    }


    #getCurrentTime() {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');

        return `[ ${hours}:${minutes}:${seconds} ]`;
    }
}
