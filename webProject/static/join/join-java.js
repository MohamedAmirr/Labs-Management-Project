const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');


signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});
signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

function verifyPass() {
    const pass = document.getElementById("pass1");
    if (pass.value === "") {
        document.getElementById("message").innerHTML = "Enter Password please!";
        event.preventDefault();
        return false;
    } else if (pass.value.length < 8) {
        document.getElementById("message").innerHTML = "Password length must be at least 8 characters";
        event.preventDefault();
        return false;
    } else {
        const pass1 = document.getElementById("pass2");
        if (pass.value !== pass1.value) {
            document.getElementById("message").innerHTML = "Please write a correct confirmation password";
            event.preventDefault();
        }
    }

}

