# S&P 500 csv
Download a list of companies in the S&P 500 as a csv file. 

## How to use
Just download the `data/sp500.csv` file from this repo.

See `datapackage.json` for table schema.

Or, build the csv yourself:

1. `git clone git@github.com:noahg/sp500csv.git`

2.  `cd sp500csv/scripts`

    `pip install -r requirements.txt`

3. `make`

## Source
The data is scrapped from the Wikipedia page: https://en.wikipedia.org/w/index.php?title=List_of_S%26P_500_companies

It appears as that the above is a frequently maintained, see recent changes list on the same page.

## Credits
This is a simplified version of [DataHub](https://datahub.io/)'s repository [s-and-p-500-companies](https://github.com/datasets/s-and-p-500-companies). 