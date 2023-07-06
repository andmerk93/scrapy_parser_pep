# from itemadapter import ItemAdapter
from collections import defaultdict
import csv
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
        # только в таком виде отрабатывают автотесты,
        # папка должна создаваться при старте паука,
        # значит имя файла лучше сделать полем объекта

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(self.file, 'w', encoding='utf-8', newline='') as csv_file:
            csv.writer(csv_file, dialect=csv.excel).writerows(
                (
                    ('Status', 'Quantity'),
                    *self.status_count.items(),
                    ('Total', sum(self.status_count.values()))
                )
            )
