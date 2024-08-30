document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.edit-btn-pedido');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const id = button.getAttribute('data-id');
            const descricao = button.getAttribute('data-descricao');
            const categoria = button.getAttribute('data-categoria');            
            // const ativo = button.getAttribute('data-ativo');            

            document.getElementById('id').value = id;
            document.getElementById('descricao').value = descricao;
            document.getElementById('categoria').value = categoria;
            // document.getElementById('ativo').value = ativo;   
            
            // Altera o texto do botão na modal para "Atualizar"
            document.getElementById('btn-salvar').textContent = 'Atualizar';
        });
    });
});