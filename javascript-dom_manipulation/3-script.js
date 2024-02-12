const header = document.querySelector("header")
const tooglehead = document.querySelector("#toggle_header")
tooglehead.addEventListener("click", () => {
    const tooglegreen = header.classList.contains("green")
    if (tooglegreen) {
        header.classList.replace("green", "red")
    } else {
        header.classList.replace("red", "green")
    }
})