import re
import requests
import csv
from fake_useragent import UserAgent

s = requests.session()
s.keep_alive = False

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

urlResearch = "name headline\">[\s]*<a href=\"(.*?)\""
#正则匹配文章链接
with open("Nature_Com_Art_From.csv", "a+", newline='', encoding="utf-8_sig") as csvfile:
    writer = csv.writer(csvfile)
    #打开csv

    # #Physical sciences
    # for i in [93,94,95,102,103,104,105,106,107,108,125,126,127]:
    #     url_Phy = "https://www.nature.com/subjects/physical-sciences/ncomms?searchType=journalSearch&sort=PubDate&page=" + str(i)
    #     try:
    #         Phy_page_text = requests.get(url=url_Phy,headers=headers,timeout=20).text
    #         print("Phy第{}页读取成功".format(i))
    #         Phy_Url_Raw = re.findall(urlResearch,Phy_page_text,re.S)
    #         num = i
    #         for url in Phy_Url_Raw:
    #             phy_Url = "https://www.nature.com" + url
    #             writer.writerow(["Physical sciences",phy_Url])
    #     except:
    #         print("Phy第{}页爬取失败".format(i))
    #         i += 1
    #         with open("wrong.txt","a+",encoding="utf-8") as f:
    #             f.write(url_Phy)
    #             f.write("\n")


    # Earth and environmental sciences
    # for i in :
    #     url_Earth = "https://www.nature.com/subjects/earth-and-environmental-sciences/ncomms?searchType=journalSearch&sort=PubDate&page=" + str(i)
    #     try:
    #         Earth_page_text = requests.get(url=url_Earth,headers=headers,timeout=20).text
    #         print("Earth第{}页读取成功".format(i))
    #         Earth_Url_Raw = re.findall(urlResearch, Earth_page_text, re.S)
    #         num = i
    #         for url in Earth_Url_Raw:
    #             Earth_Url = "https://www.nature.com" + url
    #             writer.writerow(["Earth and environmental sciences", Earth_Url])
    #     except:
    #         print("Earth第{}页爬取失败".format(i))
    #         i += 1
    #         with open("wrong.txt","a+",encoding="utf-8") as f:
    #             f.write(url_Earth)
    #             f.write("\n")


    # Biological sciences
    for i in [196,197]:
        url_Bio = "https://www.nature.com/subjects/biological-sciences/ncomms?searchType=journalSearch&sort=PubDate&page=" + str(i)
        try:
            Bio_page_text = requests.get(url=url_Bio,headers=headers,timeout=20).text
            print("Biological第{}页读取成功".format(i))
            Bio_Url_Raw = re.findall(urlResearch, Bio_page_text, re.S)
            num = i
            for url in Bio_Url_Raw:
                Bio_Url = "https://www.nature.com" + url
                writer.writerow(["Biological sciences", Bio_Url])
        except:
            print("Biological第{}页爬取失败".format(i))
            i += 1
            with open("wrong.txt","a+",encoding="utf-8") as f:
                f.write(url_Bio)
                f.write("\n")

    #
    # # Health sciences
    # for i in [80,81,82,102,103,104]:
    #     url_Health = "https://www.nature.com/subjects/health-sciences/ncomms?searchType=journalSearch&sort=PubDate&page=" + str(i)
    #     try:
    #         Health_page_text = requests.get(url=url_Health,headers=headers,timeout=20).text
    #         print("Health第{}页读取成功".format(i))
    #         num = i
    #         Health_Url_Raw = re.findall(urlResearch, Health_page_text, re.S)
    #         for url in Health_Url_Raw:
    #             Health_Url = "https://www.nature.com" + url
    #             writer.writerow(["Health sciences", Health_Url])
    #     except:
    #         print("Health第{}页爬取失败".format(i))
    #         i += 1
    #         with open("wrong.txt","a+",encoding="utf-8") as f:
    #             f.write(url_Health)
    #             f.write("\n")


    # # Scientific community and society
    # for i in range(1, 10):
    #     url_society = "https://www.nature.com/subjects/scientific-community-and-society/ncomms?searchType=journalSearch&sort=PubDate&page=" + str(i)
    #     try:
    #         society_page_text = requests.get(url=url_society,headers=headers,timeout=20).text
    #         print("Society第{}页读取成功".format(i))
    #         num = i
    #         society_Url_Raw = re.findall(urlResearch, society_page_text, re.S)
    #         for url in society_Url_Raw:
    #             society_Url = "https://www.nature.com" + url
    #             writer.writerow(["Scientific community and society", society_Url])
    #     except:
    #         print("Society第{}页爬取失败".format(i))
    #         i += 1
    #         with open("wrong.txt","a+",encoding="utf-8") as f:
    #             f.write(url_society)
    #             f.write("\n")