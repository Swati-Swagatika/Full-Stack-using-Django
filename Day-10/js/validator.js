function validate(){
    const name = document.getElementById("name").value;
    const gender = document.getElementsByName("gender");
    const branch = document.getElementById("branch").value;
    const mobile = document.getElementById("mobile").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById('password').value;
    const password2 = document.getElementById("password2").value;
    const term = document.getElementById("term");

    let error = false;
    
    //Name
    if(name === ""){
        // console.log("Name is required!");
        document.getElementById("name_error").innerHTML = "Name is required!";
        error = true;
    }
    else{
        document.getElementById("name_error").innerHTML = "";
    }

    //Gender
    // console.log(gender)
    if(!gender[0].checked && !gender[1].checked && !gender[2].checked){
        document.getElementById("gender_error").innerHTML = "Gender is required!";
        error = true;
    }
    else{
        document.getElementById("gender_error").innerHTML = "";
    }

    //Branch
    if (branch == ""){
        document.getElementById("branch_error").innerHTML = "Select your Branch";
        error = true;
    }
    else{
        document.getElementById("branch_error").innerHTML = "";
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
    if (password2 == ""){
        document.getElementById("password2_error").innerHTML = "Confirm password is required!";
        error = true;
    }
    else if(password != password2){
        document.getElementById("password2_error").innerHTML = "Confirm Password and Password must be same";
        error = true;
    }
    else{
        document.getElementById("password2_error").innerHTML = "";
    }

    //term
    if (!term.checked){
        document.getElementById("term_error").innerHTML = "Please agree to terms and conditions!";
        error = true;
    }
    else{
        document.getElementById("term_error").innerHTML = "";
    }

    // return !error;
    if(error){
        return false;
    }
    else{
        return true;
    }
}
