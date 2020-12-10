var nombre = document.getElementById("nombres").value;
var apellido = document.getElementById("apellidos").value;
var correo = document.getElementById("correo").value;
var contrasena = document.getElementById("Contrasena").value;
var vericontrasena = document.getElementById("veriContrasena").value;
var formato_correo = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
/*if(!correo.match(formato_correo)){
document.getElementById('correoError').innerHTML = 'Verifica la direccion de correo';


}
else{
document.getElementById('correoError').innerHTML = '';
}*/
if(nombre=="" || apellido=="" || correo=="" || contrasena=="" || vericontrasena=="" ) {

alert("Por favor rellena todos los campos");

}


else{
if(contrasena!=vericontrasena){
alert("Las contrasenas no coindicen");

}
else{
var nombre = document.getElementById("nombres").value="";
var apellido = document.getElementById("apellidos").value="";
var correo = document.getElementById("correo").value="";
var contrasena = document.getElementById("Contrasena").value="";
var vericontrasena = document.getElementById("veriContrasena").value="";
alert("Registro Exitoso");
}
}
//<--span id='correoerror' style="color:blueviolet;"></span>span>