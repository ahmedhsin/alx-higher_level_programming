$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  const movies = $('UL#list_movies');
  $.each(data.results, function (i, item) {
    const li = '<li>' + item.title + '</li>';
    movies.append(li);
  });
});
