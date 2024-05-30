$(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function(data) {
      data.results.forEach(function(film) {
        $("<li>").text(film.title).appendTo("ul#list_movies");
      });
    }
  });
});

