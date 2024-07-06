import scrapy
import re  # Import for regular expressions

class WikipediaScraper(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']

    def __init__(self, city, url=None, *args, **kwargs):
        super(WikipediaScraper, self).__init__(*args, **kwargs)
        self.city = city
        self.url = url
    
    def start_requests(self):
        # Replace 'YOUR_WIKIPEDIA_URL' with the URL provided by the user
        yield scrapy.Request(url=self.url, callback=self.parse)

    def clean_paragraph_text(self, text):
        pattern = r"""
        # Match optional leading slash (/)
        (/)?

        # Match optional pronunciation section (captured group 1)
        (\[(?:\s*|\S| )*\]|\([^)]*\)|<[^>]*>)*?        # Capture anything between brackets, parentheses, or HTML tags (including whitespace and non-breaking space)

        # Match optional comma, whitespace, or specific characters (captured group 2)
        (?:,\s*|\s*(?:Kannada pronunciation:|, IAST: Muṃbaī; formerly known as Bombay\[a\]))?

        # Optional trailing characters with specific class (captured group 3)
        (\s*|\s* *.mw-parser-output\s*.*?)?           # Capture any remaining text with specific class (including whitespace and non-breaking space)
    """
        # Replace matched parts with an empty string
        text = re.sub(pattern, "", text)
        text = re.sub(r'\[([^\]]+)\]', '', text)      
        return text.strip()  # Remove leading/trailing whitespace

    def parse(self, response):
        city_name = self.city

        paragraphs = []
        for paragraph in response.css("p"):
            # Get text content, preserving whitespace and line breaks
            paragraph_text = paragraph.css("::text").getall()  # Keep whitespace
            # Join paragraph text parts and clean
            paragraph_text = self.clean_paragraph_text("".join(paragraph_text))
            paragraphs.append(paragraph_text)
            # paragraphs.append("".join(paragraph_text))

        # Create a dictionary for the city data (if paragraphs and image exist)
        if paragraphs:
            city_data = {
                "city": city_name,
                "paragraphs": " ".join(paragraphs).strip()
            }
            yield city_data