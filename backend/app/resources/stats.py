from flask_restful import Resource
from flask import jsonify
from app import db
from app.models import Url, Hit
from sqlalchemy import func

class StatsResource(Resource):
  def get(self, url_id):
    url = Url.query.get(url_id)
    if url is None:
      return { 'Error': 'URL does not exist' }, 404

    hits = db.session.query(func.count(Hit.id)).filter_by(url_id = url_id).scalar()

    referrers = db.session.query(func.coalesce(Hit.referrer, ''), func.count()) \
                  .filter_by(url_id = url_id).group_by(Hit.referrer).all()

    user_agents = db.session.query(func.coalesce(Hit.user_agent, ''), func.count()) \
                    .filter_by(url_id = url_id).group_by(Hit.user_agent).all()

    return jsonify(
      id = url.id,
      short_url = url.short_url,
      destination_url = url.destination_url,
      hit_count = hits,
      referrers = [{tuple[0]: tuple[1]} for tuple in referrers],
      user_agents = [{tuple[0]: tuple[1]} for tuple in user_agents]
    )
