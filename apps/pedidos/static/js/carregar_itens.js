document.addEventListener('DOMContentLoaded', function() {
    const categoriaSelect = document.getElementById('categoria');
    const descricaoSelect = document.getElementById('descricao');

    // Função para buscar e preencher o select de descrição
    function buscarDescricoes(categoria) {
        if (categoria) {
            fetch(`/descricao_por_categoria/${categoria}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro na solicitação');
                    }
                    return response.json();
                })
                .then(data => {
                    // Limpar opções anteriores
                    descricaoSelect.innerHTML = '<option value="">Selecione uma opção</option>';

                    // Adicionar novas opções ao select de descrição
                    data.forEach(item => {
                        const option = document.createElement('option');
                        option.value = item.descricao;
                        option.textContent = `${item.descricao} (${item.total})`;
                        descricaoSelect.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error('Erro ao buscar dados:', error);
                });
        } else {
            // Limpar o select de descrição se nenhuma categoria for selecionada
            descricaoSelect.innerHTML = '<option value="">Selecione uma opção</option>';
        }
    }

    // Adicionar evento ao select de categoria para buscar descrições ao mudar a categoria
    categoriaSelect.addEventListener('change', function() {
        const categoriaSelecionada = categoriaSelect.value;
        buscarDescricoes(categoriaSelecionada);
    });
});
