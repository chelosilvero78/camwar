# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import items

class CamwarPipeline(object):
    def __init__(self):
        self.camItemCsv = csv.writer(open('cams.csv', 'wb'))
        self.camItemCsv.writerow(['cam_url'])

    def process_item(self, item, spider):
        cam_url = item["url"]
        self.camItemCsv.writerow([cam_url])
        return item
