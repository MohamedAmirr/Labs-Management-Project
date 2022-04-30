window.addEventListener("scroll",function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky",window.scrollY > 0)
})

const box = document.getElementById('Box');
const idLap = document.getElementById('ID');
const numPc = document.getElementById('num_pc');
const datee = document.getElementById('date');

box.addEventListener('submit' , e => {
    e.preventDefault();
    validateInputs();
})

const setError = (element , message) => {
    const inputControl = element.parentElement;
    const errordisplay = inputControl.querySelector('.error');

    errordisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
}

const setSuccess = element => {
    const inputcontrol = element.parentElement;
    const errordisplay = inputcontrol.querySelector('.error');

    errordisplay.innerText = '';
    inputcontrol.classList.add('success');
    inputcontrol.classList.remove('error');
}

const validateInputs = () => {
    const idvalue = idLap.value.trim();
    const numpcvalue = numPc.value.trim();
    const date = datee.value.trim();

    if (idvalue => 1 && idvalue <= 50){
        setSuccess(idlap);
        alert("success");
    }
    else {
        setError(idLap , 'id is required');
        alert("error");
    }
    if (numpcvalue => 1 && numpcvalue <= 50){
        setSuccess(numPc);
        alert("success");

    }
    else {
        setError(numPc , 'num of pc is required');
        alert("error");
    }
}