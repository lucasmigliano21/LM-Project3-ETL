![Image text](https://us.123rf.com/450wm/melnyk58/melnyk581905/melnyk58190501215/122981665-joven-futbolista-o-futbolista-con-pelo-largo-en-ropa-deportiva-y-botas-pateando-la-pelota-para-el-go.jpg?ver=6)

# Between Club or National team results, which have more weight in the decision of the 'The Best' woman player award?

### The objective of this analysis is to understand if the decision of each yearly award was influenced by the results of the players in their clubs or in their national teams.

In order to be able to compare data, we will be considering that the best national team every year is the one with more wins per year. On the other hand, we will consider that a success from the players in their clubs is winning the champions league in that year. That been said, we'll proceed to explain the data and sources:

1. [Women national results](https://www.kaggle.com/code/dhirendranarad/football-team-eda/data) this link contains the file (.csv) that was used to analyse which was the best women national team per year. As the Champions League has been played since 2002, we only considered data from 2002 onwards.
2. [The Best awards](https://www.goal.com/en-in/news/fifa-womens-world-player-of-the-year-award-winners/blt12683887fe8df959) this web page has the awarding history with every player since 2000. Scrapped this web page using Selenium. As it lacked from the nationality of each player, we had to scrap another one:
3. [Player of the year](https://www.topendsports.com/sport/soccer/list-player-of-the-year-women.htm) in this case we used BeautifulSoup as the scraping method. We merged both tables to keep only a table with the year, player, team and nationality.
4. [Champions League results](https://www.worldfootball.net/winner/frauen-champions-league/) again we scrapped using Selenium to obtain a table with all the champions through the last 20 years. 

Once the data was treated, cleaned, enriched, transformed and became useful, we exported the files as .csv and worked on them in SQL.
You can find the queries in the following [link](https://github.com/lucasmigliano21/LM-Project3-ETL/tree/master/data#:~:text=women%20football%20analisis.sql). The analysis proves that more players were awarded when their national team had most won matches that year.

## Resources used in this project:

#### Python - pandas
#### Selenium
#### Beautiful Soup
#### MySQL
