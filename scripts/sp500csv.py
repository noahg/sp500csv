import csv
from bs4 import BeautifulSoup

source_page = open('../data/cached_List_of_SP_500_companies.html').read()
soup = BeautifulSoup(source_page, 'html.parser')
table = soup.find("table", { "class" : "wikitable sortable" })

# Fail now if we haven't found the right table
header = table.findAll('th')
if header[0].string != "Ticker symbol" or header[1].string != "Security":
    raise Exception("Can't parse wikipedia's table!")

# Retreive the values in the table
records = []
rows = table.findAll('tr')
for row in rows:
    fields = row.findAll('td')
    if fields:
        symbol = fields[0].string
        # skipping second field (SEC url, redundant to CIK)
        name = fields[1].a.string           #sometimes has multiple elements so select the first link
        sector = fields[3].string
        industry = fields[4].string 
        # skipping sixth field (Date first added, incomplete)
        headquarters = fields[5].a.string   #sometimes has multiple elements so select the link
        cik = fields[7].string
        records.append([symbol, name, sector, industry, headquarters, cik])

# Write out CSV
header = ['Symbol', 'Name', 'Sector', 'Industry', 'Headquarters', 'CIK']
writer = csv.writer(open('../data/sp500.csv', 'w'), lineterminator='\n')
writer.writerow(header)
# Sort to  ensure easy tracking of modifications
records.sort(key=lambda s: s[1].lower())
writer.writerows(records)  