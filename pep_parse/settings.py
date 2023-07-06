from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_NAME = 'results'
(BASE_DIR / RESULTS_NAME).mkdir(exist_ok=True)

BOT_NAME = "pep_parse"
SPIDER_MODULES = ["pep_parse.spiders"]

ROBOTSTXT_OBEY = True  # Obey robots.txt rules
ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    f'{RESULTS_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    },
}
