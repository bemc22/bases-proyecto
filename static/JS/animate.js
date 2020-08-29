$(document).ready(function () {

    $('#sidebarCollapse').off('click').on('click', function () {
      console.log('Funciona');
        $('#sidebar').toggleClass('active');
    });

});
