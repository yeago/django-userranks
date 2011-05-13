This project will allow you to rank your users in percentile groups based
on whatever you want.

To install:

-Add 'rank_cache' field to your UserProfile
-Add a get_points() method to your UserProfile which returns an integer based on
   how you want to rank the user on your site
-Add a USERRANK_TIERS list of tuples to your settings.py Example:

USERRANK_TIERS = [
        ("Decklord",.985),
        ("Deckspert",.95),
        ("Deckster",.85),
        ("Deckkie",.80),
        ("Deckling",.70),
]


Run the 'refresh_ranks' management command on whatever schedule you'd like.
