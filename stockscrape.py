# import libraries
import requests
from bs4 import BeautifulSoup
import csv


####################### function to fetch stock page ###################
def get_stocks():
    '''fetch page at URL'''
    url = "https://gse.com.gh/Market-Statistics/shares"

    '''making HTTP 
        GET requests call to dowload stocks at URL'''
    gse_request_response = requests.get(url)

    if gse_request_response.status_code != 200:
        raise ValueError("Invalind Response from Server")

    print("Passing %s....\n"%(url))

    #parse to BeautifulSoup 
    gse_request_response_soup = BeautifulSoup(gse_request_response.text, 'html.parser')

    #get list of stocks 
    soup_data_title = gse_request_response_soup.findAll('table', {'class':'col-md-12 table-striped table-condensed cf'})
    with open('stockdata.csv', 'a') as stockdatacsvfile:
        writer = csv.writer(stockdatacsvfile)
        for datatable in soup_data_title:
            tableheader = datatable.findAll('th', {'class':'text-center'})[0].text
            #print(tableheader)
            tabledata = datatable.findAll('td', {'class':'numeric text-center'})
            #print(tabledata)
            writer.writerows(tableheader)
            writer.writerows(tabledata)

    print("Done Scraping data")
    
################# running main action ##################################
if __name__ == '__main__':
    print("\nGetting Stock list.....\n")

    ### fetch apge #########
    stock = get_stocks()    