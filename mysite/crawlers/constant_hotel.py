from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


def crawler():
    driver = webdriver.Chrome(executable_path='/home/akmal/Desktop/crawler/webScraping_hotel.com/mysite/'
                                              'crawlers/chromedriver.exe')
    driver.get('https://www.hotels.com/search.do?destination-id=1642097&q-check-in=2021-11-25&q-check-out=2021-11-26&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER')
    print(driver.title)
    import pdb; pdb.set_trace()
    block_data = driver.find_elements_by_css_selector('div.-RcIiD')
    print(block_data)

    hotel_list = []
    for z in block_data:
        row_data = []
        try:
            hotel_title = z.find_element_by_css_selector('h2._3zH0kn').text
            if hotel_title == '':
                hotel_title = "N/A"
            print(hotel_title)
        except:
            hotel_title = "N/A"
        try:
            address = z.find_element_by_css_selector('p._2oHhXM').text
            if address == '':
                address = "N/A"
            print(address)
        except:
            address = "N/A"
        try:
            place_title = z.find_element_by_css_selector('p._2LH_yj').text
            if place_title == '':
                place_title = "N/A"
            print(place_title)
        except:
            place_title = "N/A"
        try:
            rang_title = z.find_element_by_css_selector('ul._2sHYiJ._3JLCGC').text
            if rang_title == '':
                rang_title = "N/A"
            print(rang_title)
        except:
            rang_title = "N/A"
        try:
            reating = z.find_element_by_css_selector('span._1biq31').text
            if reating == "":
                reating = "N/A"
            print(reating)
        except:
            reating = "N/A"
        try:
            status = z.find_element_by_css_selector('span._3XN8b8').text
            if status == "":
                status = "N/A"
            print(status)
        except:
            status = "N/A"
        try:
            parking = z.find_element_by_css_selector('ul._1CyeN6').text
            parking_detail = parking.replace("\ue940\n", " ")
            parking_detail = parking_detail.replace("\ue950\n", " ")
            parking_detail = parking_detail.replace("\ue935\n", " ")
            parking_detail = parking_detail.replace("\ue95b\n", " ")
            parking_detail = parking_detail.replace("\ue9b2\n", " ")
            parking_detail = parking_detail.replace("\ue90a\n", " ")
            parking_detail = parking_detail.replace("\ue949\n", " ")
            parking_detail = parking_detail.replace("\ue945\n", " ")
            parking_detail = parking_detail.replace("\ue92f\n", " ")
            parking_detail = parking_detail.replace("\ue933\n", " ")
            parking_detail = parking_detail.replace("\ue93e\n", " ")
            parking_detail = parking_detail.replace("\ue93f\n", " ")
            print(parking_detail)

            if parking_detail == "":
                parking_detail = "N/A"
            print(parking_detail)
        except:
            parking_detail = "N/A"
        try:
            price = z.find_element_by_css_selector("span._2R4dw5").text
            if price == "":
                price = "N/A"
            print(price)
        except:
            price = "N/A"
        if len(hotel_title) > 0:
            row_data.append(hotel_title)
        if len(address) > 0:
            row_data.append(address)
        if len(place_title) > 0:
            row_data.append(place_title)
        if len(rang_title) > 0:
            row_data.append(rang_title)
        if len(reating) > 0:
            row_data.append(reating)
        if len(status) > 0:
            row_data.append(status)
        if len(parking_detail) > 0:
            row_data.append(parking_detail)
        if len(price) > 0:
            row_data.append(price)
        print(row_data)
        hotel_list.append(row_data)
        print(hotel_list)
    header = ['hotel_title', 'address', 'placeTitle','rang_title','reating','status','parking','price']
    with open('Abbotabad.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        # write the data
        for j in hotel_list:
            writer.writerow(j)

    driver.quit()