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
function notificacion(type, msg){
  Swal.fire({
    icon: type,
    title: msg,
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    onOpen: (toast) => {
      toast.addEventListener('mouseenter', Swal.stopTimer)
      toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
  })
}
