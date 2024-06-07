from dataclasses import dataclass, field
import requests
from comicbot_api.utils.comic import Comic
from bs4 import BeautifulSoup, Tag
from typing import List


def comic_title_finder(tag: Tag) -> bool:
    return tag.has_attr('class') and 'title' in tag.get('class')


@dataclass
class WebScraper:
    base_url: str
    parser: str = 'html.parser'
    headers: dict = field(default_factory=lambda: {'User-Agent': 'Mozilla/5.0'})

    def scrape_comics(self, url: str) -> List:
        comic_releases_response = requests.get(url, headers=self.headers)
        if comic_releases_response.status_code == 200:
            comic_releases_html = comic_releases_response.json().pop('list')
            soup = BeautifulSoup(comic_releases_html, self.parser)
            all_comic_titles = soup.findAll(comic_title_finder)
            return list(map(lambda link:
                            Comic(base_url=self.base_url,
                                  link_suffix=link.attrs.pop('href'),
                                  title=link.contents[0].strip()),
                            all_comic_titles))
        return []
