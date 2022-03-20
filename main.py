import requests
import bs4


url = "https://habr.com"
headers = {'authority': 'mc.yandex.ru',
           'method': 'POST',
           'path': '/watch/24049213?page-url=%2Fru%2Fall%2F&charset=utf-8&browser-info=nb%3A1%3Acl%3A707%3Aar%3A1%3Agdpr%3A14%3Avf%3A7oivoclvhnrnrlmt4hr%3Afu%3A3%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A760%3Acn%3A1%3Adp%3A0%3Als%3A174957697924%3Ahid%3A154168985%3Az%3A300%3Ai%3A20220320142713%3Aet%3A1647768433%3Ac%3A1%3Arn%3A825981669%3Arqn%3A187%3Au%3A1615397491939615516%3Aw%3A734x713%3As%3A1536x864x24%3Ask%3A1.25%3Acpf%3A1%3Aeu%3A0%3Ans%3A1647768415844%3Awv%3A2%3Aco%3A0%3Aadb%3A1%3App%3A3629563401%3Arqnl%3A1%3Ast%3A1647768433&t=gdpr(14)mc(h-1-p-1)lt(234800)aw(1)fid(210)ti(0)&force-urlencoded=1',
           'scheme': 'https',
           'accept': '*/*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'content-length': '0',
           'cookie': 'yandexuid=2981031341555599934; my=YwA=; _ym_uid=1555600522357904477; yuidss=2981031341555599934; gdpr=0; yabs-sid=83029481597767154; is_gdpr=0; is_gdpr_b=CKjwdxDOAygC; ymex=1943599323.yrts.1628239323; yandex_gid=43; computer=1; yandex_login=Egor4it; involved=1; engineering=1; telecommunications=1; i=yQJ4xU7/hYQ+F7v044cuen8pQfBRUU5BM63C88bAJ8RE6LgO7jur1gCZCMbp8jEiC71EkGsdUbsiq2LTfFgE0YCsMVI=; discussion=1; _ym_d=1647277468; _ym_isad=1; yabs-frequency=/5/003R0000000ghHbY/O-2FhFPgnccqHI2sBbxGt_DdPhH5857lnHVa9vzpNqNy____1Z49MUz5j7T_HVp___yTpdkb4MhpVRH586DAzBnKAfvujKN00jgIfCn34kfoj4LWbUDqs4l_UKorHO01XcGPErUFz6UqHI3DDbxWAj0MMBH5G83w83PYVzDMjKKW0ioU052X8TP7j4KWx63sgTW-4tgqHK3iLB1mbG000BH58FDki72L0000j4KWbqyobYOQBafFHVp____HRh1mbG000BH58ATli72L0000j4KWe7gmS9K0002qHM3IRh1mbG000BH5GFjKi72L0000jKM03FrKi72L0000j4M06dImS9K0002qHK25UR1mbG000BH5WFTki72L0000j4L0biqRS980002qHI0OTB1mbG000BH5eALli72L0000j4KW6NImS9K0002qHK2oTh1mbG000BH5W4zoi72L0000jKKW0Qbli72L0000jKNW0-jKi72L0000j4MWm7QmS9K0002qHM2cRx1mbG000BL5m0JKRh1mbG000BH5G8bli7000000j4KWC72mS000002qHO3uQR1m00000BL50045RR1m00000BH580Pji7000000j4KWVrMmS000002qHK0_Qx1m00000BH5e7jLi7000000j4KW0LMmS000002qHM05LR1m00000BH58BQ5Sd000000j4M00rMmS000002qHO2CLR1m00000BL5007___z-000005ImSFWrW6i00020LB1m-3KW3000081Ki73uDM1i0000W5ImSFWre7m00020LB1m/; Session_id=3:1647766413.5.1.1557937054589:JASlBQ:10.1.2:1|285565814.7507624.2.2:7507624|129520109.87915482.2.2:87915482|3:249703.698824.T7GWeu98Tq1o2sEXMLkcpxSGRrY; sessionid2=3:1647766413.5.1.1557937054589:JASlBQ:10.1.2:1|285565814.7507624.2.2:7507624|129520109.87915482.2.2:87915482|3:249703.698824.T7GWeu98Tq1o2sEXMLkcpxSGRrY; ys=udn.cDplZ29yNGl0#wprid.1647767657550672-5148929342754093993-vla1-4440-vla-l7-balancer-8080-BAL-6261#c_chck.4210845684',
           'sec-ch-ua-platform': '"Windows"',
           'Sec-Fetch-Dest': 'empty',
           'origin': 'https://habr.com',
           'referer': 'https://habr.com/ru/all/',
           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
           'sec-ch-ua-mobile': '?0',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'no-cors',
           'sec-fetch-site': 'cross-site',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
           }

response = requests.get(url, headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
KEYWORDS = ['дизайн', 'фото', 'web', 'Python']

ARTICLES = soup.find_all('article')
# TITLE = ARTICLE.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find("span").text
# INFO = ARTICLE.find_all("div", {"class":'article-formatted-body article-formatted-body_version-2'})

for ARTICLE in ARTICLES:
    DATE = ARTICLE.find(class_='tm-article-snippet__datetime-published').find("time")['title']
    LINK = ARTICLE.find(class_='tm-article-snippet__title-link').attrs['href']
    TITLE = ARTICLE.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find("span").text
    INFO = ARTICLE.find_all("div", {"class":'article-formatted-body article-formatted-body_version-2'})
    INFO = set(information.text.strip() for information in INFO)
    for i in INFO:
        list_word = i.split()
        for word in list_word:
            if word in KEYWORDS:
                print(DATE, TITLE, url+LINK)



