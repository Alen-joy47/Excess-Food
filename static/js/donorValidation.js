// const form = document.getElementById('addFoodForm');
// const foodName = document.getElementById('name');
// const type = document.getElementById('type');
// const quantity = document.getElementById('qty');
// const description = document.getElementById('description');
// const image = document.getElementById('images');

// form.addEventListener('submit', e =>{
//     e.preventDefault();
//     validateInputs();
// });

// const setError = (element, message) =>{
//     const inputControl = element.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay.innerText = message;
//     inputControl.classList.add('error');
//     inputControl.classList.remove('success');

// }
// const setSuccess = element =>{
//     const inputControl = element.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay.innerText = "";
//     inputControl.classList.add('success');
//     inputControl.classList.remove('error');
//     form.submit();
// }

// const validateInputs= () =>{
//     let validate = false;
//     const nameValue = foodName.value.trim();
//     const typeValue = type.value.trim();
//     const qtyValue = quantity.value.trim();
//     const descriptionValue = description.value.trim();
//     const imageValue = image.value.trim();

//     if(nameValue == ''){
//         setError(foodName, "Name is required..")
//         validate = false;
//     } else {
//         setSuccess(foodName)
//         validate = true;
//     }

//     if(typeValue == '-1'){
//         setError(type, "type is required..")
//     } else {
//         setSuccess(type)
//         validate = true;
//     }

//     if(qtyValue == ''){
//         setError(quantity, "Quantity is required..")
//     } else {
//         setSuccess(quantity)
//         validate = true;
//     }

//     if(descriptionValue == ''){
//         setError(description, "Description is required..")
//     } else {
//         setSuccess(description)
//         validate = true;
//     }
// }

// $(document).ready(function () {
//     // add new buss
//     $('#addFoodForm').submit(function (event) {
//         event.preventDefault();
//         validateBus();
//         // if (validateBus()) {
//         //     var formData = new FormData(this);
//         //     addEditBus(formData);
//         // }
//     });
// });

// const showError = (element, message) =>{
//         const inputControl = element.parentElement;
//         const errorDisplay = inputControl.querySelector('.error');

//         errorDisplay.innerText = message;
//         inputControl.classList.add('error');
//         inputControl.classList.remove('success');
// }

// const validateBus = () => {
//     const foodName = document.getElementById('name');
//     const type = document.getElementById('type');
//     const quantity = document.getElementById('qty');
//     const description = document.getElementById('description');
//     const image = document.getElementById('images');
//     if (foodName.val() === '') {
//         showError(foodName, 'Bus name is required');
//         return false;
//     }
//     if (quantity.val() === '') {
//         showError(quantity, 'Bus number is required');
//         return false;
//     }
//     if (description.val() === '') {
//         showError(description, 'Model number is required');
//         return false;
//     }
//     if (type.val() === '') {
//         showError(type, 'Bus color is required');
//         return false;
//     }

//     if (image[0].files.length === 0) {
//         if (Type.val() == 'Edit') {
//             return true;
//         }
//         showError(image, 'Image is required');
//         return false;
//     }
//     return true;
// }

$(document).ready(function () {
    // add new bus
    $("#addFoodForm").submit(function (event) {
        event.preventDefault();
        if (validateBus()) {
            // var formData = new FormData(this);
            this.submit();
        }
    });

    const showError = (message) => {
        const errorDisplay = $(".error");
        errorDisplay.text(message);
        errorDisplay
            .closest(".input-control")
            .addClass("error")
            .removeClass("success");
    };

    const showSuccess = () => {
        const errorDisplay = $(".error");
        errorDisplay.text("");
        errorDisplay
            .closest(".input-control")
            .addClass("success")
            .removeClass("error");
    };

    const validateBus = () => {
        const foodName = $("#name");
        const qty = $("#qty");
        const desc = $("#description");
        const img = $("#images");
        const SelectType = $("#type");
        const category = $("#category");
        const preparation_time = $("#preparation_time");
        // const checkbox1 = $("#checkbox1");
        const checkboxes = document.querySelectorAll('input[name="ingredients"]:checked');

        if (foodName.val() == "-1") {
            showError("Food name is required");
            return false;
        }
        if (SelectType.val() === "-1") {
            // Assuming '-1' is the default/invalid option
            showError("Please select a type option");
            return false;
        }
        if (category.val() === "-1") {
            // Assuming '-1' is the default/invalid option
            showError("Please select a category option");
            return false;
        }
        if (checkboxes.length === 0) {
            showError("Please select at least one ingredient");
            return false;
        }

        if (qty.val() == "") {
            showError("Quantity is required");
            return false;
        }
        if (preparation_time.val() == "") {
            showError("preparation_time is required");
            return false;
        }
        if (desc.val() == "") {
            showError("Description is required");
            return false;
        }

        if (img[0].files.length == 0) {
            showError("Image is required");
            return false;
        }
        showSuccess();
        return true;
    };
});

