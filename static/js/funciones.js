function guardarBlog(){
    document.getElementById("formulario").action="/blog/save";
}

function consultarBlog(){
    document.getElementById("formulario").action="/blog/get";
}

function listarBlogs(){
    document.getElementById("formulario").action="/blog/list";
}

function borrarBlog(){
    document.getElementById("formulario").action="/blog/delete";
}

function editarBlog(){
    document.getElementById("formulario").action="/blog/update";
}

function enviar(){
    document.getElementById("formulario").action="/login";
}
function insertar(){
    document.getElementById("formulario").action="/registrar";
}


