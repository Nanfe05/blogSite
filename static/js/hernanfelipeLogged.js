// Add Blog

var addBlogForm = document.getElementById("addBlogForm");

var OnAddBlogSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const formData = new FormData();
    formData.append('name',event.target[0].value);
    formData.append('subject',event.target[2].value);
    const result = await axios.post('/api/addblog',formData);
    alert(JSON.stringify(result.data));
}

if(addBlogForm){
    addBlogForm.addEventListener("submit",OnAddBlogSubmit,true);
}


// Get Blogs
var GetBlogs = async function(){
    const result = await axios.get('/api/blogs');
    alert(JSON.stringify(result.data));
}

setTimeout(()=>{
    GetBlogs();
},2000);