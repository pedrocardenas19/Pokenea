from flask import Blueprint, jsonify, render_template
from .models import POKENEAS
from .utils import get_random_pokenea, get_container_id

main = Blueprint('main', __name__)

@main.route('/api/random_pokenea', methods=['GET'])
def random_pokenea():
    pokenea = get_random_pokenea()
    response = {
        'id': pokenea.id,
        'nombre': pokenea.nombre,
        'altura': pokenea.altura,
        'habilidad': pokenea.habilidad,
        'container_id': get_container_id()
    }
    return jsonify(response)

@main.route('/random_pokenea', methods=['GET'])
def show_random_pokenea():
    pokenea = get_random_pokenea()
    return render_template('pokenea.html', pokenea=pokenea, container_id=get_container_id())
