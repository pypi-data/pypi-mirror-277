import json
import requests
from bs4 import BeautifulSoup

def fetch_app_store_details(url):

    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # TODO: if name changes, we'll have to handle the code
    script_tag = soup.find(
        "script",
        attrs={"name": "schema:software-application", "type": "application/ld+json"},
    )
    app_details_string = script_tag.string
    app_details = json.loads(app_details_string)

    description = app_details["description"]
    screenshots = app_details["screenshot"]

    return {
        "description": description,
        "screenshots": screenshots,
    }