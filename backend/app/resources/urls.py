from flask import jsonify
from flask_restful import Resource, reqparse
from sqlalchemy import exc
from app import db
from app.models import Url

parser = reqparse.RequestParser()
parser.add_argument('url')

class UrlsResource(Resource):
  def get(self):
    urls = []
    for url in Url.query.all():
      urls.append(url.json())

    return jsonify(urls = urls)

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

