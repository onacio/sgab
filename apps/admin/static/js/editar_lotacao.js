document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.edit-btn-lotacao');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const id = button.getAttribute('data-id');
            const nome = button.getAttribute('data-nome');
            const ativo = button.getAttribute('data-ativo');            

            document.getElementById('id').value = id;
            document.getElementById('nome').value = nome;
            document.getElementById('ativo').value = ativo;   
            
            // Altera o texto do botão na modal para "Atualizar"
            document.getElementById('btn-salvar').textContent = 'Atualizar';
        });
    });
});