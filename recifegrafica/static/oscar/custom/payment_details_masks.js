$(document).ready(function(){
  $('#id_number').mask('0000.0000.0000.0000');
  $('#id_ccv').mask('000');
  if ($('.alert').length){
        $(':input').val('');
    }
});
