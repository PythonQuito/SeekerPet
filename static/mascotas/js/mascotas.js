document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {});
});


var headers = new Headers();
var options = {
    method: 'GET',
    headers: headers,
    mode: 'cors',
    cache: 'default',
    credentials: 'include'
}


mascotas = {}
mascotas.pedirInformacion = function (url, elemento) {
    fetch(url, options).then(function (response) {
        return response.text();
    }).then(function (data) {
        elemento.innerHTML = data;
    });
}


mascotas.marcarMascotaEncontrada = function (url, elemento) {
    fetch(url, options).then(function (response) {
        return response.json();
    }).then(function (data) {
        if (data.status === 'ok') {
            elemento.parentNode.removeChild(elemento);
        }
    });
}


mascotas.asignarEvento = function () {
    document.getElementById('necesito_informacion').addEventListener("click", function (event) {
        var instance = M.Modal.getInstance(document.getElementById('modal1'));
        instance.open();
        var url = document.getElementById('url_informacion').getAttribute('data-url');
        var elemento = document.getElementById('info_propieario');
        mascotas.pedirInformacion(url, elemento);
    });

    document.getElementById('encontre_mascota').addEventListener("click", function (event) {
        var url = document.getElementById('marcar_mascota').getAttribute('data-url');
        var elemento = document.getElementById('encontre_mascota');
        mascotas.marcarMascotaEncontrada(url, elemento);
    });
}

mascotas.asignarEvento();
