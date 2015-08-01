from flask_restful import Resource
from flask import jsonify
from app import db
from app.models import Url

class UrlResource(Resource):
  def get(self, id):
    url = Url.query.get(id)
    if url is None:
      return { 'Error': 'URL does not exist' }, 404

    return jsonify(url.json())
