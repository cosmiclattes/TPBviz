import urllib2
import urlparse
import datetime
from lxml import html

from django_cron import CronJobBase, Schedule
from viz.models import TPBTopList

class TpbTopListCronJob(CronJobBase):
    RUN_EVERY_MINS = 10 # every 10 mins
    MIN_NUM_FAILURES = 3

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'viz.TpbTopListCronJob'    # a unique code
    
    base_url = 'https://thepiratebay.se/top'

    categories = {
            'all':'all',
            '48h':'48hall',
            'pictures':'608',
            'e-books':'601',
            'comics':'602'
            }
    
    def getDate(self,created):
        createdDetails = {}
        created = created.replace(u'\xa0', ' ').encode('utf-8')
        created = created.replace('Y-day', str(datetime.datetime.today() - datetime.timedelta(days=1)))
        created = created.replace('Today', datetime.datetime.today().isoformat())
        createdDetails['date'] = created.split(' ')[1]
        createdDetails['time'] = created.split(' ')[2]
        return createdDetails
    def getSize(self):
        pass
    def do():
        category = 'all'
        if category in categories:
            cat = categories[category]
        else: 
            cat = categories['all']
        url = base_url+'/'+cat
        response = urllib2.urlopen(url)
        document = html.parse(response)
        root = document.getroot()
        rows = root.cssselect('#searchResult tr')
        rows = rows[1:]
        seeds = 0
        leeches = 0
        torrentList = []
        for row in rows:
            torrent = {}
            attr = {}
            elements = row.cssselect('td')[1].cssselect('a')[1].get('href').split('&')
            torrent['infohash'] = elements[0].split(':')[-1]
            torrent['url'] =  row.cssselect('.detName a')[-1].get('href')
            torrent['name'] = urlparse.parse_qsl(elements[1])[-1][-1]
            print torrent['name']
            trackers = elements[2:]
            torrent_tracker = {}
            images = row.cssselect('img')
            for image in images:
                title = image.get('title')
                if title:
                    if 'Trusted' in title:
                        attr['status'] = 'Trusted'
                    if 'VIP' in title:
                        attr['status'] = 'VIP'
                    if 'cover' in title:
                        attr['has_cover'] = True
                    if 'comments' in title:
                        attr['comments'] = int(''.join(ele for ele in title if ele.isdigit()))
            if ('has_cover' not in attr):
                attr['has_cover'] = False        
            for idx,tracker in enumerate(trackers):
                torrent_tracker[idx] = urlparse.parse_qsl(tracker)[-1][-1]
            torrent['seeds'] = int(row.getchildren()[2].text)
            print torrent['seeds']
            
            seeds += torrent['seeds']
            torrent['leaches'] = int(row.getchildren()[3].text)
            leeches += torrent['leaches']
            print torrent['leaches']
            torrent['trackers'] = torrent_tracker
            torrent['attrs'] = attr
            cats = row.cssselect('.vertTh a')
            torrent['cat'] = [cats[0].text,cats[1].text]
            #print row.cssselect('a.detDesc')
            if (row.cssselect('a.detDesc')):
                torrent['user'] = row.cssselect('a.detDesc')[0].text
            else:
                torrent['user'] = 'Anonymous'
            torrent['size'] = row.cssselect('font')[0].text.split(',')[1].split(' ')[2:][0].replace(u'\xa0', ' ').encode('utf-8')
            torrent['uploaded'] = getDate(row.cssselect('font')[0].text.split(',')[0])
            #print torrent,seeds,leeches
            torrentList.append(torrent)
            torrentEntry, created = TPBTopList.objects.get_or_create(infoHash = torrent['infohash'])
            print 'torrent', torrent, 'created', created
            if created:
                torrentEntry.name = torrent['name']
                torrentEntry.url = torrent['url']
                torrentEntry.author = torrent['user']
                torrentEntry.seeders = torrent['seeds']
                torrentEntry.leechers = torrent['leaches']
                torrentEntry.attrNoOfComments = torrent['attrs']['comments']
                torrentEntry.attrStatus = torrent['attrs']['status']
                torrentEntry.hasCover = torrent['attrs']['has_cover']
                torrentEntry.save()