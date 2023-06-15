from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
from app_posts.models import Post


class Command(BaseCommand):
    urls = []
    wiki_data = []

    def get_wiki_urls(self):
        base_url = 'https://en.wikipedia.org'
        start_wiki_url = 'https://en.wikipedia.org/wiki/Wikipedia:Featured_articles'
        wiki_html = requests.get(start_wiki_url).text
        wiki_soup = BeautifulSoup(wiki_html, 'lxml')

        target_span = wiki_soup.find('span', {'id': 'Episodes_of_television'})
        target_p = list(target_span.nextGenerator())[4]
        spans = target_p.find_all('span')

        for span in spans:
            a = span.find('a')
            self.urls.append(base_url + a.get('href'))

    def get_posts_dict(self):
        self.get_wiki_urls()
        for url in self.urls:
            try:
                new_html = requests.get(url).text
                new_soup = BeautifulSoup(new_html, 'lxml')
                title = new_soup.find('h1').text
                all_ps = [p.text.strip() for p in new_soup.find_all('p') if len(p.text.strip()) > 0]
                description = all_ps[0]
                content = "".join(para for para in all_ps[1:])
                self.wiki_data.append({'title': title, 'description': description, 'content': content})

            except Exception as exc:
                self.stdout.write(self.style.ERROR())

    def handle(self, *args, **options):
        self.stdout.write('Parsing wiki...')
        self.get_posts_dict()
        self.stdout.write('Parsing over, preparing the data')
        posts = [
            Post(title=data_dict.get('title'),
                 description=data_dict.get('description'),
                 content=data_dict.get('content')
                 )
            for data_dict in self.wiki_data
        ]
        Post.objects.bulk_create(posts)
        self.stdout.write(self.style.SUCCESS(f'Created {len(posts)} new posts'))
