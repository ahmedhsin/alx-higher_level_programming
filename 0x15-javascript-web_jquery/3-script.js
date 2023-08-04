const redHeader = $('DIV#red_header')
const header = $('header');
redHeader.on('click', ()={
	header.addClass('red')
})
