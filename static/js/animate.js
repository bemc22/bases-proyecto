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

    // Para el tratamiento de los datos del Login
    $('#link-tyc').on('click', function () {
      event.preventDefault();
      Swal.mixin({
        title: 'POLÍTICA DE PROTECCIÓN DE DATOS',
        confirmButtonText: 'Siguiente &rarr;',
        showCancelButton: true,
        progressSteps: ['1', '2', '3']
      }).queue([
        {
          text: 'Declaro que autorizo a Galea para  la recolección y tratamiento de mis datos personales, conforme a la política de datos personales disponible aquí, entiendo que los datos serán objeto de recolección, almacenamiento, uso, circulación, supresión, transferencia, transmisión, cesión y todo el tratamiento, con la finalidad de obtener información sobre los servicios y eventos realizados por el laboratorio.'
        },
        {
          text:'Declaro que se me ha informado que como Titular de la información tengo derecho a conocer, actualizar y rectificar mis datos personales, solicitar prueba de la autorización otorgada para su tratamiento, ser informado sobre el uso que se ha dado a los mismos, presentar quejas ante la Superintendencia de Industria y Comercio por infracción a la ley, revocar la autorización y/o solicitar la supresión de mis datos en los casos en que sea procedente y acceder en forma gratuita a los mismos.'
        },
        {
          text:'Así mismo, se me ha informado que las consultas y reclamos podrán ser presentados a GALEA, como responsable del tratamiento de la información, a través del correo electrónico servicioalcliente@galea.uis.edu.co, en cumplimiento de la Ley 1581 de 2012, el Decreto No. 1377 de 2013 y demás normas concordantes.',
          confirmButtonText: 'Terminar'
        }
      ]);
    });

    //
    $('#tyc').change(function () {
      if(this.checked){
        $('#register-button').removeAttr("disabled");
      }
      else{
        $('#register-button').attr("disabled", true);
      }
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
