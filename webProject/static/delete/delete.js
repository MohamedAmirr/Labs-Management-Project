window.addEventListener("scroll", function () {
    const header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0)
})


function getConfirmation() {
    event.preventDefault();
    let retVal = confirm("Do you want to continue ?");
    if (retVal) {
        location.replace("../../home") ;
        alert("Laboratory successfully deleted");
        return true;
    } else {
        alert("Action Canceled");
        return false;
    }
}