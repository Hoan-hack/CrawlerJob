console.log('document.location', document.location.href);
console.log('location.pathname',  window.location.pathname);// Returns path only
console.log('location.href', window.location.href);
console.log('location.href_test', window.location.href.substr(-7, 7));
function get_current_page() {
    return document.getElementsByClassName("pagina-current-page")[0].innerHTML;
}

function display_pagination() {
    var current_page = get_current_page();
    var display_a = document.getElementsByClassName("pagina-current-page")[0];
    var display_next_dot = document.getElementsByClassName('next_dot')[0];
    var display_pagina_page_next = document.getElementsByClassName('pagina-page-next')[0];

    if (document.getElementsByClassName("pagina-next")[0].getAttribute("href") === 'None'){
        document.getElementsByClassName("pagina-next")[0].setAttribute("href", display_a);
    }
    if (parseInt(display_a.innerHTML) === 1){
        document.getElementsByClassName("pagina-prev")[0].setAttribute("href", display_a);
    }
    if (current_page <= 3){
        display_a.style.display = 'none';
        display_next_dot.style.display = 'none';
        display_pagina_page_next.style.display = 'none';
    }
    else if (current_page === 4) {
        display_a.style.display = 'block';
        display_next_dot.style.display = 'none';
        display_pagina_page_next.style.display = 'none';
    }
    else{
        display_a.style.display = 'none';
        display_next_dot.style.display = 'block';
        display_pagina_page_next.innerHTML = current_page;
        display_pagina_page_next.style.display = 'block';
    }
}
display_pagination();

// function getRandomColor() {
//   var letters = '0123456789ABCDEF';
//   var color = '#';
//   for (var i = 0; i < 6; i++) {
//     color += letters[Math.floor(Math.random() * 16)];
//   }
//   return color;
// }
//
// function setRandomColor() {
//     var a = document.getElementById("colorpad");
//     a.setAttribute("style", "background:" + getRandomColor()+ ";");
// }
// setRandomColor();