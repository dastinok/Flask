const inputList = document.querySelectorAll(".input");
inputList.forEach((input) => {
  input.addEventListener("input", (e) => {
    const text = e.target.value;
    if (text.length > 0) {
      input.parentElement.classList.add("is_active");
    }
  });
});


