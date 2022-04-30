const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});
signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
window.addEventListener("scroll",function(){
	var header = document.querySelector("header");
	header.classList.toggle("sticky",window.scrollY > 0)
})
