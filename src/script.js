document.querySelector("#food-img").addEventListener("click", function () {
  window.location.href = "https://omnifood-tera.netlify.app/";
});

document.querySelector("#pw-img").addEventListener("click", function () {
  window.location.href =
    "https://github.com/terabvte/web_learn?tab=readme-ov-file#password-generator";
});

// script.js
document.addEventListener("DOMContentLoaded", function () {
  const hamburgerButton = document.getElementById("hamburger-button");
  const closeMenuButton = document.getElementById("close-menu");
  const mobileMenu = document.getElementById("mobile-menu");

  // Function to open menu
  function openMenu() {
    mobileMenu.classList.remove("hidden");
    mobileMenu.classList.add("block");
    document.body.classList.add("overflow-hidden");
  }

  // Function to close menu
  function closeMenu() {
    mobileMenu.classList.remove("block");
    mobileMenu.classList.add("hidden");
    document.body.classList.remove("overflow-hidden");
  }

  hamburgerButton.addEventListener("click", openMenu);
  closeMenuButton.addEventListener("click", closeMenu);

  // Handle resize events
  window.addEventListener("resize", function () {
    // If window width is lg breakpoint (1024px) or larger and menu is open, close it
    if (window.innerWidth >= 1024 && mobileMenu.classList.contains("block")) {
      closeMenu();
    }
  });
});
