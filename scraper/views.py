from django.shortcuts import render
from django.views import View
from .models import Video, Video_Chapter
import requests
import re
from bs4 import BeautifulSoup


class AddVideoView(View):
    template_name = "add_video.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        url = request.POST.get('url')
        if 'youtube.com' in url:
            # Follow the YouTube URL and scrape details
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.find('meta', property='og:title')['content']
            description = soup.find('meta', property='og:description')['content']

            # Save the scraped data
            video, created = Video.objects.update_or_create(
                url=url,
                defaults={'title': title, 'description': description},
                )
            
            # Extract chapters from video description
            chapters = self.extract_chapters_in_description(description)

            # Save chapters in the database
            for timestamp, chapter_title in chapters:
                video.chapter_set.create(timestamp=timestamp, title=chapter_title)

            return render(request, 'add_video.html', {'video': video, 'video_chapters': video.video_chapter_set.all()})

        return render(request, 'add_video.html')

    def extract_chapters_in_description(self, description):
        description_chapters = []
        lines = description.split('\n')
        print(description_chapters)

        for line in lines:
            # Look for lines starting with a timestamp like '0:00'
            if re.match(r'^\d+:\d+', line):
                # Split the line into timestamp and title
                parts = line.split(' ', 1)
                timestamp = parts[0]
                chapter_title = parts[1] if len(parts) > 1 else ""

                description_chapters.append((timestamp, chapter_title))

        return description_chapters
    

  


    # def extract_chapters_not_in_description(video_url):
    #     hidden_chapters = []

    # # Get video description from YouTube
    # # video_id = video_url.split('v=')[1]
    # # api_url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=snippet&key=YOUR_API_KEY'
    # # response = requests.get(api_url)
    # # data = response.json()

    #     if 'items' in data and data['items']:
    #         description = data['items'][0]['snippet']['description']
    #         lines = description.split('\n')

    #         for line in lines:
    #             # Look for lines starting with a timestamp like '0:00'
    #             if re.match(r'^\d+:\d+', line):
    #                 # Split the line into timestamp and title
    #                 parts = line.split(' ', 1)
    #                 timestamp = parts[0]
    #                 chapter_title = parts[1] if len(parts) > 1 else ""

    #                 chapters.append((timestamp, chapter_title))

    #     return chapters

    # video_url = 'https://www.youtube.com/watch?v=zmdjNSmRXF4&t=47s'
    # chapters = extract_chapters(video_url)
    # print(chapters)
