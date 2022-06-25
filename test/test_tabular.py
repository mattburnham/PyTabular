from pytabular import pytabular
tab = pytabular.Tabular()

def test_connection():
	'''
	Does a quick check to the Tabular Class
	To ensure that it can connnect
	'''
	assert tab.Server.Connected


def test_query():
	'''
	Does a quick query on the model and checks if it will return expected value
	'''
	df = tab.Query('EVALUATE {1}')
	assert df.iloc[0]['[Value]'] == 1
