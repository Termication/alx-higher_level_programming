// Make a GET request to the specified URL. When the data is received, set the text of the DIV with id "character" to the name from the received data.
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
