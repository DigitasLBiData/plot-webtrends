import urllib2

def get_from_REST(url, account, username, password):
  """
	Executes a webtrends REST API call

	Keyword arguments:
	url -- url to be called
	account -- WT account name
	username -- webtrends username
	password -- webtrends password
	"""
	
	top_level_url = "https://ws.webtrends.com"
	wt_username = account + '\\' + username
	
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None, top_level_url, wt_username, password)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	# create "opener" (OpenerDirector instance)
	opener = urllib2.build_opener(handler)
	# Install the opener.
	# Now all calls to urllib2.urlopen use our opener.
	urllib2.install_opener(opener)
	#opener.open(a_url)
	response = urllib2.urlopen(url)
	data = response.read()
	
	return data
	
def getWTDate(date_time):
	"""
	Returns the WT representation of the datetime object
	
	Keyword arguments:
	date_time -- python datetime object
	"""
	wt_date_time  = ""
	#if type(date_time) == datetime.datetime:
	wt_date_time += str(date_time.year)
	wt_date_time += "m" + str(date_time.month).zfill(2)
	wt_date_time += "d" + str(date_time.day).zfill(2)
	return wt_date_time
