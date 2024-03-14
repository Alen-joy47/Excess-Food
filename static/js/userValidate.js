$(document).ready(function () {
  $("#userSignup").submit(function (event) {
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
      const location = $("#location");
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
      if (location.val() == "-1") {
        showError("Location is required");
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
      showSuccess();
      return true;
  };
});

$(document).ready(function () {
  $("#ratingForm").submit(function (event) {
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
      const order_no = $("#order_id");
      const rate = $("#ratings");
      const description = $("#description");

      if (order_no.val() === "-1") {
          showError("Select food on order_id is required");
          return false;
      }
      if (rate.val() === "-1") {
          showError("Ratings is required");
          return false;
      }
      if (description.val() == "") {
          showError("Description is required");
          return false;
      }
      showSuccess();
      return true;
  };
});



$(document).ready(function () {
    $("#orderNow").submit(function (event) {
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
        const order_no = $("#address");
        const description = $("#description");
  
        if (order_no.val() === "") {
            showError("Address is required");
            return false;
        }
        
        if (description.val() == "") {
            showError("Description is required");
            return false;
        }
        showSuccess();
        return true;
    };
  });




$(document).ready(function () {
    // add new bus
    $("#requestForm").submit(function (event) {
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
        const foodName = $("#food_name");
        const qty = $("#qty");
        const desc = $("#description");
        const SelectType = $("#type");
        const req_date = $("#req_date");

        if (foodName.val() == "") {
            showError("Food name is required");
            return false;
        }
        if (SelectType.val() === "-1") {
            // Assuming '-1' is the default/invalid option
            showError("Please select a valid option");
            return false;
        }
        if (qty.val() == "") {
            showError("Quantity is required");
            return false;
        }
        if (req_date.val() == "") {
            showError("Date is required");
            return false;
        }
        if (desc.val() == "") {
            showError("Description is required");
            return false;
        } 

        showSuccess();
        return true;
    };
});

$(document).ready(function () {
    // add new bus
    $("#checkQR").submit(function (event) {
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
        const img = $("#image");

        if (img[0].files.length == 0) {
            showError("QR code is required");
            return false;
        }
        showSuccess();
        return true;
    };
});