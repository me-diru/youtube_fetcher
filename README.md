# youtube_fetcher

an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Installation Steps

- Create a virtual environment ```python3 -m venv venv```
- Install required dependencies using ```pip3 install -r requirements.txt```
- To run the API, use ```flask run```
- To run the background process of storing latest youtube video details, open other terminal and run ```hypercorn background_process:asgi_app```
- **NOTE:** Specify your own API key if limit reaches


## Checking application 


The API comes with two endpoints:

- 
- ```/v1/search``` To search matching the youtube videos data in the database
    - Test using 
    ``` crul 
    ```
