$(document).ready(function(){
  $("#id_cpf")
  values = {cpf:$('#id_cpf').val(), cnpj:$('#id_cnpj').val()};
  for (var value in values){
    if(value == 'cpf'){
      $('#id_' + value).mask('000.000.000-00')
    }else{
      $('#id_' + value).mask('00.000.000/0000-00')
    }
    if (values[value]==''){
      $('#id_' + value).closest('.form-group').remove();
    }
  }
});
