import json

from datetime import datetime
from itemadapter import ItemAdapter
from bs4 import BeautifulSoup


class MeliChallengePipeline:

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):

        self.file.close()

        rows = []

        with open('items.jl') as f:

            for line in f:

                rows.append(json.loads(line))
                
        with open('items.jl', 'w') as f:
            
            for row in rows:

                l = [tt for tt in [t for t in rows if row['link'] not in t['link']] if row['link'] in tt['links']]

                row['appearences'] = len(l)

                row_copy = row.copy()
                row_copy.pop('links', None)

                f.write(json.dumps(row_copy) + "\n")
                

    def process_item(self, item, spider):

        soup = BeautifulSoup(item['content'], 'lxml')

        line_item = {}
        
        line_item['link'] = item['url']

        # links
        line_item['links'] = [t.get('href') for t in soup.find_all('a') if 'http' in t.get('href',[])]

        line = json.dumps(line_item) + "\n"
        self.file.write(line)

        return item
