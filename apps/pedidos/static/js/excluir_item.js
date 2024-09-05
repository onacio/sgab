// código do botão excluir itens
$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botão que acionou o modal
    var id = button.data('id'); // Extrai o ID do registro    
    console.log('Registro ID:', id)

    var form = $('#deleteForm');
    //var action = '/pedidos/item/excluir/' + id; // Define a rota de exclusão com o ID    
    var action = id; // Define a rota de exclusão com o ID    
    console.log(id)
    form.attr('action', action);
});