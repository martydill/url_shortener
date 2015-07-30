from flask_restful import Resource
from flask import request
from app import db
from app.models import Url, Hit

class ShortenedUrlsResource(Resource):
  def get(self, short_url):
    url = Url.query.filter_by(short_url = short_url).first()
    if url is None:
      return { 'Error': 'URL does not exist' }

    hit = Hit(url_id = url.id)
    hit.user_agent = request.headers.get('User-Agent')
    hit.referrer = request.referrer
    hit.ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    db.session.add(hit)
    db.session.commit()
    return {}, 301, { 'Location': url.destination_url }
