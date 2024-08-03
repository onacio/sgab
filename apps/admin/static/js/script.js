document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.edit-btn');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const id = button.getAttribute('data-id');
            const nome = button.getAttribute('data-nome');
            const sobrenome = button.getAttribute('data-sobrenome');
            const usuario = button.getAttribute('data-usuario');
            const senha = button.getAttribute('data-senha');
            const email = button.getAttribute('data-email');
            const nivel = button.getAttribute('data-nivel');
            const lotacao = button.getAttribute('data-lotacao');
            const ativo = button.getAttribute('data-ativo');

            document.getElementById('usuario_id').value = id;
            document.getElementById('nome').value = nome;
            document.getElementById('sobrenome').value = sobrenome;
            document.getElementById('usuario').value = usuario;
            document.getElementById('senha').value = senha;
            document.getElementById('email').value = email;
            document.getElementById('nivel').value = nivel;
            document.getElementById('lotacao').value = lotacao;
            document.getElementById('ativo').value = ativo;
        });
    });
});