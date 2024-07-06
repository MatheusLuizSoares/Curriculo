

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');

  form.addEventListener('submit', function(event) {
      const nome = form.querySelector('#nome').value.trim();
      const email = form.querySelector('#email').value.trim();

      if (nome === '') {
          event.preventDefault();
          document.querySelector('#error-nome').textContent = 'Campo obrigatório.';
      }

      if (email === '') {
          event.preventDefault();
          document.querySelector('#error-email').textContent = 'Campo obrigatório.';
      }
  });

 
  form.addEventListener('input', function(event) {
      if (event.target.tagName.toLowerCase() === 'input' || event.target.tagName.toLowerCase() === 'textarea') {
          const id = event.target.id;
          const errorId = `error-${id}`;
          const errorElement = document.querySelector(`#${errorId}`);
          if (errorElement) {
              errorElement.textContent = '';
          }
      }
  });
});