$(document).ready(function () {
    $("#editProfile").submit(function (event) {
        event.preventDefault();
        if (validateBus()) {
            // var formData = new FormData(this);
            this.submit();
        }
    });

    const showError = (message) => {
        const errorDisplay = $(".error");
        errorDisplay.text(message);
        errorDisplay
            .closest(".input-control")
            .addClass("error")
            .removeClass("success");
    };

    const showSuccess = () => {
        const errorDisplay = $(".error");
        errorDisplay.text("");
        errorDisplay
            .closest(".input-control")
            .addClass("success")
            .removeClass("error");
    };

    const validateBus = () => {
        const name = $("#name");
        const email = $("#email");
        const phone = $("#phone");
        const gender = $("#gender");
        const address = $("#address");

        if (name.val() == "") {
            showError("Name is required");
            return false;
        }
        if (email.val() === "") {
            // Assuming '-1' is the default/invalid option
            showError("Email is required");
            return false;
        }
        if (phone.val() == "") {
            showError("Phone is required");
            return false;
        }
        if (gender.val() == "-1") {
            showError("Gender is required");
            return false;
        }
        if (address.val() == "") {
            showError("Address is required");
            return false;
        }
        
        showSuccess();
        return true;
    };
});

$(document).ready(function () {
    $("#donorSignup").submit(function (event) {
        event.preventDefault();
        if (validateBus()) {
            this.submit();
        }
    });
  
    const showError = (message) => {
        const errorDisplay = $(".error");
        errorDisplay.text(message);
        errorDisplay
            .closest(".input-control")
            .addClass("error")
            .removeClass("success");
    };
  
    const showSuccess = () => {
        const errorDisplay = $(".error");
        errorDisplay.text("");
        errorDisplay
            .closest(".input-control")
            .addClass("success")
            .removeClass("error");
    };
  
    const validateBus = () => {
        const name = $("#name");
        const email = $("#email");
        const phone = $("#phone");
        const gender = $("#gender");
        const address = $("#address");
        const password = $("#password");
        const repassword = $("#repassword");
  
        if (name.val() == "") {
            showError("Name is required");
            return false;
        }
        if (email.val() === "") {
            // Assuming '-1' is the default/invalid option
            showError("Email is required");
            return false;
        }
        if (phone.val() == "") {
            showError("Phone is required");
            return false;
        }
        if (gender.val() == "-1") {
            showError("Gender is required");
            return false;
        }
        if (address.val() == "") {
            showError("Address is required");
            return false;
        }
        if (password.val() == "") {
          showError("Password is required");
          return false;
        }
        if (repassword.val() == "") {
            showError("Password is required");
            return false;
        }
        // if (password.val() === repassword.val()) {
        //   showError("Password should be same...");
        //   return false;
        // }
        showSuccess();
        return true;
    };
  });

$(document).ready(function () {
    $("#donorLogin").submit(function (event) {
        event.preventDefault();
        if (validateBus()) {
            this.submit();
        }
    });
  
    const showError = (message) => {
        const errorDisplay = $(".error");
        errorDisplay.text(message);
        errorDisplay
            .closest(".input-control")
            .addClass("error")
            .removeClass("success");
    };
  
    const showSuccess = () => {
        const errorDisplay = $(".error");
        errorDisplay.text("");
        errorDisplay
            .closest(".input-control")
            .addClass("success")
            .removeClass("error");
    };
  
    const validateBus = () => {
        const phone = $("#phone");
        const password = $("#password");
  
        if (phone.val() == "") {
            showError("Phone is required");
            return false;
        }
        if (password.val() == "") {
          showError("Password is required");
          return false;
        }
  
        showSuccess();
        return true;
    };
  });
