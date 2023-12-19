from django.shortcuts import render
from django.views import View
from .models import Video, Video_Chapter
import requests, re
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

            # save the soup object
            with open('scraper/data/soup.html', 'w') as f:
                f.write(str(soup))



            title = soup.find('meta', property='og:title')['content']
            description = soup.find('meta', property='og:description')['content']
            chapter = soup.find('yt-attributed-string', class_='style-scope ytd-text-inline-expander')
            #chapter = soup.find('meta', property='yt-core-attributed-string')
            print(chapter)

            # Save the scraped data
            video, created = Video.objects.update_or_create(
                url=url,
                defaults={'title': title, 'description': description},
                )
            
            # Extract chapters from video description
            chapters = self.extract_chapters_in_description(description)

            # Save chapters in the database
            for timestamp, chapter_title in chapters:
                Video_Chapter.objects.create(video=video, timestamp=timestamp, title=chapter_title)

            return render(request, 'add_video.html', {'video': video, 'video_chapters': video.video_chapter_set.all()})

        return render(request, 'add_video.html')

    def extract_chapters_in_description(self, description):
        # This regex pattern matches timestamps in the format HH:MM:SS or MM:SS followed by any text
        pattern = re.compile(r'(\d{1,2}:\d{1,2}(:\d{1,2})?) - (.*)')
        matches = pattern.findall(description)
        return matches