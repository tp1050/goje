from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import codecs
from bs4 import BeautifulSoup


profile = webdriver.FirefoxProfile()
user_agent = "Some UserAgent String here..."
proxy_ip = "127.0.0.1"
proxt_port = "9150"
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", str(proxy_ip))
profile.set_preference("network.proxy.socks_port", int(proxt_port))
profile.set_preference("network.http.use-cache", False)
profile.update_preferences()
binary = FirefoxBinary("/usr/bin/firefox")
driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
driver.get("https://bonbast.com")
html = driver.page_source
file_object = codecs.open("a.html", "w", "utf-8")
file_object.write(html)
file_object.close()

driver.quit()