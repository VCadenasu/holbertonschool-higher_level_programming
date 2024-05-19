$(document).ready(() => {
    const headerElement = $('header');
    $('DIV#update_header').click(() => {
        headerElement.text('New Header!!!');
    });
})
