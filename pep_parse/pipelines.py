# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from collections import defaultdict
from csv import DictWriter
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        date = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        self.file = results_dir / f'status_summary_{date}.csv'

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.status_count['Total'] = sum(self.status_count.values())
        with open(self.file, 'w', newline='') as csv_file:
            fieldnames = ['Status', 'Quantity']
            writer = DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for status, quantity in self.status_count.items():
                writer.writerow({'Status': status, 'Quantity': quantity})
