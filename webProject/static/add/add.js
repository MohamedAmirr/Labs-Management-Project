window.addEventListener("scroll", function () {
    const header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0)
})


let adding = document.getElementById('addItem');

function dia() {
    alert("Laboratory has been added successfully");

}

adding.onclick = function () {
    dia();

}
