document.querySelectorAll('input[type="radio"]').forEach(radio => {
  radio.addEventListener('change', function () {
    const selectedRole = this.getAttribute("data-value");
    this.setAttribute("value", selectedRole);
    const form = document.querySelector('form#user-type');
    form.submit();
  });
});
