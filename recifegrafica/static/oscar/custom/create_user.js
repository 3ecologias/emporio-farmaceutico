$(document).ready(function(){
  $('#id_registration-cnpj').closest('.form-group').hide();
  $('#id_registration-cpf').prop('required',true);
});

$('#id_registration-persona').on('change', function(){
  var selection = $(this).val();
  switch(selection){
    case 'fs':
      $('#id_registration-cnpj').closest('.form-group').hide();
      $('#id_registration-cnpj').removeAttr('required');
      $('#id_registration-cpf').closest('.form-group').show();
      $('#id_registration-cpf').prop('required',true);
      break;
    case 'jr':
      $('#id_registration-cnpj').closest('.form-group').show();
      $('#id_registration-cnpj').prop('required',true);
      $('#id_registration-cpf').closest('.form-group').hide();
      $('#id_registration-cpf').removeAttr('required');
      break;
  }
});
