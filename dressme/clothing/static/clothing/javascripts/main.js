$(document).ready(function() {
  $('.incr').click(function() {
    var article = $(this).parent().parent().find('.article').text();
    var clean = $(this).parent().parent().find('.clean');
    clean.text(Number(clean.text()) + 1);
    //$.post('/write', { update: [article, 1] });
  });
  $('.decr').click(function() {
    var article = $(this).parent().parent().find('.article').text();
    var clean = $(this).parent().parent().find('.clean');
    clean.text(Number(clean.text()) - 1);
    //$.post('/write', { update: [article, -1]});
  });
});

