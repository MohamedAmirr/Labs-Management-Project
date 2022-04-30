window.addEventListener("scroll",function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY > 0)
})
function dialogue(){
        alert("Laboratory has been added successfully");
}