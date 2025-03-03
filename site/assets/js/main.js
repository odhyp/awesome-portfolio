document.addEventListener("scroll", () => {
  headerScrollEffect();
});

function headerScrollEffect() {
  const scrollPoint = 150;
  const pageHeader = document.getElementById("header");

  if (window.scrollY > scrollPoint) {
    pageHeader.classList.remove("bg-transparent");
    pageHeader.classList.add("bg-neutral-100", "shadow-md");
  } else {
    pageHeader.classList.add("bg-transparent");
    pageHeader.classList.remove("bg-neutral-100", "shadow-md");
  }
}
