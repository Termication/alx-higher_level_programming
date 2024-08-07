// Wait for the document to be fully loaded
$(document).ready(function () {
  // Add a click event listener to the element with id 'add_item'
  $('DIV#add_item').click(function () {
    // Append a new list item to the unordered list with class 'my_list'
    $('UL.my_list').append('<li>Item</li>');
  });
  
  // Add a click event listener to the element with id 'remove_item'
  $('DIV#remove_item').click(function () {
    // Remove the last list item from the unordered list with class 'my_list'
    $('UL.my_list li:last').remove();
  });
  
  // Add a click event listener to the element with id 'clear_list'
  $('DIV#clear_list').click(function () {
    // Remove all list items from the unordered list with class 'my_list'
    $('UL.my_list').empty();
  });
});
