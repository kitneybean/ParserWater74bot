import aspose.words as aw
import requests
from bs4 import BeautifulSoup
import urllib3

def parsing_aktsii():
    
        doc = aw.Document()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        builder = aw.DocumentBuilder(doc)
        font = builder.font
        font.size = 14
        font.name = "Arial"
        paragraphFormat = builder.paragraph_format

        def ActionGO():
            try:
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Горный Оазис"')
                builder.writeln('')
                font.size = 14
                url = 'https://www.74mv.ru/aktsii'
                n = requests.get(url)
                soup = BeautifulSoup(n.text, 'html.parser')
                items = soup.find_all('div', class_="page-header")
                for item in items:
                    tempurl = 'https://www.74mv.ru' + item.find('a').get('href')
                    tempn = requests.get(tempurl)
                    tempsoup = BeautifulSoup(tempn.text, 'html.parser')
                    tempitems = tempsoup.find('div', class_ = 'item-page')
                    title = item.find('h2').get_text(strip=True)
                    descriprion = tempitems.find('div', class_='seo').get_text(strip=True)
                    font.bold = True
                    paragraphFormat.first_line_indent = 0
                    paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                    paragraphFormat.keep_together = True
                    builder.writeln(str(title))
                    builder.writeln('')
                    font.bold = False
                    paragraphFormat.first_line_indent = 28
                    paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
                    builder.writeln(str(descriprion))
                    builder.writeln('')
            except:
                print("Ошибка с ActionGO")

        def ActionAM():
            try:
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Аквамобиль"')
                builder.writeln('')
                font.size = 14
                url = 'https://aqua-mobil.ru/aktsii/'
                response = requests.get(url, verify=False)
                soup = BeautifulSoup(response.text, 'html.parser')
                items = soup.find_all('a', class_='zakazblock')
                for item in items:
                    tempurl = 'https://aqua-mobil.ru' + str(item.get('href'))
                    tempresponse = requests.get(tempurl, verify=False)
                    tempsoup = BeautifulSoup(tempresponse.text, 'html.parser')
                    tempitem = tempsoup.find('div', class_='blockin')
                    title = tempitem.find('h1').get_text(strip=True)
                    descriprion = tempitem.find('div', class_='maxcontent').get_text(strip=True)
                    font.bold = True
                    paragraphFormat.first_line_indent = 0
                    paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                    paragraphFormat.keep_together = True
                    builder.writeln(str(title))
                    builder.writeln('')
                    font.bold = False
                    paragraphFormat.first_line_indent = 28
                    paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
                    builder.writeln(str(descriprion))
                    builder.writeln('')
            except:
                print("Ошибка с ActionAM")

        def ActionVK():
            try:
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Власов Ключ"')
                builder.writeln('')
                font.size = 14
                url = 'http://vlasovkluch.ru/news/'
                response = requests.get(url, verify=False)
                soup = BeautifulSoup(response.text, 'html.parser')
                items = soup.find_all('div', class_='col-4 col-lg-6 col-mdd-12 mrb-15')
                for item in items:
                    check = item.find('span').get_text(strip=True)
                    if check=='акции':
                        title = item.find('div', class_='title-slide-new').get_text(strip=True)
                        description = item.find('div', class_='text-slide-new').get_text(strip=True)
                        font.bold = True
                        paragraphFormat.first_line_indent = 0
                        paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                        paragraphFormat.keep_together = True
                        builder.writeln(str(title))
                        builder.writeln('')
                        font.bold = False
                        paragraphFormat.first_line_indent = 28
                        paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
                        builder.writeln(str(description))
                        builder.writeln('')
            except:
                print("Ошибка с ActionVK")

        def ActionZK():
            try:    
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Живой ключ"')
                builder.writeln('')
                font.size = 14
                url = 'https://живаякапля.рф/sale/'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                items = soup.find_all('div', class_='item-wrapper col-lg-3 col-md-4 col-sm-6 col-xs-6 col-xxs-12 clearfix')
                for item in items:
                    tempurl = 'https://живаякапля.рф/sale/' + item.find('a').get('href')
                    tempresponse = requests.get(tempurl, verify=False)
                    tempsoup = BeautifulSoup(tempresponse.text, 'html.parser')
                    title = tempsoup.find('h1').get_text(strip=True)
                    descriprion = tempsoup.find('div', class_ = 'content-text muted777').get_text(strip=True)
                    font.bold = True
                    paragraphFormat.first_line_indent = 0
                    paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                    paragraphFormat.keep_together = True
                    builder.writeln(str(title))
                    builder.writeln('')
                    font.bold = False
                    paragraphFormat.first_line_indent = 28
                    paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
                    builder.writeln(str(descriprion))
                    builder.writeln('')
            except:
                print("Ошибка с ActionZK")

        def ActionLV():
            try:
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Люкс Вода"')
                builder.writeln('')
                font.size = 14
                num_of_page = 2
                for i in range(num_of_page):
                    url = 'https://l-w.ru/promo/?PAGEN_1='+ str(i + 1)
                    response = requests.get(url, verify=False)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    items = soup.findAll('div', class_='stocks__item-info')
                    for item in items:
                        title = item.find('div').get_text(strip=True)
                        descriprion =  item.find(class_='stocks__item-date').get_text(strip=True)
                        font.bold = True
                        paragraphFormat.first_line_indent = 0
                        paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                        paragraphFormat.keep_together = True
                        builder.writeln(str(title))
                        builder.writeln('')
                        font.bold = False
                        paragraphFormat.first_line_indent = 28
                        paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
                        builder.writeln(str(descriprion))
                        builder.writeln('')
            except:
                print("Ошибка с ActionLV")

        def ActionNI():
            try:    
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Ниагара"')
                builder.writeln('')
                font.size = 14
                url = 'https://niagara74.ru/stock/'
                response = requests.get(url, verify=False)
                soup = BeautifulSoup(response.text, 'html.parser')
                items = soup.find_all('div', class_='item col-md-4 col-sm-6')
                for item in items:
                    temp2 = item.find('a')
                    itemurl = 'https://niagara74.ru' + str(temp2.get('href'))
                    itemresponse = requests.get(itemurl, verify=False)
                    itemsoup = BeautifulSoup(itemresponse.text, 'html.parser')
                    title = itemsoup.find('h1').get_text(strip=True)
                    description = itemsoup.find('div', class_='article').get_text(strip=True)
                    font.bold = True
                    paragraphFormat.first_line_indent = 0
                    paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                    paragraphFormat.keep_together = True
                    builder.writeln(str(title))
                    builder.writeln('')
                    font.bold = False
                    paragraphFormat.first_line_indent = 28
                    paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
                    builder.writeln(str(description))
                    builder.writeln('')
            except:
                print("Ошибка с ActionNI")

        def ActionCI():
            try:
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Чебаркульский исток"')
                builder.writeln('')
                font.size = 14
                url = 'https://chebistok.ru/'
                response = requests.get(url, verify=False)
                soup = BeautifulSoup(response.text, 'html.parser')
                items = soup.find_all('img', class_='hidden-600')
                for item in items:
                    imgurl = ('https://chebistok.ru/' + item.find('img').get('src'))
                    img = requests.get(imgurl).content
                    builder.insert_image(img)
                    builder.writeln('')
            except:
                print("Ошибка с ActionCI")

        def ActionAW():
            try:
                font.bold = True
                font.size = 16
                paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                builder.writeln('Акции "Артезианская вода"')
                builder.writeln('')
                font.size = 14
                url = 'https://artvod.ru/product-category/akzii/'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                items = soup.find_all('div', class_="vitrina product-data-item")
                for item in items:
                    title = item.find('div').get_text(strip=True)
                    imgurl = ('https://artvod.ru' + item.find('img').get('src'))
                    img = requests.get(imgurl).content
                    font.bold = True
                    paragraphFormat.first_line_indent = 0
                    paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                    paragraphFormat.keep_together = True
                    builder.writeln(str(title))
                    builder.writeln('')
                    paragraphFormat.alignment = aw.ParagraphAlignment.CENTER
                    builder.insert_image(img)
                    builder.writeln('')
            except:
                print("Ошибка с ActionAW")
        try:
            ActionAW()
            ActionCI()
            ActionGO()
            ActionAM()
            ActionVK()
            ActionZK()
            ActionLV()
            ActionNI()
            doc.save("PARSER.docx")
        except:
            print("Ошибка с записями в ворд")