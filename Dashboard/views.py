import requests
import time
from django.shortcuts import render,redirect
from decouple import config

def index(request):
    images = []
    videos = []
    popular_tags=['design','css','web devlopment','mutimedia','intagram','youtube', "trendy", "professional", "technology", "news", "socialmedia", "entertainment", "food", "education", "media", "lifestyle", "fashion accessories", "gadgets", "coding", "startup", "digital marketing", "influencer", "creativity", "travel", "fitness", "nature", "architecture", "abstract", "business", "minimal", "summer", "urban", "self-care", "mobile app", "data science", "AI", "machine learning", "remote work", "workspace", "artificial intelligence", "blogging"]
    if request.method == 'POST':
        query = request.POST.get('text', '').strip()
        option = request.POST.get('option')
        result_count = 0
        all_option = False
        time_start = time.time()

        if option == 'image':
            access_key  = config('API_KEY_1')
            url = f'https://api.unsplash.com/search/photos?query={query}&page=100&client_id={access_key}'
            response = requests.get(url)
            data = response.json()
            images = [img['urls']['regular'] for img in data.get('results', [])]
            result_count = data.get('total', 0)

        elif option == 'video':
            pexels_key = config('API_KEY_2')
            headers = {'Authorization': pexels_key}
            url = f'https://api.pexels.com/videos/search?query={query}&per_page=100'
            response = requests.get(url, headers=headers)
            data = response.json()
            videos = [
                {
                    'title': v.get('user', {}).get('name', 'Pexels Video'),
                    'thumbnail': v.get('image'),
                    'duration': f"{v.get('duration', 0) // 60}:{v.get('duration', 0) % 60:02}",
                    'snippet': f"Video by {v.get('user', {}).get('name', '')}",
                    'url': v.get('video_files', [])[0].get('link') if v.get('video_files') else ''
                }
                for v in data.get('videos', [])
            ]
        else:
            if query:
                all_option = True

                # Images
                access_key = config('API_KEY_1')
                url = f'https://api.unsplash.com/search/photos?query={query}&page=100&client_id={access_key}'
                response = requests.get(url)
                data = response.json()
                images = [img['urls']['regular'] for img in data.get('results', [])]
                result_count = data.get('total', 0)

                # Videos
                pexels_key =  config('API_KEY_2')
                headers = {'Authorization': pexels_key}
                url = f'https://api.pexels.com/videos/search?query={query}&per_page=100'
                response = requests.get(url, headers=headers)
                data = response.json()
                videos = [
                    {
                        'title': v.get('user', {}).get('name', 'Pexels Video'),
                        'thumbnail': v.get('image'),
                        'duration': f"{v.get('duration', 0) // 60}:{v.get('duration', 0) % 60:02}",
                        'snippet': f"Video by {v.get('user', {}).get('name', '')}",
                        'url': v.get('video_files', [])[0].get('link') if v.get('video_files') else ''
                    }
                    for v in data.get('videos', [])
                ]

        time_end = time.time()
        time_taken = round(time_end - time_start, 1)
        return render(request, 'Dashboard/index.html', {
            'images': images,
            'videos': videos,
            'all_option': all_option,
            'time_taken': time_taken,
            'result_count': result_count,
            'popular_tags':popular_tags
        })

    # GET Request
    return render(request, 'Dashboard/index.html', {
        'images': [],
        'videos': [],
        'all_option': False,
        'time_taken': 0,
        'result_count': 0,
        'popular_tags':popular_tags
    })


def popularTags(request,tag):
        images = []
        videos = []
        query = tag
        popular_tags=['design','css','web devlopment','mutimedia','intagram','youtube', "trendy", "professional", "technology", "news", "socialmedia", "entertainment", "food", "education", "media", "lifestyle", "fashion accessories", "gadgets", "coding", "startup", "digital marketing", "influencer", "creativity", "travel", "fitness", "nature", "architecture", "abstract", "business", "minimal", "summer", "urban", "self-care", "mobile app", "data science", "AI", "machine learning", "remote work", "workspace", "artificial intelligence", "blogging"]
        result_count = 0
        time_start = time.time()
        if query:
                all_option = True

                # Images
                access_key = config('API_KEY_1')
                url = f'https://api.unsplash.com/search/photos?query={query}&page=100&client_id={access_key}'
                response = requests.get(url)
                data = response.json()
                images = [img['urls']['regular'] for img in data.get('results', [])]
                result_count = data.get('total', 0)

                # Videos
                pexels_key = config('API_KEY_2')
                headers = {'Authorization': pexels_key}
                url = f'https://api.pexels.com/videos/search?query={query}&per_page=100'
                response = requests.get(url, headers=headers)
                data = response.json()
                videos = [
                    {
                        'title': v.get('user', {}).get('name', 'Pexels Video'),
                        'thumbnail': v.get('image'),
                        'duration': f"{v.get('duration', 0) // 60}:{v.get('duration', 0) % 60:02}",
                        'snippet': f"Video by {v.get('user', {}).get('name', '')}",
                        'url': v.get('video_files', [])[0].get('link') if v.get('video_files') else ''
                    }
                    for v in data.get('videos', [])
                ]

        time_end = time.time()
        time_taken = round(time_end - time_start, 1)
        return render(request, 'Dashboard/index.html', {
            'images': images,
            'videos': videos,
            'all_option': all_option,
            'time_taken': time_taken,
            'result_count': result_count,
            'popular_tags':popular_tags
        })


    