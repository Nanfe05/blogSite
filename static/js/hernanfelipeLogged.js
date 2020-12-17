// Util 
// Close Modals
const closeModals = (id) =>{
    const modal = document.getElementById(id);
    const modalBack = document.getElementsByClassName('modal-backdrop')[0];
    if(modal){
        modal.classList.remove("show");
        modalBack.classList.remove("show");
    }
};

// Get Blogs
const updateBlogs = new Event('updateBlogs');
const updateComments = new Event('updateComments');

const blogsContainer = document.getElementById("blogsContainer");


blogsContainer.addEventListener('updateBlogs',async function(){
    const result = await axios.get('/api/blogs');
    window.dispatchEvent(updateComments);
    console.log(result.data);
    var content = result.data.map((el,i)=>{
        var title= String(el[3]);
        var subject= String(el[2]);
        var content= String(el[4]);
        var id=String(el[0]);
        return( 
        `<div class="hf-blog">
            <div class="hf-blog-title">
                ${title}
                <div class="hf-editete-group">
                    <span class="hf-edit-button" onClick="editarBlog('${title}','${subject}','${content}','${id}');">Editar</span>
                    <span class="hf-delete-button" onClick="eliminarBlog('${id}');">Eliminar</span>
                </div>
            </div>
            <div class="hf-blog-desc">
                <div class="hf-blog-subject">
                ${subject}
                </div>
                <div class="hf-blog-content">
                    ${content}
                </div>
                <div class="hf-blog-subtitle">
                    <span>Comentarios:</span>
                </div>
                <div class="hf-blog-last-comment" id="blog-${id}-comment-${id}">
                    No ha sido comentado aun
                </div>
                <span onCLick="window.comment_id=${id};" id="to-comment-button-${id}" data-bs-toggle="modal" data-bs-target="#agregarComentario" class="hf-comment-button">Comentar<span/>
            </div>
        </div>`);
    });
    content.join("");

    blogsContainer.innerHTML = content;
});


// Get Comments



window.addEventListener('updateComments',async function(){
    const result = await axios.get('/api/comments');
    let init = false;
    comentarios = result.data;
    console.log(comentarios);
    
    comentarios.forEach((el,i)=>{
        comentario_container = document.getElementById(`blog-${el[1]}-comment-${el[1]}`);
        if(comentario_container){
            if(comentario_container.innerHTML.trim() === 'No ha sido comentado aun' || !init){
                comentario_container.innerHTML= el[2];
                init = true;
            }else(
                comentario_container.innerHTML += `
               <span style="margin: 10px 0;">${el[2]}<span>
            `
            )
        }
        // comentario_button = document.getElementById(`to-comment-button-${el[1]}`);
        // if(comentario_button){
        // comentario_button.style.display="none";   
        // }
    });

    
});


// <!--<span data-bs-toggle="modal" data-bs-target="#agregarComentario" class="hf-comment-button" onCLick="window.comment_id=${el[0]};">Comentar<span/>-->

setTimeout(()=>{
    blogsContainer.dispatchEvent(updateBlogs);
},0);

// Delete Blog
const eliminarBlog = async (id)=>{
    const result = await axios.get(`/api/deleteBlog/${id}`);
    console.log(JSON.stringify(result.data));
    blogsContainer.dispatchEvent(updateBlogs);
};
// Editar Blog 
const editarBlog = async (title,subject,content,id)=>{
    const modal = document.getElementById('#editarBlog');
    if(modal){
        modal.click();
    }
    const titleInput= document.getElementById("blog-title-input");
    if(titleInput){
        titleInput.value=title;
    }
    const subjectInput= document.getElementById("blog-subject-input");
    if(subjectInput){
        subjectInput.value=subject;
    }
    const contentInput= document.getElementById("blog-content-input");
    if(contentInput){
        contentInput.value=content;
    }
    const idInput = document.getElementById("blog-id-input");
    if(idInput){
        idInput.value=id;
    }
    console.log(title,subject,content,id);
};

// Logout
var logoutButton = document.getElementById("logoutbutton");

var OnLogout = async function(event){
    event.preventDefault();
    const result = await axios.get('/api/logout');
    const responseURL = new URL(result.request.responseURL);
    if(responseURL.pathname !== '/api/logout'){
        window.location.href = result.request.responseURL;
    }
};

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
    const result = await axios.post('/api/addblog',formData);
    console.log(JSON.stringify(result.data));
    blogsContainer.dispatchEvent(updateBlogs);

    closeModals('agregarBlog');

}

if(addBlogForm){
    addBlogForm.addEventListener("submit",OnAddBlogSubmit,true);
}

// Edit Blog Form
 
var editBlogForm = document.getElementById("editBlogForm");

var OnEditBlogSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const formData = new FormData();
    formData.append('title',event.target[0].value);
    formData.append('subject',event.target[1].value);
    formData.append('content',event.target[2].value);
    formData.append('id',event.target[3].value);
    const result = await axios.post('/api/editblog',formData);
    console.log(JSON.stringify(result.data));
    blogsContainer.dispatchEvent(updateBlogs);

    // const modal = document.getElementById('editarBlog');
    // const modalBack = document.getElementsByClassName('modal-backdrop')[0];
    // if(modal){
    //     console.log(modal);
    //     modal.classList.remove("show");
    //     modalBack.classList.remove("show");
    // }
    closeModals('editarBlog');
}

if(editBlogForm){
    editBlogForm.addEventListener("submit",OnEditBlogSubmit,true);
}


// Agregar Comentario

var addCommentForm = document.getElementById("addComment");

var OnAddCommentSubmit = async function(event){
    event.preventDefault();
    // Create form data
    const formData = new FormData();
    formData.append('id',window.comment_id);
    formData.append('comment',event.target[0].value);
    console.log(window.comment_id);
    const result = await axios.post('/api/addcomment',formData);
    console.log(JSON.stringify(result.data));
    window.dispatchEvent(updateComments);
    // blogsContainer.dispatchEvent(updateBlogs);

    closeModals('agregarComentario');
}

if(addCommentForm){
    addCommentForm.addEventListener("submit",OnAddCommentSubmit,true);
}


