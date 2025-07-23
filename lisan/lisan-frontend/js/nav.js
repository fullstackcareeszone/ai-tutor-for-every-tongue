// js/nav.js

document.addEventListener("DOMContentLoaded", () => {
    const currentPage = window.location.pathname.split("/").pop();
    const links = document.querySelectorAll("nav a");

    links.forEach(link => {
        const href = link.getAttribute("href");
        if (href === currentPage) {
            link.classList.add("font-bold", "text-blue-500");
        }
    });
});
