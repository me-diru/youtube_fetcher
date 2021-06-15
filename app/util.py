from . import api_key
from googleapiclient.discovery import build
import asyncio


async def get_youtube_videos_in_interval(given_interval=100):

    async def call_data():

        while(True):
            try:

                youtube = build('youtube', 'v3', developerKey=api_key)
                request = youtube.search().list(
                    part='snippet',
                    type='video',
                    q='cricket',
                    order='date',
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
            except:
                print('API key has been exhausted, renew it please')
                exit(1)

    return call_data()
