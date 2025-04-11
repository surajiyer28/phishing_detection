
import datetime
import ipaddress
import time
from urllib.parse import urlparse
import re
import requests
import whois
import dns.resolver
import whois
from datetime import datetime

def checkIP(url):
    ip_flag = 0
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        ipaddress.ip_address(hostname)
        ip_flag = 1
    except:
        ip_flag = 0
    return ip_flag

def urlLength(url):
    url_length = len(url)
    return url_length


shortening_regex = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net|shorturl\.at"


def url_shortning(url):
    match = re.search(shortening_regex, url)
    if match:
        return 1
    else:
        return 0
    

def check_At(url):

    if "@" in url:
        flag_At = 1    
    else:
        flag_At = 0    
    return flag_At

def check_double_slash(url):

    pattern = r"//.*?//"
    match = re.search(pattern, url)

    if match:
        return 1
    else:
        return 0
    
def prefix_suffix(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname
    if "-" in domain:
        return 1
    else:
        return 0
    
def httpDomain(url):

    pattern = r"http.*?http"
    match = re.search(pattern, url)
    if match:
        return 1
    else:
        return 0
    

def getDepth(url):
    depth = 0
    for j in range(len(url)):
        if url[j] == "/":
            depth = depth + 1
    return depth



def no_dns_record(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        nameservers = dns.resolver.query(domain,'NS')
        
        if len(nameservers)>0:
            return 0
        else:
            return 1
    except Exception as e:
       
        return 1
    

def whois_registered(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.hostname
        hostname = whois.whois(domain).domain_name
        if type(hostname) == list:
            for each in hostname:
                if re.search(each.lower(), domain):
                    return 0
            return 1
        else:
            if re.search(hostname.lower(), domain):
                return 0
            else:
                return 1     
    except:
        return -1
    



def find_domain_age(url):

    try:
        domain_info = whois.whois(url)
        creation_date = domain_info.creation_date
        
        if not creation_date:
            return -2
        
        if isinstance(creation_date, list):
            creation_date = min(creation_date)

        if not isinstance(creation_date, datetime):
            try:
                creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            except Exception:
                return -2

        today = datetime.now()
        domain_age_days = (today - creation_date).days

        return domain_age_days

    except Exception as e:

        return -1
    

def page_rank(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname

    key = "4k8sg00c48c0sw0cwss4g00wsgs48kos4css4ws0"

    url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
    try:
        request = requests.get(url, headers={'API-OPR':key})
        result = request.json()
        result = result['response'][0]['page_rank_integer']
        if result:
            return result
        else:
            return 0
    except:
        return -1




# print(page_rank('https://files-pdf-73j.pages.dev/?e=x'))