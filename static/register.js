var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder='Email..';
form_fields[2].placeholder='Username..';
form_fields[3].placeholder='Enter password...';
form_fields[4].placeholder='Re-enter Password...';
form_fields[5].placeholder='First name...';
form_fields[6].placeholder='Last name...';


for (var field in form_fields){	
form_fields[field].className += ' form-control'
}


function show()
{
   if(!document.getElementById("bonus_info").classList.contains("bonus_infoshow")){
      document.getElementById("errors").classList.toggle("appear");
      document.getElementById("register-section").classList.toggle("mai_mic");
      document.getElementById("errorbtn").setAttribute('height', "25px !important");
   }
   else alert("Please close the login info page")
  
}

function show_info()
{
   if(!document.getElementById("errors").classList.contains("appear")){
         document.getElementById("bonus_info").classList.toggle("bonus_infoshow")
         document.getElementById("register-section").classList.toggle("form_left")

         let setting = document.getElementById('arrow');
               setting.classList.toggle('moverotate');
   }
   else alert("Inchide boule erorile!");
}