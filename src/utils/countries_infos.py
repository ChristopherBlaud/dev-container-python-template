import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

# def get_countries():
#   countries = []

#   url = "https://www.numbeo.com/cost-of-living/"
#   res = requests.get(url, headers=headers)
#   soup = BeautifulSoup(res.content, 'html.parser')

#   cost_of_living_options = soup.select('#country > option')
  
#   for option in cost_of_living_options:
#     if option.text != "---Select country---":
#       countries.append(option.text)

#   url = "https://www.numbeo.com/health-care/"
#   res = requests.get(url, headers=headers)
#   soup = BeautifulSoup(res.content, 'html.parser')

#   health_care_options = soup.select('#country > option')
  
#   for option in health_care_options:
#     if not option.text in countries and option.text != "---Select country---":
#       countries.append(option.text)
  
#   return countries

def get_countries():
  country_names = []
  countries_infos = []
  health_care_url_path = "https://www.numbeo.com/health-care/"
  cost_of_living_url_path = "https://www.numbeo.com/cost-of-living/"

  res = requests.get(cost_of_living_url_path, headers=headers)
  soup = BeautifulSoup(res.content, 'html.parser')
  html_elements = soup.select('#country > option')
  
  for option in html_elements:
    if option.text != "---Select country---":
      country_names.append(option.text)

  for country in country_names:
    cost_of_living_url = f"{cost_of_living_url_path}country_result.jsp?country={country.replace(" ", "+")}&displayCurrency=USD"
    health_care_url = f"{health_care_url_path}country_result.jsp?country={country.replace(" ", "+")}"
    countries_infos.append({'name': country, 'cost-of-living-url': cost_of_living_url, 'health-care-url': health_care_url})
  
  return countries_infos