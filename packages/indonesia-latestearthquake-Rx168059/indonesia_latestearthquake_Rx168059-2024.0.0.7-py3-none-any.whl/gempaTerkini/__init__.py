import requests
from bs4 import BeautifulSoup


class BencanaTerkini:
    def __init__(self, url, description):
        self.description = description
        self.data_result = None
        self.link = url

    def show_description(self):
        print(f'description: {self.description}')

    def scrap_data(self):
        pass

    def show_data(self):
        pass

    def run(self):
        self.scrap_data()
        self.show_data()


class RecentTsunami(BencanaTerkini):
    def __init__(self, url):
        super().__init__(url, 'Not but this should return recent tsunami in indonesia')

    def show_description(self):
        print(f'Under Construction: {self.description}'.upper())


class GempaTerkini(BencanaTerkini):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url, 'Getting Information about latest earthquake from BMKG Indonesia')

    def scrap_data(self):
        """
        dateTime: date: 31 Mei 2024, time: 05:54:38 WIB
        magnitude: 5.4
        kedalaman: 88 km
        location: LS: 1.48, BT: 134.01
        pusat: 139 km BaratLaut PULAUKARATUNG-SULUT
        keterangan: tidak berpotensi TSUNAMI
        :return:
        """

        # catch error
        try:
            # get url
            content = requests.get(self.link)
        except Exception as e:
            print(e)
            return None

        if content.status_code == 200:

            # create BeautifulSoup object
            soup = BeautifulSoup(content.text, 'html.parser')

            # find span tag
            result_span = soup.find('span', {'class': 'waktu'})
            date = result_span.text.split(', ')[0]
            time = result_span.text.split(', ')[1]

            # find list tag in div tag
            result_div = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            li = result_div.findChildren('li')

            result_list = []

            # substain result_list value
            for i in range(len(li)):
                result_list.append(li[i].text)

            # remove not used value
            result_list.pop()

            # var
            magnitude = ''
            kedalaman = ''
            location = ''
            pusat = ''
            keterangan = ''

            # substain value to var
            i = 1
            while i < len(result_list):
                magnitude = result_list[i]
                i += 1
                kedalaman = result_list[i]
                i += 1
                location = result_list[i]
                i += 1
                pusat = result_list[i]
                i += 1
                keterangan = result_list[i]
                i += 1

            data_result = {
                'dateTime': {'date': date, 'time': time},
                'magnitude': magnitude,
                'kedalaman': kedalaman,
                'location': location,
                'pusat': pusat,
                'keterangan': keterangan,
            }
            self.data_result = data_result
        else:
            return None

    def show_data(self):
        # error output
        if self.data_result is None:
            print('data tidak ditemukan')
            return
        else:
            # print(f'Date = {datas['dateTime']['date']}')
            # print(f'Time = {datas['dateTime']['time']}')
            # print(f'Magnitude = {datas['magnitude']}')
            # print(f'kedalaman = {datas['kedalaman']}')
            # print(f'location = {datas['location']}')
            # print(f'pusat = {datas['pusat']}')
            # print(f'keterangan = {datas['keterangan']}')
            for data in self.data_result:
                if data == 'dateTime':
                    for date in self.data_result[data]:
                        print(f'{date}: {self.data_result[data][date]}')
                print(f'{data}: {self.data_result[data]}')


if __name__ == '__main__':
    print('Aplikasi utama')

    id_earthquake = GempaTerkini('https://www.bmkg.go.id/')
    id_earthquake.show_description()
    id_earthquake.run()

    print('\n')

    id_Tsunami = RecentTsunami('https://www.bmkg.go.id/')
    id_Tsunami.show_description()
    id_Tsunami.run()
