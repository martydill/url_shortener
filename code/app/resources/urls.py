from flask import jsonify
from flask_restful import Resource, reqparse
from sqlalchemy import exc
from app import db
from app.models import Url

parser = reqparse.RequestParser()
parser.add_argument('url')
parser.add_argument('count', default = 25, type = int)
parser.add_argument('page', default = 1, type = int)
parser.add_argument('order_by', default = 'id asc')

class UrlsResource(Resource):
  def get(self):
    args = parser.parse_args()
    urls = []
    paged = Url.query.order_by(args['order_by']).paginate(args['page'], args['count'], False)
    for url in paged.items:
      urls.append(url.json())

    return jsonify(page = args['page'], total = paged.total, urls = urls)

  def post(self):
    args = parser.parse_args()
    destination = args['url']
    if destination is None:
      return { 'Error': 'url is a required parameter' }, 400

    # The odds of two urls getting the same random hash are kinda low, given that
    # there are 62 ^ 5 possibilities. If it happens, let's just try again.
    while True:
      try:
        url = Url(destination)
        db.session.add(url)
        db.session.commit()
        return jsonify(url.json())
      except exc.IntegrityError:
        db.session.rollback()
      except:
        return { 'Error': 'URL Creation failed' }

