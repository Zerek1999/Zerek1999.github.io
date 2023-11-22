

// 使用JavaScript监听滚动事件
window.addEventListener("scroll", function () {
    var navbar = document.getElementById("nav-bar");
    if (window.scrollY > 0) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});














