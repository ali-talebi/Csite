
import requests
from bs4 import BeautifulSoup

def GET_DATA_WITH_LINK_FUNC(url) :
    response = requests.get(url)
    status_code = response.status_code

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    a_link = []
    for link in links:
        try:
            new_link = ''
            url_ = link.get('href')
            if len(url_) > 1 :

                if url_[0] in ['#' , ':'  , '' , '?' ] or '.html' in  url_ :
                    continue

                elif url_[0] == '/' :
                    if url[-1] == '/' :
                        url = url[0:-1]
                    new_link = url + url_
                    a_link.append(new_link)


            elif 'https' in url_ or 'http' in url_ :
                new_link = url_

                a_link.append(new_link)

        except Exception as e:
            pass






    p_tags = soup.find_all('p')
    p_tag = []
    for tag in p_tags:
        p_ = tag.text
        p_tag.append(p_)

    s_ = ""
    for i in p_tags:
        s_ += f"{i} . "

    server_name = " "
    if response.headers['server'] :
        server_name = response.headers['server']


    return status_code , a_link , s_ , server_name


