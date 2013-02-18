# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import datetime
import json
import matplotlib
import pprint
import re
import webtrends


ACCOUNT = ''
USERNAME = ''
PASSWORD = ''

#xxxx - profile id
#yyyyyyyyyyy -  Id of Key Metrics Summary report
req_url = 'https://ws.webtrends.com/v3/Reporting/profiles/xxxx/reports/yyyyyyyyyyy/?totals=all&start_period=2012m10d01&end_period=2012m10d30&period_type=agg&format=json'

# <codecell>

data = webtrends.get_from_REST(req_url, ACCOUNT,USERNAME, PASSWORD)
if data:
    "Got data from webtrends"

# <codecell>

jdata = json.loads(data)
daily_data = jdata['data'][0]['SubRows'][0]
pageviews = []
dates = []
date_pattern = re.compile(r'^(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<year>[0-9]{4})$')

ts_pageviews = {}

for dte in daily_data:
    date_parts = date_pattern.match(dte)
    if date_parts:
        year = int(date_parts.group('year'))
        month = int(date_parts.group('month'))
        day = int(date_parts.group('day'))
        #We have to get the date into a format matplotlib understands
        #We do this by parsing a string into a pythong datetime object and then applying the mpl function date2num
        #This is so because mpl wants as a float that is number of days since 01-01-1
        py_dte = datetime.date(year, month, day)
        #mpl_date = matplotlib.dates.date2num(py_dte)
        #Store the date together with the number of pageviews
        dates.append(py_dte)
        pageviews.append(daily_data[dte]['measures']['PageViews'])
        
        ts_pageviews[py_dte] = daily_data[dte]['measures']['PageViews']
            
sorted_dates = sorted(ts_pageviews)
sorted_pageviews = []

for x in sorted_dates:
    sorted_pageviews.append(ts_pageviews[x])        
#now that we have all dates and pageviews we get a sorted list together with a matching list of pageviews for matplotlib to plot        


if sorted_dates and sorted_pageviews:
    print "pageviews and dates extracted from webtrends"

# <codecell>

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(sorted_dates, sorted_pageviews, 'o-')
fig.autofmt_xdate()

# <codecell>
