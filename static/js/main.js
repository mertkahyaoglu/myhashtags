$(function() {

  $('#button').click(function(e) {
    var inputVal = $('#input').val();
    var href = 'username/' + inputVal;
    $(this).attr('href', href);
  });

});
