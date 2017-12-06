sp500.csv: cached_List_of_SP_500_companies.html sp500csv.py
	python sp500csv.py

cached_List_of_SP_500_companies.html:
	# note ampersand code in real url %26
	curl -o cached_List_of_SP_500_companies.html "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
