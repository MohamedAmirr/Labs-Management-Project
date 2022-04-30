window.addEventListener("scroll",function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY > 0)
})
function getConfirmation() {
    var retVal = confirm("Do you want to continue ?");
    if( retVal == true ) {
        alert("Laboratory successfully deleted");
        return true;
    } else {
        alert("Action Canceled");
        return false;
    }
}