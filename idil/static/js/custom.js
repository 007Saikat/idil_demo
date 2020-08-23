// Rating Initialization
$(document).ready(function() {

    $('.rating input').click(function(){
        $(this).val()
        alert($(this).val());
    });

    $(function () {
      $('[data-toggle="tooltip"]').tooltip({ boundary: 'window' })
    })


    $('.nav-link').click(function(){
        $(this).parent('li').addClass('active');
    });



   //$("#navhowto").addClass('active');


   var_Url =  $(location).attr('href');
   arr_split = var_Url.split('/')


   if(arr_split.length == 6){

       Page_Name = arr_split[arr_split.length - 3]
   }
   else if(arr_split.length == 5)   {
        Page_Name =  arr_split[arr_split.length - 2]
   }
   else{
        Page_Name = arr_split[arr_split.length -1]
   }


   switch(Page_Name) {
      case 'challenges':
        $("#navChallenge").addClass('active');
        break;
       case 'lb':
        $("#navBoard").addClass('active');
        break;
       case 'about':
        $("#navAbout").addClass('active');
        break;
       case '':
        $("#navHone").addClass('active');
        break;
       case 'register':
        $("#navRegister").addClass('active');
        break;

       case 'employer':
        $("#navuser").addClass('active');
        break;

       case 'employee':
        $("#navuser1").addClass('active');
        break;

      default:
        $("#navuser2").addClass('active');


    }


});