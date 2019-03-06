# scrapy

### 1. Scrapy example

Establish a Scarapy project, use **scrapy startproject** under shell.

```shell
scrapy startproject example
New Scrapy project 'example', using template directory '/anaconda3/lib/python3.6/site-packages/scrapy/templates/project', created in:
    /Users/sean/Documents/GitHub/scrapy/Python Script/example

You can start your first spider with:
    cd example
    scrapy genspider example example.com
```

Test it by typing `tree example`

```shell
Script sean$ tree example
example
├── example
│   ├── __init__.py
│   ├── __pycache__
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg
```

Run `book_spider.py` and it will generate a csv file with the full list of the books' information.

Here is a scrapy report.

```shell
{'downloader/request_bytes': 15008,
 'downloader/request_count': 51,
 'downloader/request_method_count/GET': 51,
 'downloader/response_bytes': 299924,
 'downloader/response_count': 51,
 'downloader/response_status_count/200': 50,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2019, 3, 6, 6, 7, 47, 472406),
 'item_scraped_count': 1000,
 'log_count/DEBUG': 1051,
 'log_count/INFO': 10,
 'memusage/max': 52948992,
 'memusage/startup': 52948992,
 'request_depth_max': 49,
 'response_received_count': 51,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 50,
 'scheduler/dequeued/memory': 50,
 'scheduler/enqueued': 50,
 'scheduler/enqueued/memory': 50,
 'start_time': datetime.datetime(2019, 3, 6, 6, 7, 30, 954696)}
```

