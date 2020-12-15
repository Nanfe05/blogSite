// Login Form 
var loginForm = document.getElementById("loginForm");

var OnLoginSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const formData = new FormData();
    formData.append('email',event.target[0].value);
    formData.append('password',event.target[1].value);
    
    const result = await axios.post('/api/login',formData);

    const responseURL = new URL(result.request.responseURL);
    if(responseURL.pathname !== '/api/login'){
        window.location.href = result.request.responseURL;
    }else{
        alert(JSON.stringify(result.data));
    }
}

if(loginForm){
    loginForm.addEventListener("submit",OnLoginSubmit,true);
}

// Register Form 
var registerForm = document.getElementById("formulario-registro");
var OnRegisterSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const registerData = new FormData();
    registerData.append('name',event.target[0].value);
    registerData.append('lastname',event.target[1].value);
    registerData.append('email',event.target[2].value);
    registerData.append('password',event.target[3].value);
    
    const result = await axios.post('/api/register',registerData);
    const responseURL = new URL(result.request.responseURL);
    if(responseURL.pathname !== '/api/register'){
        window.location.href = result.request.responseURL;
    }else{
        alert(JSON.stringify(result.data));
    }
}

if(registerForm){
    registerForm.addEventListener("submit",OnRegisterSubmit,true);
}

// Recover Form

var recoverForm = document.getElementById("recoverForm");

var OnRecoverSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const formData = new FormData();
    formData.append('email',event.target[0].value);
    const result = await axios.post('/api/recoverpassword',formData);
    alert(JSON.stringify(result.data));
}

if(recoverForm){
    recoverForm.addEventListener("submit",OnRecoverSubmit,true);
}
