$(document).ready(() => {
    const headerElement = $('header');
    $('DIV#toggle_header').click(() => {
        headerElement.toggleClass('red green');
    });
})
