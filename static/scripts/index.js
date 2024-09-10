document.addEventListener("DOMContentLoaded", function () {
  var modal = document.getElementById("myModal");
  var btns = document.querySelectorAll(".add-card");
  var span = document.getElementsByClassName("close")[0];

  btns.forEach(function (btn) {
    btn.onclick = function () {
      console.log("Clicou no botão");
      modal.style.display = "block";
    };
  });

  if (span) {
    span.onclick = function () {
      modal.style.display = "none";
    };
  }

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
});
