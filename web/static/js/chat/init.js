function init() {
    window.connection = new WebSocketConnectionManager();
    window.addEventListener('beforeunload', () => connection.close());
}

init();