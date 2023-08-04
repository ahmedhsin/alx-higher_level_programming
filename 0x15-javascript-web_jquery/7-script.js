$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status) {
  const char = $('DIV#character');
  char.text(data.name);
});
