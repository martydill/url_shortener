from app import db
import string
import random
import datetime

URL_LENGTH = 5
URL_CHARACTERS = string.ascii_letters + string.digits

def make_me_a_short_url(context):
  return ''.join(random.choice(URL_CHARACTERS) for _ in range(URL_LENGTH))

class Url(db.Model):

  id = db.Column(db.Integer, primary_key = True)
  created_date = db.Column(db.DateTime, default = datetime.datetime.utcnow)
  short_url = db.Column(db.Text, unique = True, default = make_me_a_short_url)
  destination_url = db.Column(db.Text)
  hits = db.relationship("Hit", backref="url")

  def __init__(self, url):
    if url is not None and not url.startswith('http://') and not url.startswith('https://'):
      url = "http://" + url
    self.destination_url = url

  def json(self):
    return {
      'id': self.id,
      'short_url': self.short_url,
      'created_date': self.created_date,
      'destination_url': self.destination_url
    }
