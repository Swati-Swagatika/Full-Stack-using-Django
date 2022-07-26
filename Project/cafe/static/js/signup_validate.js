function validate(){
    const fname = document.getElementById("first_name").value;
    const lname = document.getElementById("last_name").value;
    const email = document.getElementById("email").value;
    const sicnumber = document.getElementById('username').value;
    const password = document.getElementById("password").value;
    const confirm_password = document.getElementById("confirm_password").value;
    let error = false;
    console.log('Connecting...')
    //name
    if(fname == ""){
        document.getElementById("fname_error").innerHTML = "Name is required!";
        error = true;
    }
    else{
        document.getElementById("fname_error").innerHTML = "";
    }

    //last name
    if(lname == ""){
        document.getElementById("lname_error").innerHTML = "Name is required!";
        error = true;
    }
    else{
        document.getElementById("lname_error").innerHTML = "";
    }

    //sic number
    if (sicnumber == ""){
        document.getElementById("sic_error").innerHTML = "SIC is required!"
        error = true;
    }
    else if(sicnumber.length != 9){
        document.getElementById("sic_error").innerHTML = "SIC must be of 9 numbers"
        error = true;
    }
    else{
        document.getElementById("sic_error").innerHTML = "";
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


    //password
    if (password == ""){
        document.getElementById("password_error").innerHTML = "password is required!";
        error = true;
    }
    else if(password.length < 8 || password.length > 16){
        document.getElementById("password_error").innerHTML = "Password must be 8 - 16 character long!";
        error = true;
    }
    else if(!password.match(/[a-z]/)){
        document.getElementById("password_error").innerHTML = "Password must be contain a lowercase character!";
        error = true;
    }
    else if(!password.match(/[A-Z]/)){
        document.getElementById("password_error").innerHTML = "Password must be contain a uppercase character!";
        error = true;
    }
    else if(!password.match(/[0-9]/)){
        document.getElementById("password_error").innerHTML = "Password must be contain a number!";
        error = true;
    }
    else if(!password.match(/[!@#$%^&*]/)){
        document.getElementById("password_error").innerHTML = "Password must be contain a special character!";
        error = true;
    }
    else{
        document.getElementById("password_error").innerHTML = "";
    }

    //confirm password
    if (confirm_password == ""){
        document.getElementById("confirm_password_error").innerHTML = "Confirm password is required!";
        error = true;
    }
    else if(password != confirm_password){
        document.getElementById("confirm_password_error").innerHTML = "Confirm Password and Password must be same";
        error = true;
    }
    else{
        document.getElementById("confirm_password_error").innerHTML = "";
    }

    if(error){
        return false;
    }
    else{
        return true;
    }
}