import asyncio
from json import loads
from requests import get
from .models import YTApiKey, VideoDetails
from datetime import datetime


# Function to insert data into db
def data_insert_to_db(incoming_data):
    """
    Function to insert video data to database.
    """

    print('inserting data')

    try:
        for data in incoming_data:

            changed_time_fmt = datetime.strptime(data["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")

            to_be_inserted = {
                "videoId": data["id"]["videoId"],
                "title": data["snippet"]["title"],
                "description": data["snippet"]["description"],
                "publishedAt": changed_time_fmt,
                "thumbnailUrl": data["snippet"]["thumbnails"]["medium"]["url"],
                "channelName": data["snippet"]["channelTitle"]
            }

            # Checks videoId already present or not.
            VideoDetails.objects.update_or_create(videoId=data["id"]["videoId"], defaults=to_be_inserted)
    except Exception as e:
        print(e)

# Async function for getting data from YT API
async def get_data_from_youtube():
    """
    Function to get data from Youtube using API.
    """

    while True:
            apiKeyObject = YTApiKey.objects.filter().order_by('timesUsed').first()
            query = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&order=date&q=cricket&key={apiKeyObject.apiKey}"
            print(query)
            try:
                res = get(query)
            except Exception as e:
                print(e)

            # Checks if data is fetched or not
            if res.status_code == 200:
                apiKeyObject.timesUsed += 1
                apiKeyObject.save()
                print(apiKeyObject)
                #obj = YTApiKey.objects.get(id=apiKeyObject.id)
                #obj.timesUsed = 1 + apiKeyObject.timesUsed

                res = res.content.decode("utf-8")
                print('Received data from YT')
                incoming_data = loads(res)
                data_insert_to_db(incoming_data["items"])

            else:
                print(res.text)

            await asyncio.sleep(60)

# Function for initialising Async Loop
def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_data_from_youtube())
