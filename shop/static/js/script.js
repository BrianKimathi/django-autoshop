const rightMenu = document.getElementById("right-menu");
const btm = document.getElementById("btm");


rightMenu.addEventListener("click", () => {
  if (btm.classList.contains("active")) {
    btm.classList.remove("active");
  } else {
    btm.classList.add("active");
  }
});

