$(document).ready(function() {
    $.getJSON('http://127.0.0.1:8000/api/lista_personal', function(data) {
        var producto = data;

        $('#enviar').click(function() {
            $.each(producto, function(i, item) {
                $('#categorias').append(
                    "<tr><td>" + item.rut + "-" + item.dv +
                    "</td><td>" + item.pnombre + " " + item.snombre + " " + item.appaterno + " " + item.apmaterno +
                    "</td><td>" + item.fono +
                    "</td><td>" + item.cargo +
                    "</td><td>" + item.comuna +
                    "</td><td>" + item.fecha_ing +
                    "</td><td>" + "</td></tr>");
            });

        });

    }).fail(function() {
        console.log('Error al consumir la API!');
    });

});