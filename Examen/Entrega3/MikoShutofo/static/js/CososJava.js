function CambiarMayusculas(){
    var a= document.getElementById('nomb');
    a.value=a.value.toUpperCase();
}

function CambiarMayus(){
    var a= document.getElementById('comun');
    a.value=a.value.toUpperCase();
}

function CambiarColor(a){
    a.style.background="pink";
}

function actual() {
    fecha=new Date(); //Actualizar fecha.
    hora=fecha.getHours(); //hora actual
    minuto=fecha.getMinutes(); //minuto actual
    segundo=fecha.getSeconds(); //segundo actual
    if (hora<10) { //dos cifras para la hora
       hora="0"+hora;
       }
    if (minuto<10) { //dos cifras para el minuto
       minuto="0"+minuto;
       }
    if (segundo<10) { //dos cifras para el segundo
       segundo="0"+segundo;
       }
    //ver en el recuadro del reloj:
    mireloj = hora+" : "+minuto+" : "+segundo;	
    return mireloj; 
    }
  function actualizar() { //función del temporizador
  mihora=actual(); //recoger hora actual
  mireloj=document.getElementById("reloj"); //buscar elemento reloj
  mireloj.innerHTML=mihora; //incluir hora en elemento
  }
  setInterval(actualizar,1000); //iniciar temporizador
  function valida_envia(){
    //valido el nombre
    if (document.fvalida.nombre.value.length==0){
           alert("Tiene que escribir su nombre")
           document.fvalida.nombre.focus()
           return 0;
    }
 
    //valido la edad. tiene que ser entero mayor que 18
    edad = document.fvalida.edad.value
    edad = validarEntero(edad)
    document.fvalida.edad.value=edad
    if (edad==""){
           alert("Tiene que introducir un número entero en su edad.")
           document.fvalida.edad.focus()
           return 0;
    }else{
           if (edad<18){
                  alert("Debe ser mayor de 18 años.")
                  document.fvalida.edad.focus()
                  return 0;
           }
    }
 
    //valido el interés
    if (document.fvalida.interes.selectedIndex==0){
           alert("Debe seleccionar un motivo de su contacto.")
           document.fvalida.interes.focus()
           return 0;
    }
 
    //el formulario se envia
    alert("Muchas gracias por enviar el formulario");
    document.fvalida.submit();
}
