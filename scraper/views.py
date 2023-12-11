from django.shortcuts import render
from django.views import View
from .models import Video
import requests
from bs4 import BeautifulSoup
import re

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
            chapters = self.extract_chapters(description)

            # Save chapters in the database
            for timestamp, chapter_title in chapters:
                video.chapter_set.create(timestamp=timestamp, title=chapter_title)

            return render(request, 'add_video.html', {'video': video, 'chapters': video.chapter_set.all()})

        return render(request, 'add_video.html')

    def extract_chapters(self, description):
        chapters = []
        lines = description.split('\n')

        for line in lines:
            # Look for lines starting with a timestamp like '0:00'
            if re.match(r'^\d+:\d+', line):
                # Split the line into timestamp and title
                parts = line.split(' ', 1)
                timestamp = parts[0]
                chapter_title = parts[1] if len(parts) > 1 else ""

                chapters.append((timestamp, chapter_title))

        return chapters

