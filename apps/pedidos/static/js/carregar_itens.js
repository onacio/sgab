document.addEventListener('DOMContentLoaded', function() {
    const categoriaSelect = document.getElementById('categoria');
    const itemSelect = document.getElementById('item');

    categoriaSelect.addEventListener('change', function() {
        const categoria = this.value;

        // Verifica se alguma categoria foi selecionada
        if (categoria) {
            // Faz a requisição AJAX para buscar os itens da categoria
            fetch(`/pedidos/descricao_por_categoria/${categoria}`)
                .then(response => response.json())
                .then(data => {
                    // Limpa as opções existentes no select de itens
                    itemSelect.innerHTML = '';
                    
                    // Adiciona uma opção vazia
                    const emptyOption = document.createElement('option');
                    emptyOption.value = '';
                    emptyOption.textContent = '';
                    itemSelect.appendChild(emptyOption);

                    // Preenche o select de itens com os dados retornados
                    data.forEach(item => {
                        const option = document.createElement('option');
                        option.value = item['descricao'];
                        option.textContent = item['descricao'];
                        itemSelect.appendChild(option);                        
                    });
                })
                .catch(error => console.error('Erro:', error));
                
        } else {
            // Se nenhuma categoria for selecionada, limpa o select de itens
            itemSelect.innerHTML = '<option value=""></option>';
        }
    });
});
