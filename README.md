# coffeeSnobScraper
A quick project in order to get the best deals from the coffeeSnobs forum; those that are free.
This is a simple automation project that involves web scraping through the coffeeSnobs forum, finding new listings and emailing them to the user. This is done so I don't have to sit around and browse the site all day.
The way this has been structured it doesn't need to be running all the time and can be shut down in between runs as current listings are cached in a text file (coffeeListings).
To use this code the user needs to generate an email password with Gmail or some other email service and enter it in a new .env file as described by the .env.example file.
![image](https://user-images.githubusercontent.com/37292117/191873461-de739d83-9e29-4103-b30d-3d6d53bfcb7d.png)
