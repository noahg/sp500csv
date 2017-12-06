  
sp500.csv: cached_List_of_SP_500_companies.html build.py
	python build.py

cached_List_of_SP_500_companies.html: ../data
	# note ampersand code in real url %26
	curl -o ../data/cached_List_of_SP_500_companies.html "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

../data:
	mkdir ../data  
