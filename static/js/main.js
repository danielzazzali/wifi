$(document).ready(function() {
    $('#refresh-button').click(function() {
        $('#wifi-result').text('Cargando redes WiFi...');

        // Hacer una solicitud AJAX al servidor para actualizar las redes
        $.get('/', function(data) {
            var wifiContent = $(data).find('#wifi-result').html();
            $('#wifi-result').html(wifiContent);
        }).fail(function() {
            $('#wifi-result').text('Error al obtener las redes WiFi.');
        });
    });
});
