// Make a GET request to the specified URL. When the data is received, append a list item for each movie title to the UL with id "list_movies".
$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
