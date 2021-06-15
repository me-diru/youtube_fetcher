from app import db

# Creating db models by taking advantage of already loaded tables in database


class YoutubeVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    thumbnail_url_default = db.Column(db.Text())
    thumbnail_url_medium = db.Column(db.Text())
    thumbnail_url_high = db.Column(db.Text())

    def __repr__(self):
        return 'The video title is: {title} \n  description: {description}'.format(title=self.title, description=self.description)
