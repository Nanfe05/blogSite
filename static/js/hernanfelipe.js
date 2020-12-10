// Login Form 
var loginForm = document.getElementById("loginForm");

var OnLoginSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const formData = new FormData();
    formData.append('email',event.target[0].value);
    formData.append('password',event.target[1].value);

    const result = await axios.post('/api/login',formData);
    alert(JSON.stringify(result.data));
}

if(loginForm){
    loginForm.addEventListener("submit",OnLoginSubmit,true);
}

// Register Form 
// var registerForm = document.getElementById("registerForm");

// var OnRegisterSubmit = async function(event){
//     event.preventDefault();
//     console.log('Register Form');
// }

// if(registerForm){
//     registerForm.addEventListener("submit",OnRegisterSubmit,true);
// }

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
