import csv
from bs4 import BeautifulSoup

source_page = open('../data/cached_List_of_SP_500_companies.html').read()
soup = BeautifulSoup(source_page, 'html.parser')
table = soup.find("table", { "class" : "wikitable sortable" })

# Fail now if we haven't found the right table
header = table.findAll('th')
if header[0].text != "Ticker symbol" or header[1].text != "Security":
    raise Exception("Can't parse wikipedia's table!")

# Retreive the values in the table
records = []
rows = table.findAll('tr')
for row in rows:
    fields = row.findAll('td')
    if fields:
        # use .text instead of .string to handle links + text
        symbol = fields[0].text
        # skipping second field (SEC url, redundant to CIK)
        name = fields[1].text
        sector = fields[3].text
        industry = fields[4].text 
        # skipping sixth field (Date first added, incomplete)
        headquarters = fields[5].text
        cik = fields[7].text
        records.append([symbol, name, sector, industry, headquarters, cik])

# Write out CSV
header = ['Symbol', 'Name', 'Sector', 'Industry', 'Headquarters', 'CIK']
writer = csv.writer(open('../data/sp500.csv', 'w'), lineterminator='\n')
writer.writerow(header)
# Sort to  ensure easy tracking of modifications
records.sort(key=lambda s: s[1].lower())
writer.writerows(records)  