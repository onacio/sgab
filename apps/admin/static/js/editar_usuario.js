document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.edit-btn-usuario');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Dados recebido da tabela de lotação
            const id = button.getAttribute('data-id');
            const nome = button.getAttribute('data-nome');
            const sobrenome = button.getAttribute('data-sobrenome');
            const usuario = button.getAttribute('data-usuario');
            const senha = button.getAttribute('data-senha');
            const email = button.getAttribute('data-email');
            const nivel = button.getAttribute('data-nivel');
            const lotacao = button.getAttribute('data-lotacao');
            const ativo = button.getAttribute('data-ativo');

            // Esses códigos preenche os campos com os dados obtidos do botão editar na tabela
            document.getElementById('id').value = id;
            document.getElementById('nome').value = nome;
            document.getElementById('sobrenome').value = sobrenome;
            document.getElementById('usuario').value = usuario;
            document.getElementById('senha').value = senha;
            document.getElementById('email').value = email;
            document.getElementById('nivel').value = nivel;
            document.getElementById('lotacao').value = lotacao;
            document.getElementById('ativo').value = ativo;

            // Altera o texto do botão na modal para "Atualizar"
            document.getElementById('btn-salvar').textContent = 'Atualizar';
        });
    });
});