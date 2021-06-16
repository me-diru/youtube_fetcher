from . import api_key
from googleapiclient.discovery import build
import asyncio
from os import abort


async def get_youtube_videos_in_interval(given_interval=100):
    '''
        This function fetches latest youtube video details related to cricket
    '''

    async def call_data():

        while(True):
            try:

                youtube = build('youtube', 'v3', developerKey=api_key)
                request = youtube.search().list(
                    part='snippet',
                    type='video',
                    # this is search string which gets us the results
                    q='cricket',
                    order='date',
                    # considering our end users who are below 18 :)
                    safeSearch='moderate',
                    # limiting to 50 as no quantity is mentioned
                    maxResults=50
                )

                response = request.execute()

                captured_data = list()

                for youtube_video_data in response["items"]:
                    temp_data = dict()
                    temp_data['title'] = youtube_video_data['snippet']['title']
                    temp_data['description'] = youtube_video_data['snippet']['description']
                    temp_data['publish_date'] = youtube_video_data['snippet']['publishedAt']
                    temp_data['thumbnail_url_default'] = youtube_video_data['snippet']['thumbnails']['default']['url']
                    temp_data['thumbnail_url_medium'] = youtube_video_data['snippet']['thumbnails']['medium']['url']
                    temp_data['thumbnail_url_high'] = youtube_video_data['snippet']['thumbnails']['high']['url']

                    captured_data.append(temp_data)

                yield captured_data
                await asyncio.sleep(given_interval)
            except Exception as ex:
                print(ex.__class__.__doc__)
                exit(1)

    return call_data()


def get_paginated_list(klass, url, start, limit):
    # check if page exists
    youtube_videos_data = youtube_videos_data = klass.query.order_by(
        klass.publish_date.desc()).all()
    results = list()
    for youtube_video_data in youtube_videos_data:
        youtube_video_data = youtube_video_data.__dict__
        del youtube_video_data['_sa_instance_state']
        results.append(youtube_video_data)

    count = len(results)
    if (count < start):
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj
