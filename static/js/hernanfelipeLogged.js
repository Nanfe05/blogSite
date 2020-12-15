// Logout
var logoutButton = document.getElementById("logoutbutton");

var OnLogout = async function(event){
    event.preventDefault();
    const result = await axios.get('/api/logout');
    const responseURL = new URL(result.request.responseURL);
    if(responseURL.pathname !== '/api/logout'){
        window.location.href = result.request.responseURL;
    }
}

if(logoutButton){
    // console.log(window.location.href);
    // console.log(window.location.hostname + window.location.pathname);
    logoutButton.addEventListener("click",OnLogout,true);
}


// Add Blog

var addBlogForm = document.getElementById("addBlogForm");

var OnAddBlogSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const formData = new FormData();
    formData.append('name',event.target[0].value);
    formData.append('subject',event.target[1].value);
    formData.append('content',event.target[2].value);
    console.log(event.target[0].value,event.target[1].value,event.target[2].value);
    const result = await axios.post('/api/addblog',formData);
    
    alert(JSON.stringify(result.data));
}

if(addBlogForm){
    addBlogForm.addEventListener("submit",OnAddBlogSubmit,true);
}


// Get Blogs
var GetBlogs = async function(){
    const result = await axios.get('/api/blogs');
    console.log(JSON.stringify(result.data));
}

setTimeout(()=>{
    GetBlogs();
},2000);