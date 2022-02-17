import time
import requests
import re
from fake_useragent import UserAgent
from lxml import etree
import csv
from xml.etree import ElementTree

s = requests.session()
s.keep_alive = False
# 关闭多余链接

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}
#随机指定user agent

urlList = []
urlMetrics_List = []
page = 1500
for page in range(1500,1501):
    getArt_URL_content = "https://www.nature.com/ncomms/research-articles?searchType=journalSearch&sort=PubDate&page=" + str(page)
    page_text = requests.get(getArt_URL_content,headers=headers).text
    Url_research = "itemprop=\"name headline\">\s*<a href=\"(.*?)\""  #正则匹配文章子链接
    # print(re.findall(Url_research,page_text,re.S),type(re.findall(Url_research,page_text,re.S)))
    urlListRaw = re.findall(Url_research,page_text,re.S)
    for item in urlListRaw:
        Art_Url = "https://www.nature.com" + item
        urlList.append(Art_Url)
    print("目录第{}页爬取成功".format(page))
    page += 1
#获取文章链接，metrics链接


with open("Article_Data.csv", "w", newline='', encoding="utf-8_sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Title", "文章链接","Open Access", "Ciatation", "Citation爬取时间","Additional Information","Peer review", "Receive Date", "Accept Date", "Publish Date", "Altmetric", "Altmetric爬取时间"])
    for url in urlList:
        page_text = requests.get(url=url,headers = headers).text
        title_Search = "<title>([\s\S]*?)\|[\s\S]*</title>"
        artTitle = re.findall(title_Search,page_text,re.S)[0]
        print('Title是{}'.format(artTitle))
        #获取文章标题

        try:
            openAccess_Search = '<li class=\"c-article-identifiers__item\">[\s\n\r]*<span class=\"c-article-identifiers__open\" data-test=\"open-access\">(.*?)</span>'
            openAccess = re.findall(openAccess_Search,page_text,re.S)
            print("有Open Access")
            OpenAccess_csv = 1
        except:
            print("无Open Access")
            OpenAccess_csv = 0
        #获取Open Access

        tree = etree.HTML(page_text)
        try:
            citation = tree.xpath('//span[text()="Citations"]/../text()')[0]
            print("citation是{}".format(citation))
            citation_time = time.strftime('%Y-%m-%d', time.localtime())
        except:
            print('citation = 0')
            citation = 0
            citation_time = time.strftime('%Y-%m-%d', time.localtime())
        #获取Citation

        try:
            peer_review = tree.xpath("//*[@class='print-link' and contains(text(),'Peer Review File')]/@href")[0]
            #print(1)
            print("有open peer review")
            Peer_Review_csv = 1
        except:
            print("无open peer review")
            Peer_Review_csv = 0
        #获取peer review

        try:
            receiveDate_Search= '<p>Received<span class=\"u-hide\">: </span><span class=\"c-bibliographic-information__value\"><time datetime=\"(.*?)\">'
            receiveDate = re.findall(receiveDate_Search,page_text,re.S)[0]
            print("Receive Date是{}".format(receiveDate))
        except:
            print("Receive Date 爬取失败")
        #获取Receive Date

        try:
            acceptDate_Search= '<p>Accepted<span class=\"u-hide\">: </span><span class=\"c-bibliographic-information__value\"><time datetime=\"(.*?)\">'
            acceptDate = re.findall(acceptDate_Search,page_text,re.S)[0]
            print("Accept Date是{}".format(acceptDate))
        except:
            print("Accept Date 爬取失败")
        #获取Accept Date

        try:
            publishDate_Search= '<p>Published<span class=\"u-hide\">: </span><span class=\"c-bibliographic-information__value\"><time datetime=\"(.*?)\">'
            publishDate = re.findall(publishDate_Search,page_text,re.S)[0]
            print("Publish Date是{}".format(publishDate))
        except:
            print("Publish Date 爬取失败")
        #获取Publish Date

        try:
            addInformatin_raw = tree.xpath('//*[@id="additional-information-content"]')[0]
            addInformatin = addInformatin_raw.xpath('string(.)')
            print("addInformatin是{}".format(addInformatin))
        except:
            try:
                addInformatin_raw = tree.xpath("//h2[text()='Additional information']/..//div//text()")
                str = ' '
                addInformatin = str.join(addInformatin_raw)
                print(addInformatin)
                print("addInformatin是{}".format(addInformatin))
            except:
                addInformatin = 0
                print("无additional infomation 或者爬取失败")
        print("{}主页面爬取完成,网址是{}".format(artTitle,url))

        print("开始爬取metrics界面")
        urlMetrics = url + "/metrics"
        metrics_page_text = requests.get(url=urlMetrics,headers=headers).text
        try:
            altmetrics_Search = "<div.*class=\"c-article-metrics__image\">[\s\r\n]*<img.*alt=\"Altmetric\s*score\s*(.*?)\""
            altmetrics = re.findall(altmetrics_Search,metrics_page_text,re.S)[0]
            altmetricsTime_Search = "<li\sclass=\"c-article-identifiers__item\">Last\supdated:\s.*?,\s(.*?)\s\d{0,2}:"
            altmetricsTime = re.findall(altmetricsTime_Search,metrics_page_text,re.S)[0]
            print("{}的altmetrics是{}".format(urlMetrics,altmetrics))
            print("{}的almetrics爬取时间是{}".format(urlMetrics,altmetricsTime))
        except:
            print("{}图片加载缓慢，尝试休息20秒".format(urlMetrics))
            time.sleep(20)
            try:
                altmetrics_Search = "<div.*class=\"c-article-metrics__image\">[\s\r\n]*<img.*alt=\"Altmetric\s*score\s*(.*?)\""
                altmetrics = re.findall(altmetrics_Search, metrics_page_text, re.S)[0]
                altmetricsTime_Search = "<li\sclass=\"c-article-identifiers__item\">Last\supdated:\s.*?,\s(.*?)\s\d{0,2}:"
                altmetricsTime = re.findall(altmetricsTime_Search, metrics_page_text, re.S)[0]
                print("{}的altmetrics是{}".format(urlMetrics,altmetrics))
                print("{}的almetrics爬取时间是{}".format(urlMetrics,altmetricsTime))
            except:
                print("{}的metrics加载失败 或者 为0".format(urlMetrics))

        writer.writerow(
            [artTitle, url, OpenAccess_csv, citation, citation_time,addInformatin, Peer_Review_csv, receiveDate, acceptDate,
             publishDate,altmetrics,altmetricsTime])
        print("csv写入成功")
        print('\n')

