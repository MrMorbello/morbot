import requests

class Servicios:
    def __init__(self):
        self.url = ''

    def precio_del_dolar(self):
        url = 'https://dolarhoy.com/i/cotizaciones/dolar-blue'
        t = requests.get(url).text
        i = f = t.find('<span>Compra</span>')
        while t[i] != '>':
            i -= 1
        return float(t[i+1:f])

    def precio_del_pase_fortnite(self):
        url = 'https://www.xbox.com/es-ar/games/store/a14fe89a-b37a-462c-a9c1-692dfaa9206c/cfq7ttc0l23l?ranMID=46131&ranEAID=vL14T8U*qP4&ranSiteID=vL14T8U.qP4-5cVGTZm3veSayMaAAvuVfw&epi=vL14T8U.qP4-5cVGTZm3veSayMaAAvuVfw&irgwc=1&OCID=AIDcmm549zy227_aff_7806_1243925&tduid=%28ir__jc0hntrjgwkfbgvhnloxmsrqjn2xfxrhvfdkwwyt00%29%287806%29%281243925%29%28vL14T8U.qP4-5cVGTZm3veSayMaAAvuVfw%29%28%29&irclickid=_jc0hntrjgwkfbgvhnloxmsrqjn2xfxrhvfdkwwyt00'
        t = requests.get(url).text
        i = f = t.find("ARS$")+5
        while t[f] != ',':
            f += 1
        return float(t[i:f])
    
# print(Servicios().precio_del_pase_fortnite())