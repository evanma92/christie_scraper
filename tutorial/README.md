*Instructions:*

1. Download the entire package "christies_scraper" onto your "Documents" folder. 
2. Navigate to tutorial -> tutorial -> spiders. You will find a file called "user_to_change.py". 
3. Open "user_to_change.py" with TextEdit.
4. Change your Mac username. This can be found on your Finder. Replace <insert username> with the username that you have found.
5. Change the url to scrape. Copy and paste the url you want to scrape between the apostrophe marks ''. Be careful not to remove the apostrophe marks '' or it will not work!
5. In the Terminal app, type "cd ", then drag and drop the package "christies_scraper" from the Downloads folder into Terminal. This will direct you into the directory of the program.
6. Type "cd tutorial"
7. Type "scrapy crawl christies -o <filename>.csv -t csv". Replace <filename> with what you want to name it. 
8. Now repeat steps 5, and 7, remembering to change the url of the auction you want to scrape and the filename you want to save your data as! If you keep the filename the same, it will just keep adding onto your original csv file. 

