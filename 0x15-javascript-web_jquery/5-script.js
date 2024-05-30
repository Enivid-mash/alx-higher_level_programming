$(document).ready(function () {
  $("#add_item").on("click", function () {
    $("<li>New Item</li>").insertBefore("ul.my_list li:first-child");
  });
});

