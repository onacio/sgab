from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from apps.auth.auth import login_required
from apps.pedidos.model import Pedidos, ItensPedido
from database import db
from datetime import date, time

pedidos_bp = Blueprint('pedidos_bp', __name__, url_prefix='/pedidos', template_folder='templates', static_folder='static')

@pedidos_bp.route('/', methods=['GET', 'POST'])
@login_required('usuario')
def home():
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        item = request.form.get('item')
        quantidade = request.form.get('quantidade')
        justificativa = request.form.get('justificativa')
        solicitante = session['lotacao']

        data = date.today()
        hora = time()  

        pedidos = Pedidos(data, hora, item, categoria, quantidade, solicitante, justificativa)
        db.session.add(pedidos)
        db.session.commit()

        flash('Pedido realizado com sucesso!!!', 'success')

        return redirect(url_for('pedidos_bp.home'))
    
    pedidos = Pedidos.query.all()
    # Consulta para agrupar as categorias da tabela itens_pedido
    categorias = db.session.query(ItensPedido.categoria).group_by(ItensPedido.categoria).all()
    # Consulta para agrupar as descrições da tabela itens_pedido
    itens = db.session.query(ItensPedido.descricao).group_by(ItensPedido.descricao).all()
    return render_template('pedidos/pedidos.html', pedidos=pedidos, categorias=categorias, itens=itens)


@pedidos_bp.route('/itens', methods=['GET', 'POST'])
@login_required('master')
def cadastrar_itens():    
    if request.method == 'POST':
        item_id = request.form.get('id')
        if item_id:
            item = ItensPedido.query.get(item_id)
            
            item.descricao = request.form.get('descricao')
            item.categoria = request.form.get('categoria')
            ativo_atual = request.form.get('ativo')
            item.ativo = int(ativo_atual)

            db.session.commit()

            flash('Item atualizado com sucesso!!!', 'success')
            
        else:
            descricao = request.form.get('descricao')
            categoria = request.form.get('categoria')
            ativo_atual = request.form.get('ativo')
            ativo = int(ativo_atual)

            itens = ItensPedido(descricao, categoria, ativo)
            db.session.add(itens)
            db.session.commit()

            flash('Item cadastrado com sucesso!!!', 'success')

        return redirect(url_for('pedidos_bp.cadastrar_itens'))
    
    itens = ItensPedido.query.all()
    return render_template('pedidos/itens.html', itens=itens)

@pedidos_bp.route('/descricao_por_categoria/<categoria>')
def descricao_por_categoria(categoria):
    # Consulta para agrupar descrições por categoria específica
    resultados = db.session.query(
        ItensPedido.descricao        
    ).filter((ItensPedido.categoria == categoria) & (ItensPedido.ativo == 1)).group_by(ItensPedido.descricao).all()

    # Transformando os resultados em um formato de lista de dicionários
    dados = [{'descricao': resultado.descricao,} for resultado in resultados]

    # Retornando os dados como JSON
    return jsonify(dados)

@pedidos_bp.route('/item/excluir/<int:id>', methods=['POST'])
@login_required('master')
def excluir_item(id):
    item = ItensPedido.query.get(id)

    try:        
        db.session.delete(item)
        db.session.commit()
        flash('Item deletado com sucesso!!!', 'success')
        return redirect(url_for('pedidos_bp.cadastrar_itens'))
    except:
        flash('Erro ao deletar item!', 'error')