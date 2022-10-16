from scrape import *
import pandas as pd

anime_ids = [5114, 9253, 1535, 16498, 30276, 11757, 31964, 38000, 20, 22319, 11061, 19815, 32281, 33486, 25777, 1735, 35760, 4224, 37999, 40748, 1, 22135]
anime_names = ["Fullmetal_Alchemist__Brotherhood", "Steins_Gate", "Death_Note", "Shingeki_no_Kyojin", "One_Punch_Man", "Sword_Art_Online", "Boku_no_Hero_Academia", "Kimetsu_no_Yaiba", "Naruto", "Tokyo_Ghoul", "Hunter_x_Hunter_2011", "No_Game_No_Life", "Kimi_no_Na_wa", "Boku_no_Hero_Academia_2nd_Season", "Shingeki_no_Kyojin_Season_2", "Naruto__Shippuuden", "Shingeki_no_Kyojin_Season_3", "Toradora", "Kaguya-sama_wa_Kokurasetai__Tensai-tachi_no_Renai_Zunousen", "Jujutsu_Kaisen", "Cowboy_Bebop", "Ping_Pong_the_Animation"]

# only start here because I got banned after the first 12 
start_index = 20

# gets all reviews
for a in range(start_index, len(anime_ids)):
    print(anime_ids[a])
    #get_reviews(anime_ids[a], anime_names[a], 1000)
    get_reviews(1, "Cowboy_Bebop", 1000)
