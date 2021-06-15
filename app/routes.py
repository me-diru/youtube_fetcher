from . import app, db
from .models import *
from flask import request, jsonify, Response
from datetime import datetime
from .util import get_youtube_videos_in_interval
from sqlalchemy import or_


@app.route('/', methods=['GET'])
async def test():
    youtube_videos = await get_youtube_videos_in_interval()
    print(youtube_videos)
    async for youtube_video in youtube_videos:
        for data in youtube_video:
            print(data, '\n\n')
        print(datetime.now())

    return Response(
        mimetype='application/json',
        status=200
    )


@app.route('/v1/fetch_stored_youtube_videos', methods=['GET'])
def fetch_youtube_videos():
    '''
        A GET API which returns the stored video data in a paginated 
        response sorted in descending order of published datetime.
    '''
    youtube_videos_data = YoutubeVideo.query.order_by(
        YoutubeVideo.publish_date.desc()).paginate(1, 5, False).items

    result_data = list()
    for youtube_video_data in youtube_videos_data:
        youtube_video_data = youtube_video_data.__dict__
        del youtube_video_data['_sa_instance_state']
        result_data.append(youtube_video_data)

    return jsonify(result_data)


@app.route('/v1/search', methods=['GET'])
def search_data():
    ''' 
        This API endpoint seaches the relevant Youtube videos wrt their
        Title and Description names 
    '''
    input_data = request.args

    # creating regex which machtes with anything containing given input as substring
    search = "%{}%".format(input_data["search_string"])

    # fetch relevant details from database
    relevant_videos = YoutubeVideo.query.filter(
        or_(YoutubeVideo.title.like(search), YoutubeVideo.description.like(search))).all()
    result_data = list()
    for youtube_video_data in relevant_videos:
        youtube_video_data = youtube_video_data.__dict__
        del youtube_video_data['_sa_instance_state']
        result_data.append(youtube_video_data)
    return jsonify(result_data)
