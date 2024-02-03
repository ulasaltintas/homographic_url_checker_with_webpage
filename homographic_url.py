from urllib.parse import urlparse, urlunparse, quote
from idna import encode, decode

def is_homograph(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Encode the domain part using IDNA encoding
    encoded_domain = encode(parsed_url.netloc).decode('utf-8')

    # Construct a new URL with the encoded domain
    encoded_url = urlunparse((parsed_url.scheme, encoded_domain, *parsed_url[2:]))

    # Compare the original and encoded URLs
    if url != encoded_url:
        print(f"Original URL: {url}")
        print(f"Encoded URL : {encoded_url}")
        print("This URL may be a homograph attack.")
        return True
    else:
        print("The URL is not a homograph attack.")
        return False

# Example usage:
url_to_check = "https://аmazon.com"
is_homograph(url_to_check)