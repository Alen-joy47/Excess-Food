$(document).ready(function(){
    $('#namecheck').hide();
    $('#phonecheck').hide();
    $('#passwordcheck').hide();
    $('#emailcheck').hide();
    $('#gendercheck').hide();
    $('#addresscheck').hide();
    $('#repasswordcheck').hide();

    var name_err = true;
    var phone_err = true;
    var password_err = true;
    var email_err = true;
    var gender_err = true;
    var address_err = true;
    var repassword_err = true;

    $('#name').keyup(function(){
        name_check();
    });
    $('#phone').keyup(function(){
        phone_check();
    });
    $('#password').keyup(function(){
        password_check();
    });
    $('#email').keyup(function(){
        email_check();
    });
    $('#gender').keyup(function(){
        gender_check();
    });
    $('#address').keyup(function(){
        address_check();
    });
    $('#repassword').keyup(function(){
        repassword_check();
    });

    var nameRegex = /^[A-Za-z\- ]+$/;
    var phoneRegex = /^[6-9]\d{9}$/;
    var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+]{8,}$/;

    function name_check()
    {
        var name_val = $('#name').val();
        if(name_val.length == '')
        {
            $('#namecheck').show();
            $('#namecheck').html("Please enter name");
            $('#namecheck').focus();
            $('#namecheck').css("color", "red")
            name_err = false;
            return false;
        }else if(name_val.length <3 || name_val.length >15){
            $('#namecheck').show();
            $('#namecheck').html("Name length should be between 3 to 14 characters");
            $('#namecheck').focus();
            $('#namecheck').css("color", "red")
            name_err = false;
            return false;
        }else if(!nameRegex.test(name_val)){
            $('#namecheck').show();
            $('#namecheck').html("Name should contain letters");
            $('#namecheck').focus();
            $('#namecheck').css("color", "red")
            name_err = false;
            return false;
        }else{
            $('#namecheck').hide();
        }
    }

    function phone_check()
    {
        var phone_val = $('#phone').val();
        if(phone_val.length == '')
        {
            $('#phonecheck').show();
            $('#phonecheck').html("Please enter contact number");
            $('#phonecheck').focus();
            $('#phonecheck').css("color", "red")
            phone_err = false;
            return false;
        }else if(phone_val.length != 10){
            $('#phonecheck').show();
            $('#phonecheck').html("Invalid contact number");
            $('#phonecheck').focus();
            $('#phonecheck').css("color", "red")
            phone_err = false;
            return false;
        }else if(!phoneRegex.test(phone_val)){
            $('#phonecheck').show();
            $('#phonecheck').html("Contact should start with 6-9");
            $('#phonecheck').focus();
            $('#phonecheck').css("color", "red")
            phone_err = false;
            return false;
        }else{
            $('#phonecheck').hide();
        }
    }
    function email_check()
    {
        var email_val = $('#email').val();
        if(email_val.length == '')
        {
            $('#emailcheck').show();
            $('#emailcheck').html("Please enter email");
            $('#emailcheck').focus();
            $('#emailcheck').css("color", "red")
            email_err = false;
            return false;
        }else if(!emailRegex.test(email_val)){
            $('#emailcheck').show();
            $('#emailcheck').html("Invalid email");
            $('#emailcheck').focus();
            $('#emailcheck').css("color", "red")
            email_err = false;
            return false;
        }else{
            $('#emailcheck').hide();
        }
    }
    function gender_check()
    {
        var gender_val = $('#gender').val();
        if(gender_val.length == '-1')
        {
            $('#gendercheck').show();
            $('#gendercheck').html("Please select gender");
            $('#gendercheck').focus();
            $('#gendercheck').css("color", "red")
            gender_err = false;
            return false;
        }else{
            $('#gendercheck').hide();
        }
    }
    function address_check()
    {
        var address = $('#address').val();
        if(address.length == '')
        {
            $('#addresscheck').show();
            $('#addresscheck').html("Please enter address");
            $('#addresscheck').focus();
            $('#addresscheck').css("color", "red")
            address_err = false;
            return false;
        }else{
            $('#addresscheck').hide();
        }
    } 
    function password_check()
    {
        var password = $('#password').val();
        if(password.length == '')
        {
            $('#passwordcheck').show();
            $('#passwordcheck').html("Please enter password");
            $('#passwordcheck').focus();
            $('#passwordcheck').css("color", "red")
            password_err = false;
            return false;
        }else if(password.length < 8 || password.length >15)
        {
            $('#passwordcheck').show();
            $('#passwordcheck').html("Password length should be between 8-15");
            $('#passwordcheck').focus();
            $('#passwordcheck').css("color", "red")
            password_err = false;
            return false;
        }
        else if(!passwordRegex.test(password))
        {
            $('#passwordcheck').show();
            $('#passwordcheck').html("Password should be a combination of uppercase, lowercase, digit and numbers");
            $('#passwordcheck').focus();
            $('#passwordcheck').css("color", "red")
            password_err = false;
            return false;
        }
        else{
            $('#passwordcheck').hide();
        }
    }
    function repassword_check()
    {
        var password = $('#password').val();
        var repassword = $('#repassword').val();
        if(repassword.length == '')
        {
            $('#repasswordcheck').show();
            $('#repasswordcheck').html("Please enter password");
            $('#repasswordcheck').focus();
            $('#repasswordcheck').css("color", "red")
            repassword_err = false;
            return false;
        }else if(repassword.length < 8 || repassword.length >15)
        {
            $('#repasswordcheck').show();
            $('#repasswordcheck').html("Password length should be between 8-15");
            $('#repasswordcheck').focus();
            $('#repasswordcheck').css("color", "red")
            password_err = false;
            return false;
        }
        else if(!passwordRegex.test(repassword))
        {
            $('#repasswordcheck').show();
            $('#repasswordcheck').html("Password should be a combination of uppercase, lowercase, digit and numbers");
            $('#repasswordcheck').focus();
            $('#repasswordcheck').css("color", "red")
            repassword_err = false;
            return false;
        }else if(password != repassword){
            $('#repasswordcheck').show();
            $('#repasswordcheck').html("Both the password sholud be same ");
            $('#repasswordcheck').focus();
            $('#repasswordcheck').css("color", "red")
            repassword_err = false;
            return false;
        }
        else{
            $('#repasswordcheck').hide();
        }
    }
//     $("#myform").submit(function (event) {
//         event.preventDefault();
//         if (validateBus()) {
//             this.submit();
//         }
//     });

//     const validateBus = () => {
//         name_check();
//         phone_check();
//         email_check();
//         address_check();
//         password_check();
//         repassword_check();
//         gender_check();
//     }
    
//     $('#loginSubmit').click(function(event){
//         phone_err = true;
//         password_err = true;
//         phone_check();
//         password_check();
        

//         if(phone_check && password_check)
//             {
//                 return true
//             }
//             else
//             {
//                 return false;
//             }
//     });
});