document.getElementById('menu').addEventListener('click', scrollToElement);
function scrollToElement(e) {
element = document.getElementById("section-menu")
element.scrollIntoView(true);
}