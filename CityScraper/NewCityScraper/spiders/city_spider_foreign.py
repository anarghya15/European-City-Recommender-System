import scrapy
import re  # Import for regular expressions

class CityParagraphsSpider(scrapy.Spider):
  name = "foreign_city_data_scraper"
  start_urls = ["https://en.wikipedia.org/wiki/Paris","https://en.wikipedia.org/wiki/Madrid","https://en.wikipedia.org/wiki/Ruhr","https://en.wikipedia.org/wiki/Milan","https://en.wikipedia.org/wiki/Barcelona","https://en.wikipedia.org/wiki/Berlin","https://en.wikipedia.org/wiki/Naples","https://en.wikipedia.org/wiki/Athens","https://en.wikipedia.org/wiki/Rome","https://en.wikipedia.org/wiki/Rotterdam","https://en.wikipedia.org/wiki/Lisbon","https://en.wikipedia.org/wiki/Budapest","https://en.wikipedia.org/wiki/Brussels","https://en.wikipedia.org/wiki/Stockholm","https://en.wikipedia.org/wiki/Hamburg","https://en.wikipedia.org/wiki/Munich","https://en.wikipedia.org/wiki/Bucharest","https://en.wikipedia.org/wiki/Frankfurt","https://en.wikipedia.org/wiki/Vienna","https://en.wikipedia.org/wiki/Warsaw","https://en.wikipedia.org/wiki/Amsterdam","https://en.wikipedia.org/wiki/Copenhagen","https://en.wikipedia.org/wiki/Valencia","https://en.wikipedia.org/wiki/Turin","https://en.wikipedia.org/wiki/Lyon","https://en.wikipedia.org/wiki/Marseille","https://en.wikipedia.org/wiki/Dublin","https://en.wikipedia.org/wiki/Porto","https://en.wikipedia.org/wiki/Lille","https://en.wikipedia.org/wiki/Prague","https://en.wikipedia.org/wiki/Seville","https://en.wikipedia.org/wiki/Sofia","https://en.wikipedia.org/wiki/Toulouse","https://en.wikipedia.org/wiki/Utrecht","https://en.wikipedia.org/wiki/Nice","https://en.wikipedia.org/wiki/Thessaloniki","https://en.wikipedia.org/wiki/Bordeaux","https://en.wikipedia.org/wiki/Bilbao","https://en.wikipedia.org/wiki/Florence","https://en.wikipedia.org/wiki/Palermo","https://en.wikipedia.org/wiki/Krak%C3%B3w","https://en.wikipedia.org/wiki/Nuremberg","https://en.wikipedia.org/wiki/Zaragoza","https://en.wikipedia.org/wiki/Zagreb","https://en.wikipedia.org/wiki/Pozna%C5%84","https://en.wikipedia.org/wiki/Mannheim","https://en.wikipedia.org/wiki/Leipzig","https://en.wikipedia.org/wiki/Wroc%C5%82aw","https://en.wikipedia.org/wiki/Vilnius","https://en.wikipedia.org/wiki/Genoa","https://en.wikipedia.org/wiki/Ostrava","https://en.wikipedia.org/wiki/Bologna","https://en.wikipedia.org/wiki/Grenoble","https://en.wikipedia.org/wiki/Granada","https://en.wikipedia.org/wiki/Vigo","https://en.wikipedia.org/wiki/Eindhoven","https://en.wikipedia.org/wiki/Brno","https://en.wikipedia.org/wiki/Heidelberg","https://en.wikipedia.org/wiki/Ghent","https://en.wikipedia.org/wiki/Venice","https://en.wikipedia.org/wiki/Groningen","https://en.wikipedia.org/wiki/Plovdiv","https://en.wikipedia.org/wiki/Verona","https://en.wikipedia.org/wiki/Monte_Carlo", "https://en.wikipedia.org/wiki/Annecy","https://en.wikipedia.org/wiki/Leeds","https://en.wikipedia.org/wiki/Igualada","https://en.wikipedia.org/wiki/Trento","https://en.wikipedia.org/wiki/Freiburg_im_Breisgau","https://en.wikipedia.org/wiki/Cluses","https://en.wikipedia.org/wiki/Bergen","https://en.wikipedia.org/wiki/Cesena","https://en.wikipedia.org/wiki/Wexford","https://en.wikipedia.org/wiki/Bavaria","https://en.wikipedia.org/wiki/Tuscany","https://en.wikipedia.org/wiki/Innsbruck","https://en.wikipedia.org/wiki/Oxford","https://en.wikipedia.org/wiki/Interlaken","https://en.wikipedia.org/wiki/Manchester","https://en.wikipedia.org/wiki/Klagenfurt","https://en.wikipedia.org/wiki/Trondheim","https://en.wikipedia.org/wiki/%C3%89vora","https://en.wikipedia.org/wiki/Lucerne","https://en.wikipedia.org/wiki/Jyv%C3%A4skyl%C3%A4","https://en.wikipedia.org/wiki/Delft","https://simple.wikipedia.org/wiki/Bath,_Somerset","https://en.wikipedia.org/wiki/Lourdes","https://en.wikipedia.org/wiki/Avignon","https://en.wikipedia.org/wiki/Pforzheim","https://en.wikipedia.org/wiki/Jablonec_nad_Nisou","https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa","https://en.wikipedia.org/wiki/Randersacker","https://en.wikipedia.org/wiki/Po_Valley","https://en.wikipedia.org/wiki/Colmar","https://en.wikipedia.org/wiki/Erlangen","https://en.wikipedia.org/wiki/Kecskem%C3%A9t","https://en.wikipedia.org/wiki/D%C3%BCsseldorf","https://en.wikipedia.org/wiki/Cluj-Napoca","https://en.wikipedia.org/wiki/Aosta","https://en.wikipedia.org/wiki/Durham,_England","https://en.wikipedia.org/wiki/Salzburg","https://en.wikipedia.org/wiki/Sz%C3%A9kesfeh%C3%A9rv%C3%A1r","https://en.wikipedia.org/wiki/Foggia","https://en.wikipedia.org/wiki/Nitra","https://en.wikipedia.org/wiki/Tarn%C3%B3w","https://en.wikipedia.org/wiki/Edinburgh","https://en.wikipedia.org/wiki/C%C3%A1ceres,_Spain","https://en.wikipedia.org/wiki/La_Rochelle","https://en.wikipedia.org/wiki/Pisa","https://en.wikipedia.org/wiki/Pleven","https://en.wikipedia.org/wiki/W%C3%BCrzburg","https://en.wikipedia.org/wiki/Rijeka","https://en.wikipedia.org/wiki/Linz","https://en.wikipedia.org/wiki/Sibiu","https://en.wikipedia.org/wiki/Dortmund","https://en.wikipedia.org/wiki/Seraing","https://en.wikipedia.org/wiki/Sheffield","https://en.wikipedia.org/wiki/Slough","https://en.wikipedia.org/wiki/Rovigo","https://en.wikipedia.org/wiki/Valence,_Dr%C3%B4me","https://en.wikipedia.org/wiki/Espoo","https://en.wikipedia.org/wiki/Santa_Croce_sull%27Arno","https://en.wikipedia.org/wiki/Zl%C3%ADn","https://en.wikipedia.org/wiki/Prato","https://en.wikipedia.org/wiki/Siena","https://en.wikipedia.org/wiki/Constan%C8%9Ba","https://en.wikipedia.org/wiki/Geneva","https://en.wikipedia.org/wiki/Toledo,_Spain","https://en.wikipedia.org/wiki/Uppsala","https://en.wikipedia.org/wiki/Sighi%C8%99oara","https://en.wikipedia.org/wiki/Avignon","https://en.wikipedia.org/wiki/Berat","https://en.wikipedia.org/wiki/La_D%C3%A9fense","https://en.wikipedia.org/wiki/Esch-sur-Alzette","https://en.wikipedia.org/wiki/Milton_Keynes","https://en.wikipedia.org/wiki/Schwerin","https://en.wikipedia.org/wiki/C%C3%B3rdoba,_Spain","https://en.wikipedia.org/wiki/Marv%C3%A3o","https://en.wikipedia.org/wiki/Carcassonne","https://en.wikipedia.org/wiki/Plze%C5%88","https://en.wikipedia.org/wiki/Graz","https://en.wikipedia.org/wiki/Essen","https://en.wikipedia.org/wiki/Rothenburg_ob_der_Tauber","https://en.wikipedia.org/wiki/Garmisch-Partenkirchen","https://en.wikipedia.org/wiki/Gstaad","https://en.wikipedia.org/wiki/Cambridge","https://en.wikipedia.org/wiki/Trentino-Alto_Adige/S%C3%BCdtirol","https://en.wikipedia.org/wiki/Valletta","https://en.wikipedia.org/wiki/Sintra","https://en.wikipedia.org/wiki/Dubrovnik","https://en.wikipedia.org/wiki/Birmingham","https://en.wikipedia.org/wiki/Carmona,_Spain","https://en.wikipedia.org/wiki/Santiago_de_Compostela","https://en.wikipedia.org/wiki/Canterbury","https://en.wikipedia.org/wiki/Lutry","https://en.wikipedia.org/wiki/Assisi","https://en.wikipedia.org/wiki/Set%C3%BAbal","https://en.wikipedia.org/wiki/Como","https://en.wikipedia.org/wiki/London","https://en.wikipedia.org/wiki/Ljubljana","https://en.wikipedia.org/wiki/Schiphol-Rijk","https://en.wikipedia.org/wiki/Basel","https://en.wikipedia.org/wiki/Bristol","https://en.wikipedia.org/wiki/Szeged"]


  def clean_paragraph_text(self, text):
    pattern = r"""
    # Match optional leading slash (/)
    (/)?

    # Match optional pronunciation section (captured group 1)
    (\[(?:\s*|\S| )*\]|\([^)]*\)|<[^>]*>)*?

    # Match optional comma, whitespace, or specific characters (captured group 2)
    (?:,\s*|\s*(?:Kannada pronunciation:|, IAST: Muṃbaī; formerly known as Bombay\[a\]))?

    # Optional trailing characters with specific class (captured group 3)
    (\s*|\s* *.mw-parser-output\s*.*?)?
"""

    # Replace matched parts with an empty string
    text = re.sub(pattern, "", text)
    text = re.sub(r'\[([^\]]+)\]', '', text)      
    return text.strip()  # Remove leading/trailing whitespace

  def parse(self, response):
    city_name = response.url.split("/")[-1]  # Extract city name from URL

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
