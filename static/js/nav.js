const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

navToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
    navToggle.classList.toggle("active");

    const isOpen = navLinks.classList.contains("active");
    navToggle.setAttribute("aria-expanded", isOpen);
});