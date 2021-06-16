from . import app, db
from .models import *
from flask import request, jsonify, Response
from datetime import datetime
from .util import get_paginated_list
from sqlalchemy import or_, and_


@app.route('/v1/fetch_stored_youtube_videos', methods=['GET'])
def fetch_youtube_videos():
    '''
        A GET API which returns the stored video data in a paginated 
        response sorted in descending order of published datetime.
    '''

    return jsonify(get_paginated_list(
        YoutubeVideo,
        '/api/v2/events/page',
        start=int(request.args.get('start', 1)),
        limit=int(request.args.get('limit', 5))
    ))


@app.route('/v1/search', methods=['GET'])
def search_data():
    ''' 
        This API endpoint seaches the relevant Youtube videos wrt their
        Title or Description names 
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
