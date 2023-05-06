import string
import random


class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.characters = string.ascii_letters + string.digits
        self.base_url = "https://your-domain.com/"

    def shorten_url(self, url):
        short_code = self.generate_short_code()
        short_url = self.base_url + short_code
        self.url_map[short_code] = url
        return short_url

    def generate_short_code(self, length=6):
        return "".join(random.choice(self.characters) for _ in range(length))

    def expand_url(self, short_url):
        short_code = short_url.replace(self.base_url, "")
        return self.url_map.get(short_code, None)


# Create an instance of the URLShortener
shortener = URLShortener()

# Shorten a URL
short_url = shortener.shorten_url("https://www.example.com")

# Print the shortened URL
print("Shortened URL:", short_url)

# Expand the shortened URL
original_url = shortener.expand_url(short_url)

# Print the original URL
print("Original URL:", original_url)
