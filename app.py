import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

def scrape_visible_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        
        for tag in soup(["script", "style", "meta", "link", "noscript", "header", "footer", "aside", "nav", "img"]):
            tag.extract()

       
        header_content = soup.find("header")
        header_text = header_content.get_text() if header_content else ""

 
        paragraph_content = soup.find_all("p")
        paragraph_text = " ".join([p.get_text() for p in paragraph_content])

        
        visible_text = f"{header_text}\n\n{paragraph_text}"

        
        visible_text = re.sub(r'\s+', ' ', visible_text)
        return visible_text.strip()
    except Exception as e:
        st.error(f"Error occurred while scraping the data: {e}")
        return None

#ST

def main():
    st.title("Web Data Scraper")

    
    url_input = st.text_input("Enter the URL 👉✏️:", "")

    if st.button("Load Datum 🧈"):
        if url_input:
           
            data = scrape_visible_text_from_url(url_input)
            if data:
                st.success("Data text successfully scraped!")
                st.subheader("Scraped Text :")
                st.write(data)
            else:
                st.warning("Failed to load data from the URL.")
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
