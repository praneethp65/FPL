from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = 'https://fantasy.premierleague.com/statistics'

# Use a headless browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

time.sleep(10)
driver.get(url)
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

player_rows = soup.find_all('div', class_='Media__Body-sc-94ghy9-2 eflLUc')

for player_row in player_rows:
    # Extract player information
    player_name = player_row.find('div', class_='ElementInTable__Name-y9xi40-1 heNyFi').text
    player_team = player_row.find('span', class_='ElementInTable__Team-y9xi40-3 hosEuf').text
    player_position = player_row.find('div', class_='ElementInTable__Info-y9xi40-2 XzKWB').find_all('span')[-1].text
    player_value = player_row.find_next('td').text
    ownership_percentage = player_row.find_next('td').find_next('td').text
    player_form = player_row.find_next('td').find_next('td').find_next('td').text
    
    player_form = float(player_form)
    limit = 7.5
        
    if player_form > limit:
        print(f"Player: {player_name}, Team: {player_team}, Position: {player_position}, Value: {player_value}, Ownership: {ownership_percentage}, Form: {player_form}")
        
