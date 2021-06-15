from app.util import get_youtube_videos_in_interval
from datetime import datetime
import asyncio
from app import asgi_app, db
from app.models import *

db.create_all()


async def run():
    youtube_videos = await get_youtube_videos_in_interval()

    async for youtube_video in youtube_videos:
        for data in youtube_video:

            video_present = YoutubeVideo.query.filter_by(
                title=data['title']).first()
            if not video_present:
                temp_video = YoutubeVideo()
                temp_video.title = data['title']
                temp_video.description = data['description']
                temp_video.publish_date = datetime.strptime(
                    data['publish_date'], '%Y-%m-%dT%H:%M:%SZ')
                temp_video.thumbnail_url_default = data['thumbnail_url_default']
                temp_video.thumbnail_url_medium = data['thumbnail_url_medium']
                temp_video.thumbnail_url_high = data['thumbnail_url_high']
                db.session.add(temp_video)
                db.session.commit()
                print('Stored in database')
            else:
                print('Already present in database')


asyncio.run(run())
