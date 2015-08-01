from flask import jsonify
from flask_restful import Resource, reqparse
from app import db
from app.models import Hit, Url

parser = reqparse.RequestParser()

parser.add_argument('count', default = 25, type = int)
parser.add_argument('page', default = 1, type = int)
parser.add_argument('order_by', default = 'id asc')

class HitsResource(Resource):
  def get(self, url_id):
    url = Url.query.get(url_id)
    if url is None:
      return { 'Error': 'URL does not exist' }, 404

    args = parser.parse_args()
    hits = []
    paged = Hit.query.filter_by(url_id = url_id).order_by(args['order_by']).paginate(args['page'], args['count'], False)
    for hit in paged.items:
      hits.append(hit.json())

    return jsonify(page = args['page'], total = paged.total, hits = hits)
