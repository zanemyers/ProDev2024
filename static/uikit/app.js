let alertWrappers = document.querySelectorAll('.alert');

alertWrappers.forEach(alertWrapper => {
  let closeButton = alertWrapper.querySelector('.alert__close');

  if (closeButton) {
    closeButton.addEventListener('click', () => {
      alertWrapper.style.display = 'none';
    });
  }
});
