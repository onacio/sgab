// código do botão excluir itens
$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botão que acionou o modal    
    var id = button.data('id'); // Extrai rota e ID do registro a ser excluído
    var form = $('#deleteForm');    
    var action = id; // Define a rota de exclusão com o ID        
    form.attr('action', action);
});


function mensagem(msg){
    alert(msg)
}