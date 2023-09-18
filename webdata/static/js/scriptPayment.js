const buttonPay = document.getElementById("buttonPay")
const inputAgreement = document.getElementById("inputAgreement")
const divError = document.getElementById("divError")

const asynchronous = document.getElementById("asynchronous")

buttonRegister.addEventListener("click", (event)=>{
    event.preventDefault()

    var errorText = ""

    const agreement = inputAgreement.checked
    if(!agreement){
        errorText = "Please tick the terms and conditions checkbox!"
    }

    divError.innerHTML = errorText
    divError.style.display = 'block';
})