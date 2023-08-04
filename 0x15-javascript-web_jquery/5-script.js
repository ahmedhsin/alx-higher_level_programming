const add = $('DIV#add_item');
const list = $('UL.my_list');
add.on('click', function () {
  const item = '<li>Item</li>';
  list.append(item);
});
