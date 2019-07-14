$(document).ready(function() {
    console.log( "ready!" );

    $("#latest").on('click', () => {
      $('#latest').addClass('active');
      $('#videos').removeClass('active');
      $('#articles').removeClass('active');

      $('.latest').fadeIn();
      $('.video').fadeOut();
      $('.article').fadeOut();
    });

    $("#videos").on('click', () => {
      $('#videos').addClass('active');
      $('#latest').removeClass('active');
      $('#articles').removeClass('active');

      $('.article').fadeOut();
      $('.video').fadeIn();
    });

    $("#articles").on('click', () => {
      $('#articles').addClass('active');
      $('#latest').removeClass('active');
      $('#video').removeClass('active');

      $('.video').fadeOut();
      $('.article').fadeIn();
    });

    $('.video').hide();
    $('.article').hide();
    $('.video').removeClass('hidden');
    $('.article').removeClass('hidden');
});
