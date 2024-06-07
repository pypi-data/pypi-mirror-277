# IndonesiaLatestEarthQuake
This package will get information about latest earthquake from BMKG(Indonesian Agency for Meteorological, Climatological and Geophysics)

## How It Works
This package will scrap data from [BMKG](https://www.bmkg.go.id/) to get information about latest earthquake on indonesia

This package used BeautifulSoup4 and Requests to generate JSON output that'll be used for web or mobile apps

## How to Run
```
import gempaTerkini

if __name__ == '__main__':
    print('Aplikasi utama')

    id_earthquake = GempaTerkini('https://www.bmkg.go.id/')
    id_earthquake.show_description()
    id_earthquake.run()
```

# Author
Muhammad Dwi Reza