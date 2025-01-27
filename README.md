![Python >= 3.7](https://img.shields.io/badge/python->=3.7-red.svg) [![](https://badgen.net/github/release/deedy5/duckduckgo_search)](https://github.com/deedy5/duckduckgo_search/releases) [![](https://badge.fury.io/py/duckduckgo-search.svg)](https://pypi.org/project/duckduckgo-search)
# Duckduckgo_search<a name="TOP"></a>

Search for words, documents, images, videos, news, maps and text translation using the DuckDuckGo.com search engine. Downloading files and images to a local hard drive.

## Table of Contents
* [Install](#install)
* [CLI version](#cli-version)
* [Duckduckgo search operators](#duckduckgo-search-operators)
* [Regions](#regions)
* [Using proxy](#using-proxy)
* [Warning](#warning)
* [1. ddg() - text search](#1-ddg---text-search-by-by-duckduckgocom)
* [2. ddg_answers() - instant answers](#2-ddg_answers---instant-answers-by-duckduckgocom)
* [3. ddg_images() - image search](#3-ddg_images---image-search-by-duckduckgocom)
* [4. ddg_videos() - video search](#4-ddg_videos---video-search-by-duckduckgocom)
* [5. ddg_news() - news search](#5-ddg_news---news-search-by-duckduckgocom)
* [6. ddg_maps() - map search](#6-ddg_maps---map-search-by-duckduckgocom)
* [7. ddg_translate() - translation](#7-ddg_translate---translation-by-duckduckgocom)
* [8. ddg_suggestions() - suggestions](#8-ddg_suggestions---suggestions-by-duckduckgocom)

## Install
```python
pip install -U duckduckgo_search
```

## CLI version

```python3
ddgs --help
```
or
```python3
python -m duckduckgo_search --help
```

CLI examples:
```python3
# download pdf files
ddgs text -k "russia filetype:pdf" -m 250 -o None -d
# download images
ddgs images -k "lady in red" -m 1000 -s off -o None -d
# get latest news
ddgs news -k "ukraine war" -s off -t d -m 50
```
[Go To TOP](#TOP)

## Duckduckgo search operators

| Keywords example |	Result|
| ---     | ---   |
| cats dogs |	Results about cats or dogs |
| "cats and dogs" |	Results for exact term "cats and dogs". If no results are found, related results are shown. |
| cats -dogs |	Fewer dogs in results |
| cats +dogs |	More dogs in results |
| cats filetype:pdf |	PDFs about cats. Supported file types: pdf, doc(x), xls(x), ppt(x), html |
| dogs site:example.com  |	Pages about dogs from example.com |
| cats -site:example.com |	Pages about cats, excluding example.com |
| intitle:dogs |	Page title includes the word "dogs" |
| inurl:cats  |	Page url includes the word "cats" |

[Go To TOP](#TOP)

## Regions
<details>
  <summary>expand</summary>

    xa-ar for Arabia
    xa-en for Arabia (en)
    ar-es for Argentina
    au-en for Australia
    at-de for Austria
    be-fr for Belgium (fr)
    be-nl for Belgium (nl)
    br-pt for Brazil
    bg-bg for Bulgaria
    ca-en for Canada
    ca-fr for Canada (fr)
    ct-ca for Catalan
    cl-es for Chile
    cn-zh for China
    co-es for Colombia
    hr-hr for Croatia
    cz-cs for Czech Republic
    dk-da for Denmark
    ee-et for Estonia
    fi-fi for Finland
    fr-fr for France
    de-de for Germany
    gr-el for Greece
    hk-tzh for Hong Kong
    hu-hu for Hungary
    in-en for India
    id-id for Indonesia
    id-en for Indonesia (en)
    ie-en for Ireland
    il-he for Israel
    it-it for Italy
    jp-jp for Japan
    kr-kr for Korea
    lv-lv for Latvia
    lt-lt for Lithuania
    xl-es for Latin America
    my-ms for Malaysia
    my-en for Malaysia (en)
    mx-es for Mexico
    nl-nl for Netherlands
    nz-en for New Zealand
    no-no for Norway
    pe-es for Peru
    ph-en for Philippines
    ph-tl for Philippines (tl)
    pl-pl for Poland
    pt-pt for Portugal
    ro-ro for Romania
    ru-ru for Russia
    sg-en for Singapore
    sk-sk for Slovak Republic
    sl-sl for Slovenia
    za-en for South Africa
    es-es for Spain
    se-sv for Sweden
    ch-de for Switzerland (de)
    ch-fr for Switzerland (fr)
    ch-it for Switzerland (it)
    tw-tzh for Taiwan
    th-th for Thailand
    tr-tr for Turkey
    ua-uk for Ukraine
    uk-en for United Kingdom
    us-en for United States
    ue-es for United States (es)
    ve-es for Venezuela
    vn-vi for Vietnam
    wt-wt for No region
___
</details>

[Go To TOP](#TOP)

## Using proxy

```python3
from duckduckgo_search import ddg
from duckduckgo_search.utils import SESSION


SESSION.proxies = {
    "http": f"socks5h://localhost:9150",
    "https": f"socks5h://localhost:9150"
}
r = ddg("Don't Worry, Be Happy")
print(r)
```

[Go To TOP](#TOP)

## Warning
:warning:
**Always** use the **max_results** parameter if you need more results than what is returned when page=1.
In this case requests to the api are multithreaded and duplicate results are avoided.
If you try to get all results using the page parameter and increasing it (1, 2, 3, 4, etc.), api will be returning repeated results indefinitely.

[Go To TOP](#TOP)

## 1. ddg() - text search by by duckduckgo.com

```python
from duckduckgo_search import ddg

def ddg(
    keywords,
    region="wt-wt",
    safesearch="moderate",
    time=None,
    max_results=None,
    page=1,
    output=None,
    download=False,
):
    """DuckDuckGo text search. Query params: https://duckduckgo.com/params

    Args:
        keywords (str): keywords for query.
        region (str, optional): wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch (str, optional): on, moderate, off. Defaults to "moderate".
        time (Optional[str], optional): d, w, m, y. Defaults to None.
        max_results (Optional[int], optional): maximum number of results, max=200. Defaults to None.
            if max_results is set, then the parameter page is not taken into account.
        page (int, optional): page for pagination. Defaults to 1.
        output (Optional[str], optional): csv, json. Defaults to None.
        download (bool, optional): if True, download and save dociments to 'keywords' folder.
            Defaults to False.

    Returns:
        Optional[List[dict]]: DuckDuckGo text search results.
    """
```
***Returns***
```python
[{'title': str,
  'href': str,
  'body': str,},
 ...
 ]
```
***Example 1. Text search***
```python
from duckduckgo_search import ddg

keywords = 'Bella Ciao'
results = ddg(keywords, region='wt-wt', safesearch='Off', time='y')
print(results)
```
```python
[
{'title': 'Bella Ciao - Original Italian Lyrics & English Translation ...', 'href': 'https://dailyitalianwords.com/bella-ciao-original-italian-lyrics-english-translation/', 'body': 'Bella Ciao - English Meaning (Mondine version) In the morning as soon as I get up oh goodbye beautiful, goodbye beautiful, goodbye beautiful, bye, bye, bye In the morning as soon as I get up I have to go to the paddy fields. And between insects and mosquitoes oh goodbye beautiful, goodbye beautiful, goodbye beautiful, bye, bye, bye'},
{'title': "What's the meaning of Bella Ciao | Italian song explained", 'href': 'https://www.thinkinitalian.com/bella-ciao-meaning/', 'body': "Bella Ciao is probably the most famous Italian folk song. It has been sung anywhere in the world for years, and the TV series Money Heist made it even more popular. But what does it talk about? What's the story behind its lyrics? This is a perfect chance to learn some more Italian with the meaning of Bella Ciao. Italian culture Michele"},
...
]
```
***Example 2. Searching for pdf files***
```python
from duckduckgo_search import ddg

keywords = 'conditioned reflex in humans filetype:pdf'
results = ddg(keywords, safesearch='Off', max_results=200)
print(results)
```
```python
[
{'title': 'PDF Conditioned Reflexes', 'href': 'https://antilogicalism.com/wp-content/uploads/2019/04/conditioned-reflexes.pdf', 'body': '302 CONDITIONED REFLEXES. in the strength of the reflexes, a state of ;affair.~ which lasted for many. days, the relation between the magnitudes of the reflexes and the Other dogs those of the inhibitable type suffered a functional disturbance of the cortical activities for a very considerable period.'},
{'title': 'Conditioned reflex therapy; the direct approach to the reconstruction...', 'href': 'https://archive.org/details/conditionedrefle00salt', 'body': "Two chapters were rewritten and expanded from the author's What is hypnosis. One was reprinted from the South west review. Bibliography: p. 321-340."},
{'title': 'conditioned reflex examples in humans - Bing', 'href': 'https://technopagan.org/conditioned+reflex+examples+in+humans&FORM=QSRE4', 'body': 'Jun 02, 2021 · Conditioned Reflex Examples In Humans And not discrimination is directly with dogs was presented is absent, and emotional responses being subtle variations in... When they hear thunder, in conditioned reflex was sent to humans are allowed early contributions ivan to know about why...'},
...
]
```

[Go To TOP](#TOP)

## 2. ddg_answers() - instant answers by duckduckgo.com

```python
from duckduckgo_search import ddg_answers

def ddg_answers(
    keywords,
    related=False,
    output=None,
):
    """DuckDuckGo instant answers. Query params: https://duckduckgo.com/params
    Args:
        keywords (str): keywords for query.
        related (bool, optional): add related topics to results. Defaults to False.
        output (Optional[str], optional): csv, json. Defaults to None.
    Returns:
        Optional[List[dict]]: DuckDuckGo instant answers results.
    """
```

***Returns***
```python
[{'icon': Optional[str],
  'text': Optional[str],
  'topic': Optional[str],
  'url': Optional[str],},
 ...
 ]
```

***Example 1. Answers***
```python
from duckduckgo_search import ddg_answers

keywords = 'ford company'
results = ddg_answers(keywords, related=True)
print(results)
```
```python
[
{'icon': None, 'text': "Ford Motor Company is an American multinational automobile manufacturer headquartered in Dearborn, Michigan, United States. It was founded by Henry Ford and incorporated on June 16, 1903. The company sells automobiles and commercial vehicles under the Ford brand, and luxury cars under its Lincoln luxury brand. Ford also owns Brazilian SUV manufacturer Troller, an 8% stake in Aston Martin of the United Kingdom and a 32% stake in China's Jiangling Motors. It also has joint ventures in China, Taiwan, Thailand, Turkey, and Russia. The company is listed on the New York Stock Exchange and is controlled by the Ford family; they have minority ownership but the majority of the voting power. Ford introduced methods for large-scale manufacturing of cars and large-scale management of an industrial workforce using elaborately engineered manufacturing sequences typified by moving assembly lines; by 1914, these methods were known around the world as Fordism.", 'topic': None, 'url': 'https://en.wikipedia.org/wiki/Ford_Motor_Company'}
{'icon': None, 'text': 'Ford Motor Company Category', 'topic': None, 'url': 'https://duckduckgo.com/c/Ford_Motor_Company'}
{'icon': None, 'text': "Ford's Garage - Ford's Garage is an American chain of casual dining restaurants founded in 2012. The first restaurant was opened in Fort Myers, Florida. As of July 2022, the company had 21 restaurants in four states, the majority of which are operated by 23 Restaurant Services.", 'topic': None, 'url': "https://duckduckgo.com/Ford's_Garage"}
...
]
```

[Go To TOP](#TOP)

## 3. ddg_images() - image search by duckduckgo.com

```python
from duckduckgo_search import ddg_images

def ddg_images(
    keywords,
    region="wt-wt",
    safesearch="moderate",
    time=None,
    size=None,
    color=None,
    type_image=None,
    layout=None,
    license_image=None,
    max_results=None,
    page=1,
    output=None,
    download=False,
):
    """DuckDuckGo images search. Query params: https://duckduckgo.com/params

    Args:
        keywords (str): keywords for query.
        region (str, optional): wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch (str, optional): on, moderate, off. Defaults to "moderate".
        time (Optional[str], optional): Day, Week, Month, Year. Defaults to None.
        size (Optional[str], optional): Small, Medium, Large, Wallpaper. Defaults to None.
        color (Optional[str], optional): color, Monochrome, Red, Orange, Yellow, Green, Blue,
            Purple, Pink, Brown, Black, Gray, Teal, White. Defaults to None.
        type_image (Optional[str], optional): photo, clipart, gif, transparent, line.
            Defaults to None.
        layout (Optional[str], optional): Square, Tall, Wide. Defaults to None.
        license_image (Optional[str], optional): any (All Creative Commons), Public (PublicDomain),
            Share (Free to Share and Use), ShareCommercially (Free to Share and Use Commercially),
            Modify (Free to Modify, Share, and Use), ModifyCommercially (Free to Modify, Share, and
            Use Commercially). Defaults to None.
        max_results (Optional[int], optional): maximum number of results, max=1000. Defaults to None.
            if max_results is set, then the parameter page is not taken into account.
        page (int, optional): page for pagination. Defaults to 1.
        output (Optional[str], optional): csv, json. Defaults to None.
        download (bool, optional): if True, download and save images to 'keywords' folder.
            Defaults to False.

    Returns:
        Optional[List[dict]]: DuckDuckGo text search results.
    """
```
***Returns***
```python
[{'height': int,
  'image': str,
  'source': str,
  'thumbnail': str,
  'title': str,
  'url': str,
  'width': int },
 ...
 ]
```
***Example***
```python
from duckduckgo_search import ddg_images

keywords = 'liberty tree'
r = ddg_images(keywords, region='wt-wt', safesearch='Off', size=None,
               color='Monochrome', type_image=None, layout=None, license_image=None, max_results=300)
print(r)
```
```python
[
{'height': 1000, 'image': 'https://i5.walmartimages.com/asr/fef2dbdb-3756-4401-b7ae-502ec2ea082b_1.eb37ae35a5e3d4ae59d61ecac336c226.jpeg?odnWidth=1000&odnHeight=1000&odnBg=ffffff', 'source': 'Bing', 'thumbnail': 'https://tse2.mm.bing.net/th?id=OIP.4DhDDdx9IOAwbFm6CRGpTwHaHa&pid=Api', 'title': 'Liberty Tree 1765 Nthe Large Elm Tree At Boylston Market ...', 'url': 'https://www.walmart.com/ip/Liberty-Tree-1765-Nthe-Large-Elm-Tree-Boylston-Market-Boston-Massachusetts-Named-Liberty-Tree-Sons-Liberty-Held-Meetings-Summer-1765-Wood-Engraving-A/997377547?wmlspartner=bizratecom&affcmpid=3313893407&tmode=0000', 'width': 1000},
{'height': 2400, 'image': 'http://etc.usf.edu/clipart/13500/13570/liberty-tree_13570.tif', 'source': 'Bing', 'thumbnail': 'https://tse2.mm.bing.net/th?id=OIP.4t3AojTiUP6TZ-AFaSfCHAHaJ7&pid=Api', 'title': 'Liberty Tree | ClipArt ETC', 'url': 'http://etc.usf.edu/clipart/13500/13570/liberty-tree_13570.htm', 'width': 1790},
{'height': 297, 'image': 'https://www.blogtalkradio.com/api/image/resize/400x297/aHR0cHM6Ly9kYXNnN3h3bWxkaXg2LmNsb3VkZnJvbnQubmV0L2hvc3RwaWNzLzc1MGZhZjVhLTJhMTUtNDE5Ni1iOTQwLTA1NTc1NjVlMGM1MV9saWJlcnR5LXRyZWVfbG9nby5qcGc/750faf5a-2a15-4196-b940-0557565e0c51_liberty-tree_logo.jpg?mode=Fill', 'source': 'Bing', 'thumbnail': 'https://tse2.mm.bing.net/th?id=OIP.IQxgK4LaaFV82m7Iz9J3sgAAAA&pid=Api', 'title': 'Liberty Tree Radio Online Radio | BlogTalkRadio', 'url': 'http://www.blogtalkradio.com/libertytreeradio', 'width': 400},
...
]
```

[Go To TOP](#TOP)

## 4. ddg_videos() - video search by duckduckgo.com

```python
from duckduckgo_search import ddg_videos

def ddg_videos(
    keywords,
    region="wt-wt",
    safesearch="moderate",
    time=None,
    resolution=None,
    duration=None,
    license_videos=None,
    max_results=None,
    page=1,
    output=None,
):
    """DuckDuckGo videos search. Query params: https://duckduckgo.com/params

    Args:
        keywords (str): keywords for query.
        region (str, optional): wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch (str, optional): on, moderate, off. Defaults to "moderate".
        time (Optional[str], optional): d, w, m. Defaults to None.
        resolution (Optional[str], optional): high, standart. Defaults to None.
        duration (Optional[str], optional): short, medium, long. Defaults to None.
        license_videos (Optional[str], optional): creativeCommon, youtube. Defaults to None.
        max_results (Optional[int], optional): maximum number of results, max=1000. Defaults to None.
            if max_results is set, then the parameter page is not taken into account.
        page (int, optional): page for pagination. Defaults to 1.
        output (Optional[str], optional): csv, json. Defaults to None.

    Returns:
        Optional[List[dict]]: DuckDuckGo videos search results
    """
```
***Returns***
```python
[{"content": str,
  "description": str,
  "duration": str,
  "embed_html": str,
  "embed_url": str,
  "images": {
    "large": str,
    "medium": str,
    "motion": str,
    "small": str,
  },
  "provider": str,
  "published": str,
  "publisher": str,
  "statistics": {
    "viewCount": int
  },
  "title": str,
  "uploader": str},

 ...
 ]
```
***Example***
```python
from duckduckgo_search import ddg_videos

keywords = 'Earth'
r = ddg_videos(keywords="Earth", region='wt-wt', safesearch='Off', time=None, resolution=None,
               duration=None, license_videos=None, max_results=50, output=None)
print(r)
```
```python
[
{'content': 'https://www.youtube.com/watch?v=HCDVN7DCzYE', 'description': "Earth is the only planet known to maintain life. Find out the origins of our home planet and some of the key ingredients that help make this blue speck in space a unique global ecosystem. Subscribe: http://bit.ly/NatGeoSubscribe #NationalGeographic #Earth #EarthDay About National Geographic: National Geographic is the world's premium ...", 'duration': '3:33', 'embed_html': '<iframe width="1280" height="720" src="https://www.youtube.com/embed/HCDVN7DCzYE?autoplay=1" frameborder="0" allowfullscreen></iframe>', 'embed_url': 'https://www.youtube.com/embed/HCDVN7DCzYE?autoplay=1', 'images': {'large': 'https://tse2.mm.bing.net/th?id=OVP.oeITkB49pZMoAG0Ds6PoXQHgFo&pid=Api', 'medium': 'https://tse2.mm.bing.net/th?id=OVP.oeITkB49pZMoAG0Ds6PoXQHgFo&pid=Api', 'motion': 'https://tse2.mm.bing.net/th?id=OM2.PVGeB2TtDBxXjQ_1633563877&pid=Api', 'small': 'https://tse2.mm.bing.net/th?id=OVP.oeITkB49pZMoAG0Ds6PoXQHgFo&pid=Api'}, 'provider': 'Bing', 'published': '2018-11-22T13:00:02.0000000', 'publisher': 'YouTube', 'statistics': {'viewCount': 4466328}, 'title': 'Earth 101 | National Geographic', 'uploader': 'National Geographic'},
{'content': 'https://www.youtube.com/watch?v=hGpItpIlLkc', 'description': 'Chaos erupts when a new mother introducers her calf into the hippopotamus pod... Subscribe: http://bit.ly/BBCEarthSub #NaturalWorld #BBCEarth Watch more: Planet Earth http://bit.ly/PlanetEarthPlaylist Blue Planet http://bit.ly/BluePlanetPlaylist Planet Earth II http://bit.ly/PlanetEarthIIPlaylist Planet Dinosaur https://bit.ly ...', 'duration': '6:05', 'embed_html': '<iframe width="1280" height="720" src="https://www.youtube.com/embed/hGpItpIlLkc?autoplay=1" frameborder="0" allowfullscreen></iframe>', 'embed_url': 'https://www.youtube.com/embed/hGpItpIlLkc?autoplay=1', 'images': {'large': 'https://tse1.mm.bing.net/th?id=OVP.lwq6by7crgwpkXGERzXLvQHgFo&pid=Api', 'medium': 'https://tse1.mm.bing.net/th?id=OVP.lwq6by7crgwpkXGERzXLvQHgFo&pid=Api', 'motion': 'https://tse1.mm.bing.net/th?id=OM.3QweCgZ-KW53rQ&pid=Api', 'small': 'https://tse1.mm.bing.net/th?id=OVP.lwq6by7crgwpkXGERzXLvQHgFo&pid=Api'}, 'provider': 'Bing', 'published': '2022-02-20T14:00:15.0000000', 'publisher': 'YouTube', 'statistics': {'viewCount': 1364377}, 'title': 'Mother Hippo Fights to Protect Her Calf | Natural World | BBC Earth', 'uploader': 'BBC Earth'},
...
]
```

[Go To TOP](#TOP)

## 5. ddg_news() - news search by duckduckgo.com

```python
from duckduckgo_search import ddg_news

def ddg_news(
    keywords,
    region="wt-wt",
    safesearch="moderate",
    time=None,
    max_results=None,
    page=1,
    output=None,
):
    """DuckDuckGo news search. Query params: https://duckduckgo.com/params

    Args:
        keywords (str): keywords for query.
        region (str): wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch (str): on, moderate, off. Defaults to "moderate".
        time (Optional[str], optional): d, w, m. Defaults to None.
        max_results (Optional[int], optional): maximum number of results, max=240. Defaults to None.
            if max_results is set, then the parameter page is not taken into account.
        page (int, optional): page for pagination. Defaults to 1.
        output (Optional[str], optional): csv, json. Defaults to None.

    Returns:
        Optional[List[dict]]: DuckDuckGo news search results.
    """
```
***Returns***
```python
[{'date': str,
  'title': str,
  'body': str,
  'url': str,
  'image': str,
  'source': str,
 ...
 ]
```
***Example***
```python
from duckduckgo_search import ddg_news

keywords = "russia invasion ukraine"
r = ddg_news(keywords, region='wt-wt', safesearch='Off', time='d', max_results=100)
print(r)
```
```python
[
{'date': '2022-02-04T06:50:00', 'title': 'Russia denies leaking U.S. security talks document to El Pais', 'body': 'Moscow has demanded guarantees from Washington and NATO that Ukraine will not be allowed to join the military bloc. Russia has amassed over 100,000 troops close to the Ukrainian borders, but denies planning an invasion.', 'url': 'https://wdez.com/2022/02/04/russia-denies-leaking-u-s-security-talks-document-to-el-pais/', 'image': 'https://storage.googleapis.com/media.mwcradio.com/mimesis/2022-02/04/2022-02-04T060600Z_1_LYNXMPEI13053_RTROPTP_3_RUSSIA-USA-SECURITY.JPG', 'source': 'WDEZ'},
{'date': '2022-02-04T06:50:00', 'title': 'Analysis-Traders scour markets for protection amid Ukraine tensions', 'body': 'LONDON (Reuters) - Unnerved by the sabre-rattling between Russia and the West over Ukraine, traders are scouring ... a 10% probability of a full-fledged invasion. Ganry recommends a different ...', 'url': 'https://wsau.com/2022/02/04/analysis-traders-scour-markets-for-protection-amid-ukraine-tensions/', 'image': 'https://storage.googleapis.com/media.mwcradio.com/mimesis/2022-02/04/2022-02-04T061136Z_2_LYNXMPEI13058_RTROPTP_3_GLOBAL-MARKETS-TRADING.JPG', 'source': 'WSAY'},
{'date': '2022-02-04T06:47:00', 'title': "Morning news brief: US's warning on Russia-Ukraine crisis, Johnson's top aides quitting, and more", 'body': 'Russia will produce graphic propaganda video as pretext for an invasion against Ukraine: US © Provided by WION Pentagon officials said today that Russia could fabricate a pretext for an invasion of Ukraine. "As part of this fake attack, we believe that ...', 'url': 'https://www.msn.com/en-in/news/world/morning-news-brief-us-s-warning-on-russia-ukraine-crisis-johnson-s-top-aides-quitting-and-more/ar-AATs9ml', 'image': 'https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AATsnww.img?h=315&w=600&m=6&q=60&o=t&l=f&f=jpg', 'source': 'MSN'},
...
]
```

[Go To TOP](#TOP)

## 6. ddg_maps() - map search by duckduckgo.com

```python
from duckduckgo_search import ddg_maps

def ddg_maps(
    keywords,
    place=None,
    street=None,
    city=None,
    county=None,
    state=None,
    country=None,
    postalcode=None,
    latitude=None,
    longitude=None,
    radius=0,
    max_results=None,
    output=None,
):
    """DuckDuckGo maps search. Query params: https://duckduckgo.com/params

    Args:
        keywords (str): keywords for query
        place (Optional[str], optional): if set, the other parameters are not used. Defaults to None.
        street (Optional[str], optional): house number/street. Defaults to None.
        city (Optional[str], optional): city of search. Defaults to None.
        county (Optional[str], optional): county of search. Defaults to None.
        state (Optional[str], optional): state of search. Defaults to None.
        country (Optional[str], optional): country of search. Defaults to None.
        postalcode (Optional[str], optional): postalcode of search. Defaults to None.
        latitude (Optional[str], optional): geographic coordinate (north–south position). Defaults to None.
        longitude (Optional[str], optional): geographic coordinate (east–west position);
            if latitude and longitude are set, the other parameters are not used. Defaults to None.
        radius (int, optional): expand the search square by the distance in kilometers. Defaults to 0.
        max_results (Optional[int], optional): maximum number of results. Defaults to None.
        output (Optional[str], optional): csv, json. Defaults to None.

    Returns:
        Optional[List[dict]]: DuckDuckGo maps search results
    """
```
***Returns***
```python
[{'title': str,
  'address': str,
  'country_code': str,
  'latitude': float,
  'longitude': float,
  'url': str,
  'desc': str,
  'phone': str,
  'image': str,
  'source': str,
  'links': dict,
  'hours': dict,}
 ...
 ]
```
***Example 1. Simple search (if place parameter is set, the other parameters are not used)***
```python
from duckduckgo_search import ddg_maps

keywords = 'dentists'
place = 'Los Angeles'

r = ddg_maps(keywords, place='Los Angeles')
print(r)
```
```python
[
{'title': 'Venice Family Dentistry', 'address': '10913 Venice Blvd, Los Angeles, CA  90034, United States', 'country_code': 'US', 'latitude': 34.0159528696929, 'longitude': -118.412624001503, 'url': 'http://venicefamilydentistry.com', 'desc': 'This website is for sale! venicefamilydentistry.com is your first and best source for all of the information you’re looking for. From general topics to more of what you would expect to find here, venicefamilydentistry.com has it all. We hope you find what you are searching for!', 'phone': '+13108733331', 'image': '', 'source': 'http://yelp.com/biz/EKGhduy0WGnMBpbqJCQapg', 'links': '', 'hours': {'Fri': '9AM–5PM', 'Mon': '9AM–5PM', 'Sat': '9AM–5PM', 'Wed': '9AM–5PM', 'closes_soon': 0, 'is_open': 0, 'opens_soon': 0, 'state_switch_time': '9AM'}},
{'title': 'Serenity Dental Care', 'address': '11262 W Washington Blvd, Culver City, CA  90230, United States', 'country_code': 'US', 'latitude': 34.0050049579316, 'longitude': -118.413847088814, 'url': 'https://serenitydentalcare.com', 'desc': None, 'phone': '+13103906500', 'image': None, 'source': 'http://yelp.com/biz/tD9wuIHnJhYjsPAnEGHzTQ', 'links': None, 'hours': {'Fri': '8AM–2PM', 'Mon': '10AM–7PM', 'Sat': '8AM–5PM', 'Thu': '10AM–7PM', 'Tue': '10AM–7PM', 'Wed': '8AM–5PM', 'closes_soon': 0, 'is_open': 0, 'opens_soon': 0, 'state_switch_time': '8AM'}},
...
]
```
***Example 2. Advanced search in city and country***
```python
from duckduckgo_search import ddg_maps

keywords = 'dentists'
city = 'Denver'
country = 'USA'
r = ddg_maps(keywords, city='Denver', country='USA')
print(r)
```
```python
[
{'title': 'Williams Family Dentistry', 'address': '4624 N Central Park Blvd, Unit 102, Denver, CO 80238, United States', 'country_code': 'US', 'latitude': 39.7804958556395, 'longitude': -104.88231038524, 'url': 'http://www.margiewilliamsdds.com/', 'desc': '4624 Central Park Blvd #102 (303) 945-2699 Front Desk Mon – Thu: 7AM – 6PMFri: 7AM-4PM Talented and Caring Team At Williams Family Dentistry we strive to develop long lasting relationships with our patients and neighbors. We […]', 'phone': '+13039452699', 'image': 'https://margiewilliamsdds.com/wp-content/uploads/2021/06/Dr-Group-photo-scaled.jpg', 'source': 'http://yelp.com/biz/DgmYAIM30TXvBaB-FBSvRQ', 'links': '', 'hours': {'Fri': '7AM–4PM', 'Mon': '7AM–6PM', 'Thu': '7AM–6PM', 'Tue': '7AM–6PM', 'Wed': '7AM–6PM', 'closes_soon': 0, 'is_open': 1, 'opens_soon': 0, 'state_switch_time': '4PM'}},
{'title': 'Dentists of Central Park', 'address': '10355 E Martin Luther King Jr Blvd, Unit 110, Denver, CO 80238, United States', 'country_code': 'US', 'latitude': 39.7602729, 'longitude': -104.8673477, 'url': 'https://www.dentistsofcentralpark.com', 'desc': 'Local dentist near you in Denver. Book your dental appointment for general dentistry, teeth whitening, oral surgery, or emergency dentistry.', 'phone': '+17204038351', 'image': 'https://www.dentistsofcentralpark.com/etc/designs/pds/favicon-152x152.png', 'source': 'http://yelp.com/biz/6GULzhI8Zg6V5Diqyc_rWw', 'links': {'facebook': 'https://www.facebook.com/DentistsofCentralPark/'}, 'hours': {'Fri': '7AM–7PM', 'Mon': '7AM–7PM', 'Sat': '7AM–7PM', 'Sun': '8AM–2PM', 'Thu': '7AM–7PM', 'Tue': '7AM–7PM', 'Wed': '7AM–7PM', 'closes_soon': 0, 'is_open': 1, 'opens_soon': 0, 'state_switch_time': '7PM'}},
...
]
```
***Example 3. Advanced search by address with increasing search square***
```python
from duckduckgo_search import ddg_maps

keywords = 'dentists'
street = 'Av. Dom Pedro Massa 639'
city = 'São Gabriel da Cachoeira'
radius = 2 #km
r = ddg_maps(keywords, street='Av. Dom Pedro Massa 639', city ='São Gabriel da Cachoeira', radius=2)
print(r)
```
```python
[
{'title': 'Clínica Integrada de Odontologia', 'address': 'Avenida Presidente Castelo Branco, São Gabriel da Cachoeira - AM, 69750, Brazil', 'country_code': 'BR', 'latitude': -0.130427164469837, 'longitude': -67.0899445932125, 'url': '', 'desc': None, 'phone': '+559734711654', 'image': None, 'source': 'https://maps.apple.com/place?q=Cl%C3%ADnica%20Integrada%20de%20Odontologia&auid=7074519049033716214&address=Avenida%20Presidente%20Castelo%20Branco,%20S%C3%A3o%20Gabriel%20da%20Cachoeira%20-%20AM,%2069750,%20Brazil&ll=-0.13042716446983657,-67.08994459321246', 'links': None, 'hours': ''},
{'title': 'DNS Odontomedica', 'address': 'Rua Alfredo Macêdo, 102, São Gabriel da Cachoeira - AM, 69750-000, Brazil', 'country_code': 'BR', 'latitude': -0.1242364, 'longitude': -67.0890056, 'url': 'http://www.dnsodontologica.com.br', 'desc': None, 'phone': '+559734712066', 'image': None, 'source': 'https://maps.apple.com/place?q=DNS%20Odontomedica&auid=9296844468385454246&address=Rua%20Alfredo%20Mac%C3%AAdo,%20102,%20S%C3%A3o%20Gabriel%20da%20Cachoeira%20-%20AM,%2069750-000,%20Brazil&ll=-0.1242364,-67.0890056', 'links': None, 'hours': ''},

...
]
```
***Example 4. Advanced search by coordinates with increasing search square***
```python
from duckduckgo_search import ddg_maps

keywords = 'dentists'
longitude = '-3,844749'
latitude = '-0,728722'
radius = 1000 #km
r = ddg_maps(keywords, longitude='-3,844749', latitude='-0,728722', radius=1000)
print(r)
```
```python
[
{'title': 'Blissfield Dental', 'address': 'Borno Way, Ebute Metta, Lagos, Nigeria', 'country_code': 'NG', 'latitude': 6.49685370846362, 'longitude': 3.37770581245422, 'url': '', 'desc': None, 'phone': '+2348023134407', 'image': None, 'source': 'https://maps.apple.com/place?q=Blissfield%20Dental&auid=14057124693413493763&address=Borno%20Way,%20Ebute%20Metta,%20Lagos,%20Nigeria&ll=6.496853708463621,3.3777058124542236', 'links': None, 'hours': ''},
{'title': 'pierrefabrecotedivoire', 'address': 'Rue D35, Abidjan, Côte d’Ivoire', 'country_code': 'CI', 'latitude': 5.33444294059565, 'longitude': -3.97692739963531, 'url': 'https://www.instagram.com/pierrefabrecotedivoire/', 'desc': 'Welcome back to Instagram. Sign in to check out what your friends, family & interests have been capturing & sharing around the world.', 'phone': '', 'image': 'https://www.instagram.com/static/images/ico/apple-touch-icon-180x180-precomposed.png/c06fdb2357bd.png', 'source': 'https://maps.apple.com/place?q=pierrefabrecotedivoire&auid=11515715525840432861&address=Rue%20D35,%20Abidjan,%20C%C3%B4te%20d%E2%80%99Ivoire&ll=5.334442940595645,-3.976927399635315', 'links': '', 'hours': ''},
...
]
```

[Go To TOP](#TOP)

## 7. ddg_translate() - translation by duckduckgo.com

```python
from duckduckgo_search import ddg_translate

def ddg_translate(
    keywords,
    from_=None,
    to="en",
    output=None,
):
    """DuckDuckGo translate

    Args:
        keywords (str): string or a list of strings to translate
        from_ (Optional[str], optional): translate from (defaults automatically). Defaults to None.
        to (str): what language to translate. Defaults to "en".
        output (Optional[str], optional): csv, json. Defaults to None.

    Returns:
        Optional[List[dict]]: DuckDuckGo translate results.
    """
```
***Returns***
```python
[
{'detected_language': str,
  'translated': str,
  'original': str,},
 ...
 ]
```
***Example 1. Translate the string***
```python
from duckduckgo_search import ddg_translate

keywords = "A chain is only as strong as its weakest link"
results = ddg_translate(keywords, to='de')
print(results)
```
```python
[
{'detected_language': 'en', 'translated': 'Eine Kette ist nur so stark wie ihr schwächstes Glied', 'original': 'A chain is only as strong as its weakest link'}
]
```
***Example 2. Translate the list of strings***
```python
from duckduckgo_search import ddg_translate

keywords = ["Такие дела, брат", "You can lead a horse to water, but you can't make it drink.",
            "Ein Spatz in der Hand ist besser, als eine Taube auf dem Dach."]
results = ddg_translate(keywords, from_=None, to='tr')
print(results)
```
```python
[
{'detected_language': 'ru', 'translated': 'Böyle şeyler, kardeşim.', 'original': 'Такие дела, брат'},
{'detected_language': 'en', 'translated': 'Bir atı suya götürebilirsin ama içiremezsin.', 'original': "You can lead a horse to water, but you can't make it drink."},
{'detected_language': 'de', 'translated': 'Elinizdeki serçe çatıdaki bir güvercinden daha iyidir.', 'original': 'Ein Spatz in der Hand ist besser, als eine Taube auf dem Dach.'},
...
]
```

[Go To TOP](#TOP)


## 8. ddg_suggestions() - suggestions by duckduckgo.com

```python
from duckduckgo_search import ddg_suggestions

def ddg_suggestions(
    keywords,
    region="wt-wt",
    output=None,
):
    """DuckDuckGo suggestions. Query params: https://duckduckgo.com/params
    Args:
        keywords (str): keywords for query.
        region (str, optional): wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        output (Optional[str], optional): csv, json. Defaults to None.
    Returns:
        Optional[List[dict]]: DuckDuckGo suggestions results.
    """
```

***Returns***
```python
[{"phrase":str},{"phrase":str},{"phrase":str},...]
```

***Example 1. Suggestions***
```python
from duckduckgo_search import ddg_suggestions

keywords = 'ford'
results = ddg_suggestions(keywords)
print(results)
```
```python
[{"phrase":"ford kögler"},{"phrase":"ford kuga"},{"phrase":"ford focus"},{"phrase":"ford puma"},{"phrase":"ford mustang"},{"phrase":"ford transit"},{"phrase":"ford ranger"},{"phrase":"ford fiesta"}]
```

[Go To TOP](#TOP)
