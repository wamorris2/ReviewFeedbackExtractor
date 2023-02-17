# ReviewFeedbackExtractor

Developing a video game is a complicated process. And getting feedback is an important part of that process! Steam early access gives developers feedback before their game's actual release, and even after release, patches allow a developer to constantly improve their game.  For that, it's important that they extract useful information to improving their game from the players' reviews.  Using natural language processing, this application will be able to take a user's review and answer the following questions:
- What parts of the game stand out the most to players?
- What things did players enjoy the most?
- What things did players enjoy the least?
- and more...

The valuable answers to these questions will allow developers to more closely understand what players find the most compelling about their game, so they know to spend more development time on them!


## Pipeline

- Data from Steam (store.steampowered.com) reviews for games
- Scrape steam reviews by parsing html with BeautifulSoup (div with class='Reviews_summary')
- Compact reviews in single blob of text
- ...
