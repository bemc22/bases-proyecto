// Configurando para poder ocultar el slidebar cuando se ingresa en alguna la sesion
$(document).ready(function () {
    $('#sidebarCollapse').off('click').on('click', function () {
      $('#sidebar').toggleClass('active');
    });

    $('.b-us').on('click', function () {
      $('#opcion-usuario').addClass('show');
      $('#opcion-estudiante').removeClass('show');
    });

    $('.b-es').on('click', function () {
      $('#opcion-usuario').removeClass('show');
      $('#opcion-estudiante').addClass('show');
    });
});


// Configurando alertas:
function notifica_error(msg){
  Swal.fire({
    icon: 'error',
    title: 'Oops...',
    text: msg,
    footer: 'Si no recuerda su contraseña, por favor consulte al admin encargado'
  })
}
