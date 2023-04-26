# Dataset Creation

1. Sources of the dataset a. Where did you get the data? b. How did you get the data? c. What is the license of the data if any? e. Link to code used to create the dataset.
    - The data was collected from reviews of 21 games currently available for purchase on Steam.  It was scraped using a combination of Selenium and BeautifulSoup4.  There is no license on the data, and it is publicly available. The code used for scraping can be found [here](something).
<br><br>
2. Description of the dataset a. What is the size of the dataset? b. What is the format of the dataset? c. What is the structure of the dataset?
    - I manually set the cutoff point as a maximum of 1000 reviews for each game and made sure to select games from a variety of genres. In the end, I collected a total of 20,449 reviews.  The two fields I collected were the text of the review itself as well as whether the reviewer recommended the game or not. The data is stored in a csv file.
<br><br>
3. Data models and data structures a. What are the data models used in the dataset? b. What are the data structures used in the dataset?
    - I intend to use the data in the form of a pandas DataFrame for use in my project