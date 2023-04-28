from bs4 import BeautifulSoup as bs4
import time, re, os, sys
from selenium import webdriver
import pandas as pd

def main():
    driver = webdriver.Firefox(os.getcwd())

    output_file = "reviews.csv"
    if os.path.exists(output_file):
        os.remove(output_file)
    div = '</div>'
    appids = [#'1245620', # Elden Ring
              '289070', # Civ 6
              #'1811260', # FIFA 23
              #'1172620', # Sea of Thieves
              '389730', # TEKKEN 7
              #'990080', # Hogwarts Legacy
              #'1142710', # Total War: Warhammer 3
              #'945360', # Among Us
              #'1097150', # Fall Guys
              #'548430', # Deep Rock Galatic
              '105600', # Terraria
              #'1817230', # Hi-Fi Rush
              #'620980', # Beat Saber
              #'814380', # Sekiro
              #'247080', # Crypt of the NecroDancer
              #'322170', # Geometry Dash
              '413150', # Stardew Valley
              '270880', # American Truck Simulator
              '1343400', # RuneScape
              '438100', # VRChat
              #'1517290', # Battlefield 2042
              '379720', # DOOM
              '72850', # Skyrim
              ]
    opinions = []
    texts = []
    titles = []
    TIME_TO_LOAD = 3
    MAX_REVIEWS = 20000
    for i, id in enumerate(appids):
        url = f'https://steamcommunity.com/app/{id}/reviews/?browsefilter=toprated&snr=1_5_100010_'
        #sys.stdout.flush()
        print(f'{(i+1)}/{len(appids)} url: {url}')
        driver.get(url)
        html = driver.page_source
        soup = bs4(html, 'lxml')
        title = soup.find('div', {'class': 'apphub_AppName ellipsis'}).get_text()
        print(title)
        # Scroll until satisfied
        old_len = -1
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html = driver.page_source
            soup = bs4(html, 'lxml')
            reviews = soup.find_all('div', {'class':'apphub_UserReviewCardContent'})
            if len(reviews) >= MAX_REVIEWS or len(reviews) == old_len:
                break
            old_len = len(reviews)
            time.sleep(TIME_TO_LOAD)
        print('DONE SCROLLING!!!')

        titles.extend([title] * len(reviews))        
        for r in reviews:
            op = r.find('div', {'class':'title'}).get_text().strip()
            text = r.find('div', {'class':'apphub_CardTextContent'})
            text = str(text)[:-len(div)]
            text = text[text.rindex(div)+len(div):]
            text = re.sub(r'<br>|<br/>', ' ', text.strip())
            opinions.append(op)
            texts.append(text)

    df = pd.DataFrame({
        'title': titles,
        'review': texts,
        'opinion': opinions,
    })
    print(df)
    driver.close()
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()