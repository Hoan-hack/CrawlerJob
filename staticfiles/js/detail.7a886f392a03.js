function createElementFromHTML() {
    return document.getElementsByClassName('content')[0].innerHTML;
}

function addElement() {
    var element = createElementFromHTML();
    document.getElementsByClassName('content-vew')[0].innerHTML = element.replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">");
}
addElement();