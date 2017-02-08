$(document).ready(function(){
  $('#id_postcode').mask('00000-000');
  $('#id_phone_number').mask('(00)00000-0000');
  $('#id_country option[value="BR"]').attr("selected",true);
});
