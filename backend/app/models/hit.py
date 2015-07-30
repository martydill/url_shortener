import datetime
from app import db

class Hit(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  created_date = db.Column(db.DateTime, default = datetime.datetime.utcnow)
  referrer = db.Column(db.Text)
  user_agent = db.Column(db.Text)
  ip_address = db.Column(db.Text)
  url_id = db.Column(db.Integer, db.ForeignKey('url.id'))

  def json(self):
    return {
      'id': self.id,
      'created_date': self.created_date,
      'referrer': self.referrer,
      'user_agent': self.user_agent,
      'ip_address': self.ip_address
    }
