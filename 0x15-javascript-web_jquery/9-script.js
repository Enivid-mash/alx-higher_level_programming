$(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    method: "GET",
    dataType: "json",
    success: function(data) {
      $("DIV#hello").text(data.hello);
    }
  });
});

