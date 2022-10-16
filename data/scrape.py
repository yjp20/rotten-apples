import requests
import pandas as pd
import bs4
from bs4 import BeautifulSoup

# anime_id and anime_name are to be equivalent to the one found in the MAL url as follows: 
# https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood, where anime_id = 5114 and anime_name is Fullmetal_Alchemist__Brotherhood
def review_link(anime_id, anime_name, page_num):
    return "https://myanimelist.net/anime/" + str(anime_id) + "/" + str(anime_name) + "/reviews?sort=mostvoted&filter_check=&filter_hide=&preliminary=on&spoiler=on&p=" + str(page_num)

def get_reviews(anime_id, anime_name, num_reviews):
    f = open(str(anime_id) + ".csv", "w", encoding = "utf-8")
    data = []
    num_pages = int((num_reviews + 19) / 20)
    column_labels = ["anime_id", "review_text", "review_rating", "author_username"]
    for page_num in range(1, num_pages+1):
        html_text = requests.get(review_link(anime_id, anime_name, page_num)).text
        soup = BeautifulSoup(html_text, "html.parser")
        reviews = soup.find_all("div", class_="review-element js-review-element")
        
        #print(soup.find_all("div", class_="review-element js-review-element")[0])
        for review in reviews:
            data_row = []
            data_row.append(anime_id)
            data_row.append("")
            review_contents = review.find("div", class_="text").contents
            for content in review_contents:
                if type(content) == bs4.element.NavigableString and content != '\n':
                    data_row[1] += content
                    #print(content, end="")
            hidden_text = review.find("span", class_="js-hidden")
            if hidden_text:
                for content in review.find("span", class_="js-hidden").contents:
                    if type(content) == bs4.element.NavigableString and content != '\n':
                        data_row[1] += content
            #print(data_row[1])
            #print(review.find("span", class_="js-hidden").contents)
            #print("LMAO")
            data_row.append(review.find("span", class_="num").string)
            #print(review.find("div", class_="username").find("a").string)
            data_row.append(review.find("div", class_="username").find("a").string)
            #print(data_row)
            #print(data_row[1][0])
            data.append(data_row)
    df = pd.DataFrame(data, columns = column_labels)
    df.to_csv(f, index = False, errors = "replace")
    f.close()

