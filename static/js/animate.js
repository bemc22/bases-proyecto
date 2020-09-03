// Configurando para poder ocultar el slidebar cuando se ingresa en alguna la sesion
$(document).ready(function () {
    // Para el login
    $('.b-us').on('click', function () {
      $('#opcion-usuario').addClass('show');
      $('#opcion-estudiante').removeClass('show');
    });

    $('.b-es').on('click', function () {
      $('#opcion-usuario').removeClass('show');
      $('#opcion-estudiante').addClass('show');
    });

    // Para el slidebar
    $('#sidebarCollapse').off('click').on('click', function () {
      $('#sidebar').toggleClass('active');
    });

    // Para filtrar la tabla
    $('#filter-input').on('keyup', function () {
      var texto = $(this).val().toLowerCase();
      var opc = $('#filter-select').val();
      $('table tbody tr').each(function (index) {
        if($(this).find('td:eq('+opc+')').text().toLowerCase().includes(texto)){
          $(this).show();
        }
        else{
          $(this).hide();
        }
      });
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
