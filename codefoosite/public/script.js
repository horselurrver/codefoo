$(document).ready(function() {
    console.log( "ready!" );

    $("#latest").on('click', () => {
      $('#latest').addClass('active');
      $('#videos').removeClass('active');
      $('#articles').removeClass('active');
    });

    $("#videos").on('click', () => {
      $('#videos').addClass('active');
      $('#latest').removeClass('active');
      $('#articles').removeClass('active');
    });

    $("#articles").on('click', () => {
      $('#articles').addClass('active');
      $('#latest').removeClass('active');
      $('#articles').removeClass('active');
    });
});
