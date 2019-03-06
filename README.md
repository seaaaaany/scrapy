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



