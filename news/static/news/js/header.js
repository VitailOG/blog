document.getElementById("bg").onclick = function () {
    open()
};

function open() {
    document.getElementById("nms").classList.toggle("active");
    document.getElementById("bg").classList.toggle("show");
    document.getElementById("body").classList.toggle("lock");
}