window.baseMessageElement = createBaseMessageElement();

function createBaseMessageElement() {
    const div = document.createElement('div');
    div.className = 'message';
    return div;
}