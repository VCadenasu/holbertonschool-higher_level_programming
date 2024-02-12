const Item = "<li>Item</li>"
const list = document.querySelector(".my_list")
const add = document.querySelector("#add_item")

add.addEventListener("click", () => {
    list.insertAdjacentHTML("beforeend", Item)
})