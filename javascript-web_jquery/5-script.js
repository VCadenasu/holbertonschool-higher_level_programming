$(document).ready(() => {
    const unorderList = $('UL.my_list');
    $('DIV#add_item').click(() => {
        const listItem = '<li>Item</li>';
        unorderList.append(listItem);
    });
})