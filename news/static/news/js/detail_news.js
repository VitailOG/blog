function Comment(a, b) {
    document.getElementById("parent-id").value = b;
    document.getElementById("text_comment").innerText = `${a}, `;
}

function actionButton(a) {
    let e = document.getElementsByClassName("row-action");
    for (var i = 0; i < e.length; i++) e[i].style.display = a;
}

function closeAction(a) {
    let e = document.getElementsByClassName("row-action");
    for (var i = 0; i < e.length; i++) e[i].style.display = a;
}

function moreText(a, b, c) {
    let text = document.getElementById(a);
    let button = document.getElementById(b);
    if (button.innerText === "Більше") {
        text.innerText = c;
        button.innerText = 'Приховати';
    }else if (button.innerText === "Приховати") {
        text.innerText = c.slice(0, 100);
        button.innerText = 'Більше';
    }
}


