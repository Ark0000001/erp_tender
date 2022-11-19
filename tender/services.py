import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):
    ua = UserAgent(verify_ssl=False)
    headers = {'User-Agent': ua.chrome}
    r = requests.get(url, headers=headers)
    r.encoding='utf-8'
    if r.ok:
        return r.text

def refine_ang(ang1):
    ang = str.upper(ang1)
    intab = 'А, В, С, Е, Н, К, М, О, Р, Т, Х'
    outtab = 'A, B, C, E, H, K, M, O, P, T, X'
    trantab = ang.maketrans(intab,outtab)
    return ang.translate(trantab)

def refine_p(p):
    return p.replace(' ','')

def write_csv(data):
    with open('modif/jm2.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    lis = soup.find_all('div', class_='inner_wrap TYPE_1')

    for li in lis:
        try:
            ang = li.find('div', class_='item-title').find('a').find('span').text.strip()
            name = refine_ang(ang)
        except:
            name = ''

        try:
            p = li.find('div', class_='price_value_block values_wrapper').find('span',
                                                                               class_='price_value').text.strip()
            price = refine_p(p)
        except:
            price = ''
        data = {'name': name,
                'price': price}

        write_csv(data)

def konec(url):

    soup = BeautifulSoup(get_html(url), 'lxml')
    url1 = soup.find('div', class_='nums').find_all('a', class_="dark_link")
    for elem in url1:
        e = []
        e.append(elem)
    print(e)
    k = str(e[-1])
    c = re.compile('\d+')
    print(int(c.findall(k)[-1]))
    return int(c.findall(k)[-1])+1

def main():

    pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/metallicheskie-shkafy/shkafy-metallicheskie-dlya-razdevalok/shkafy-dlya-razdevalok-praktik/?PAGEN_4={}'

    for i in range(1, konec(pattern)):
        url = pattern.format(str(i))
        print(url)
        get_page_data(get_html(url))

    pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/metallicheskie-shkafy/shkafy-metallicheskie-sumochnye/?PAGEN_4={}'

    for i in range(1, konec(pattern)):
        url = pattern.format(str(i))
        print(url)
        get_page_data(get_html(url))

    pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/metallicheskie-shkafy/shkafy-praktik/?PAGEN_4={}'

    for i in range(1, konec(pattern)):
        url = pattern.format(str(i))
        print(url)
        get_page_data(get_html(url))

    pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/metallicheskie-shkafy/metallicheskie-arkhivnye-shkafy/?PAGEN_4={}'

    for i in range(1, konec(pattern)):
        url = pattern.format(str(i))
        print(url)
        get_page_data(get_html(url))

    # pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/seyfy/?PAGEN_2={}'
    #
    # for i in range(1, konec(pattern)):
    #     url = pattern.format(str(i))
    #     print(url)
    #     get_page_data(get_html(url))


if __name__ == '__main__':
    main()