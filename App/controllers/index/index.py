import datetime

from flask import render_template, Blueprint

from App.controllers.common.utils import to_json
from App.models.models import Concert

index_index = Blueprint('index_index', __name__, )


@index_index.route('', methods=['GET', 'POST'])
@index_index.route('index/', methods=['GET', 'POST'])
@index_index.route('index/index/', methods=['GET', 'POST'])
@index_index.route('index/index.html', methods=['GET', 'POST'])
def index():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    events = Concert.query.filter(Concert.eventDate == today).order_by(Concert.id.desc()).all()

    Upcoming = Concert.query.filter(Concert.eventDate > today).order_by(Concert.id.desc()).all()

    rows = Concert.query.filter().order_by(Concert.id.desc()).all()
    categorys = []

    datas = []

    for row in rows:
        item = to_json(row)

        if item['category'] not in categorys:
            categorys.append(item['category'])
            datas.append(item)

    return render_template('index/index.html', **{'events': events, 'Upcoming': Upcoming, 'datas': datas})
