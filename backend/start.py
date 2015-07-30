from flask_restful import Resource, Api
from app import app, db
from app.models import Url, Hit
from app.resources import UrlResource, UrlsResource, HitsResource, ShortenedUrlsResource, StatsResource

db.create_all()

api = Api(app)

api.add_resource(ShortenedUrlsResource, '/<string:short_url>')
api.add_resource(UrlsResource, '/urls')
api.add_resource(UrlResource, '/urls/<string:id>')
api.add_resource(HitsResource, '/urls/<string:url_id>/hits')
api.add_resource(StatsResource, '/urls/<string:url_id>/stats')

app.run(debug = True)
