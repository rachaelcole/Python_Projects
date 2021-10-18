from urllib.request import urlopen

# Open URL and use .read() method to read the page's HTML
url = 'http://olympus.realpython.org/profiles/dionysus'
html_page = urlopen(url)
html_text = html_page.read().decode('utf-8')

# Use a for loop to extract desired text (here, name and favourite colour)
for string in ["Name: ", "Favorite Color: "]:
    string_start_idx = html_text.find(string)  # Use to find starting index of either name or fav color string
    text_start_idx = string_start_idx + len(string)  # get index of char immediately after ':'
    next_html_tag_offset = html_text[text_start_idx:].find("<")  # find index of first '<' relative to start index
    text_end_idx = text_start_idx + next_html_tag_offset  # find text end index by adding text start and next tag indexes
    raw_text = html_text[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")  # removes whitespace from raw text
    print(clean_text)
