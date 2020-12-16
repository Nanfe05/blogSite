// Get Blogs
const updateBlogs = new Event('updateBlogs');

const blogsContainer = document.getElementById("blogsContainer");


blogsContainer.addEventListener('updateBlogs',async function(){
    const result = await axios.get('/api/blogs');

    console.log(result.data);
    var content = result.data.map((el,i)=>{
        return `    
        <div class="hf-blog">
            <div class="hf-blog-title">
                ${el[3]}
                <div class="hf-editete-group">
                    <span class="hf-edit-button">Editar<span/>
                    <span class="hf-delete-button">Eliminar<span/>
                </div>
            </div>
            <div class="hf-blog-desc">
                <div class="hf-blog-subject">
                ${el[2]}
                </div>
                <div class="hf-blog-content">
                    ${el[4]}
                </div>
                <div class="hf-blog-subtitle">
                    <span>Ultimo Comentario:</span>
                    <span>${el[5]}</span>
                </div>
                <div class="hf-blog-last-comment">
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ....
                </div>
                <span class="hf-comment-button">Comentar<span/>
            </div>
        </div> 
        `;
    });
    content.join();

    blogsContainer.innerHTML = content;
});


setTimeout(()=>{
    blogsContainer.dispatchEvent(updateBlogs);
},1000);

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
    formData.append('title',event.target[0].value);
    formData.append('subject',event.target[1].value);
    formData.append('content',event.target[2].value);
    console.log(event.target[0].value,event.target[1].value,event.target[2].value);
    const result = await axios.post('/api/addblog',formData);
    console.log(JSON.stringify(result.data));
    blogsContainer.dispatchEvent(updateBlogs);

}

if(addBlogForm){
    addBlogForm.addEventListener("submit",OnAddBlogSubmit,true);
}



