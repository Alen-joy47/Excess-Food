function addFood() {
  $("#heading").text("Add Food");
  $("#addFoodModal").modal("show");
}

function editProfile() {
  $("#heading").text("Edit Profile");
  $("#editProfileModal").modal("show");
}

function editProfile1() {
  $("#heading").text("Edit Food");
  $("#editFoodModal").modal("show");
}

function editFood(id) {  
  $.ajax({
    type: "GET",
    url: "/get_food_details/",
    data: {
      id: id,
    },
    dataType: "json",
    success: function (data) {
      console.log("Food Details:", data);


      // Assuming you have a form with the following input fields
      $("#id").val(data.id);
      $("#name").val(data.name);
      $("#type").val(data.type);
      // $("#ingredients").val(data.ingredients);
      $("#qty").val(data.quantity);
      $("#description").val(data.description);
      $("#images").val(data.image);

      // if (data.ingredients && data.ingredients.length > 0) {
      //   // Iterate through the array and check the corresponding checkboxes
      //   for (var i = 0; i < data.ingredients.length; i++) {
      //     var ingredientValue = data.ingredients[i];
      //     // Check the checkbox with the corresponding value
      //     $("input[name='ingredients'][value='" + ingredientValue + "']").prop("checked", true);
      //   }
      // }


      // $("#foodImage").attr("src", data.image);

      $("#editFoodModal").modal("show");
    },
    error: function (error) {
      console.log("Error:", error);
    },
  });
}

  function orderNow() {
    $("#heading").text("Order Food");
    $("#orderFoodModal").modal("show");
  }