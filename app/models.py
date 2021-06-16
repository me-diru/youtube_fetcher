from app import db


class YoutubeVideo(db.Model):
    # youtube video model to store data in a structured format in the database
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    thumbnail_url_default = db.Column(db.Text())
    thumbnail_url_medium = db.Column(db.Text())
    thumbnail_url_high = db.Column(db.Text())

    def __repr__(self):
        return 'The video title is: {title} \n  description: {description}'.format(title=self.title, description=self.description)
