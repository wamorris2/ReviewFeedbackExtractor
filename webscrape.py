from bs4 import BeautifulSoup as bs4
import time, re, shutil, os, sys
from selenium import webdriver
import pandas as pd

def main():
    driver = webdriver.Firefox('/home/wamorris/Projects/NLP_Final_Proj/')

    output_file = "review_text.csv"
    if os.path.exists(output_file):
        os.remove(output_file)
    div = '</div>'
    appids = ['1245620','289070','1811260','1172620','389730','990080','1142710','945360','1097150','548430','105600','1817230','620980',
              '814380','247080','322170','413150','270880','1343400','438100','1517290']
    opinions = []
    texts = []
    titles = []
    TIME_TO_LOAD = 3
    MAX_REVIEWS = 1000
    for i, id in enumerate(appids):
        url = f'https://steamcommunity.com/app/{id}/reviews/?browsefilter=toprated&snr=1_5_100010_'
        sys.stdin.flush()
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
    df.to_csv(output_file)

if __name__ == "__main__":
    main()