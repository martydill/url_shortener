from flask_restful import Resource
from flask import jsonify
from app import db
from app.models import Hit, Url

class HitsResource(Resource):
  def get(self, url_id):
    url = Url.query.get(url_id)
    if url is None:
      return { 'Error': 'URL does not exist' }, 404

    hits = []
    for hit in Hit.query.filter_by(url_id = url_id):
      hits.append(hit.json())

    print hits
    return jsonify(hits = hits)
