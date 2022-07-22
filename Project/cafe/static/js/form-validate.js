function validate(){
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const mobile = document.getElementById("mobile").value;
    const sugg = document.getElementById("suggestion").value;
    let error = false;
    console.log('Connecting...')
    //name
    if(name == ""){
        document.getElementById("name_error").innerHTML = "Name is required!";
        error = true;
    }
    else{
        document.getElementById("name_error").innerHTML = "";
    }

    //mobile
    if(mobile == ""){
        document.getElementById("mobile_error").innerHTML = "Mobile number is required!";
        error= true;
    }
    else if(mobile.length != 10 || isNaN(mobile)){
        document.getElementById("mobile_error").innerHTML = "Please enter a 10-digit valid number!";
        error= true;
    }
    else{
        document.getElementById("mobile_error").innerHTML = "";
    }

    //email
    let atPos = email.indexOf('@');
    let dotPos = email.lastIndexOf('.');
    if(email==""){
        document.getElementById("email_error").innerHTML = "Email is required!";
        error = true;
    }
    else if(atPos <= 0 || dotPos <= 0 || (dotPos - atPos) <= 4 || dotPos == email.length - 1 ){
        document.getElementById("email_error").innerHTML = "Please provide a valid email!";
        error = true;
    }
    else{
        document.getElementById("email_error").innerHTML = "";
    }

    //suggestion
    if(sugg == ""){
        document.getElementById("submit_error").innerHTML = "Suggestion is required!";
        error = true;
    }
    else{
        document.getElementById("submit_error").innerHTML = "";
    }
    if(error){
        return false;
    }
    else{
        return true;
    }
}