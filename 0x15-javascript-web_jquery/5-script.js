// When the DIV with id "add_item" is clicked, append a new <li> element with the text "Item" to the UL with class "my_list".
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
