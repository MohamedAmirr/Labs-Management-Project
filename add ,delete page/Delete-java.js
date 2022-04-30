window.addEventListener("scroll",function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY > 0)
})
let isExecuted = confirm("Are you sure to execute this action?");

console.log(isExecuted); // OK = true, Cancel = false
if (isExecuted) {
    // if true
    alert("Action successfully executed");
} else {
    // if false
    alert("Action canceled");
}