import os
import os.path
import shutil
import re
from random import randrange

from duckduckgo_search import ddg_images


def test_ddg_images():
    results = ddg_images("cat")
    assert len(results) >= 75


def test_ddg_images_pagination():
    results = ddg_images("cat", page=2)
    assert len(results) >= 75


def test_ddg_images_max_results():
    results = ddg_images("cat", max_results=200)
    assert len(results) >= 150


def test_ddg_images_save_csv_json():
    keywords = "cat"
    results = ddg_images(keywords, output="json")
    assert len(results) >= 75

    results = ddg_images(keywords, output="csv")
    assert len(results) >= 75

    # delete files contains keyword in name
    not_files = True
    for name in os.listdir():
        if f"ddg_images_{keywords}" in name:
            if os.path.isfile(name):
                os.remove(name)
                not_files = False
    if not_files:
        raise AssertionError("csv or json files not found")


def test_ddg_images_download():
    keywords = "cat"
    results = ddg_images(keywords, max_results=10, download=True)
    assert len(results) >= 10

    # delete files contains keyword in name
    files = False
    for dir in os.listdir("."):
        if f"ddg_images_{keywords}" in dir:
            for filename in os.listdir(dir):
                filename = f"{os.getcwd()}/{dir}/{filename}"
                if os.path.isfile(filename):
                    os.remove(filename)
                    files = True
    if not files:
        raise AssertionError("images files not found")

    # delete folder contains keyword in name
    for dir in os.listdir():
        if f"ddg_images_{keywords}" in dir:
            if os.path.isdir(dir):
                shutil.rmtree(dir)


def test_ddg_images_args():
    random_chars = "".join(chr(randrange(65, 90)) for i in range(1))
    r = ddg_images(
        keywords=random_chars,
        region="us-en",
        safesearch="Off",
        size="Wallpaper",
        color="color",
        type_image="photo",
        layout="Wide",
        license_image="any",
        max_results=50,
    )
    assert len(r) > 0


def test_ddg_images_not_results():
    random_chars = "".join(chr(randrange(65, 90)) for i in range(100))
    r = ddg_images(
        keywords=random_chars,
        region="ru-ru",
        safesearch="Off",
        size="Wallpaper",
        color="color",
        type_image="photo",
        layout="Wide",
        license_image="any",
        max_results=50,
    )
    assert len(r) == 0


def test_ddg_images_check_image_result_filtering():
    keyword = 'bangladeshi 100 taka note site:https://en.numista.com'
    r1 = ddg_images(keywords=keyword,
                   safesearch='off',
                   layout='Wide',
                   max_results=50,
                   size='Large')

    assert len(r1) >= 50
    filter_func = lambda x : x['width'] > 1280

    r2_filtered = ddg_images(keywords=keyword,
                   safesearch='off',
                   layout='Wide',
                   max_results=50,
                   size='Large',
                   )

    assert  len(r2_filtered) < len(r1)


def test_ddg_images_filter_with_image_download():
    keyword = 'bangladeshi 100 taka note site:en.numista.com'
    filter_func = lambda x: '100 taka' in x['title'].lower() and x['width'] > 1280
    r1 = ddg_images(keywords=keyword,
                    safesearch='off',
                    layout='Wide',
                    max_results=100,
                    size='Large',
                    download=True,
                    filter_results=filter_func
                    )

    assert len(r1) < 100
    flag = False
    for dir in os.listdir("."):
        if f"ddg_images_{keyword[0:keyword.find('site')]}" in dir:
            flag = True
            shutil.rmtree(dir)
            break
        else:
            flag = False


    if not flag:
        raise AssertionError('Path does not exist')

def test_ddg_images_filter_with_image_download_https():
    keyword = 'bangladeshi 100 taka note site:https://www.realbanknotes.com'
    filter_func = lambda x: '100 taka' in x['title'].lower() and x['width'] > 1280
    r1 = ddg_images(keywords=keyword,
                    safesearch='off',
                    layout='Wide',
                    max_results=100,
                    size='Large',
                    download=True,
                    filter_results=filter_func
                    )

    assert len(r1) < 100
    flag = False
    for dir in os.listdir("."):
        if f"ddg_images_{keyword[0:keyword.find('site')]}" in dir:
            flag = True
            shutil.rmtree(dir)
            break
        else:
            flag = False

    if not flag:
        raise AssertionError('Path does not exist')


def test_ddg_images_filter_with_image_download_https_www():
    keyword = 'bangladeshi 100 taka note site:https://realbanknotes.com'
    filter_func = lambda x: '100 taka' in x['title'].lower() and x['width'] > 1280
    r1 = ddg_images(keywords=keyword,
                    safesearch='off',
                    layout='Wide',
                    max_results=100,
                    size='Large',
                    download=True,
                    filter_results=filter_func
                    )

    assert len(r1) < 100
    flag = False
    for dir in os.listdir("."):
        if f"ddg_images_{keyword[0:keyword.find('site')]}" in dir:
            flag = True
            shutil.rmtree(dir)
            break
        else:
            flag = False

    if not flag:
        raise AssertionError('Path does not exist')

def test_ddg_images_custom_header():
    keyword = 'bangladeshi 100 taka note site:realbanknotes.com'
    filter_func = lambda x: x['width'] - x['height'] > 300 and '100 Taka' in x['title']
    custom_h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Referer": "https://www.realbanknotes.com"}
    r = ddg_images(keywords=keyword, safesearch='off', layout='Wide', max_results=50, size='Large'
                   , filter_results=filter_func, download=True,custom_header=custom_h)

    assert len(r) < 50
