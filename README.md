# coffeeSnobScraper V1

A quick project in order to get the best deals from the coffeeSnobs forum; those that are free.

This is a simple automation project that involves web scraping through the coffeeSnobs forum, finding new listings and emailing them to the user. This is done so I don't have to sit around and browse the site all day.

The way this has been structured it doesn't need to be running all the time and can be shut down in between runs as current listings are cached in a text file (coffeeListings).

To use this code the user needs to generate an email password with Gmail or some other email service and enter it in a new .env file as described by the .env.example file.


Future Improvements:
- Being able to send the post description inside the email.
- Screening out listings that aren't within a predetermined area. There is no point sending emails for posts on the other side of the country.
- Potentially screen out some products based on keywords. For example I'm not personally interested in pour over equipment or little breville grinders so these could be removed from emails.
