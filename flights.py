# -*- coding:utf-8 -*-


class City:
    def __init__(self, name_abbr, name_en, name_zh):
        self.name_abbr = name_abbr
        self.name_en = name_en
        self.name_zh = name_zh

    def __str__(self):
        return '%s [%s %s]' % (self.name_abbr, self.name_en.ljust(16), self.name_zh.ljust(16))
    def __repr__(self):
        return self.__str__()

class Region:
    def __init__(self, region, region_code):
        self.region = region
        self.region_code = region_code


class Ticket:
    def __init__(self, dep_city=None, arr_city=None, dep_date=None, ret_date=None, min_price=None, money=None, seg_type=None, region=None):
        self.dep_city = dep_city
        self.arr_city = arr_city
        self.dep_date = dep_date
        self.ret_date = ret_date
        self.min_price = min_price
        self.money = money
        self.seg_type = seg_type
        self.region = region


class Airport:
    def __init__(self, **kwargs):
        class _flight:
            def __init__(self, **kwargs):
                self.arr_city = City(
                        kwargs.get('ARRCITY', ''),
                        kwargs.get('ARRCTIYNAME_EN', ''),
                        kwargs.get('ARRCTIYNAME_ZH', '')
                )
                self.dep_date = kwargs.get('DEPDATE', '')
                self.ret_date = kwargs.get('RETURNDATE', '')
                self.money = kwargs.get('money', '')
                self.min_price = kwargs.get('MINPRICE', '')
                self.seg_type = kwargs.get('SEGTYPE', '')

            def __str__(self):
                return '%s: <%s, %s>, %s%s' % (self.arr_city, self.dep_date, self.ret_date, self.min_price, self.money)

        self.city = City(
            kwargs.get('DEPCITY', ''),
            kwargs.get('DEPCTIYNAME_EN', ''),
            kwargs.get('DEPCTIYNAME_ZH', '')
        )
        self.region = Region(
            kwargs.get('REGION', ''),
            kwargs.get('REGION_CODE', '')
        )

        self.flights = []
        for f in kwargs.get('FLIGHT', ''):
            #print(f)
            if isinstance(f, dict):
                temp = _flight(**f)
                self.flights.append(temp)
        print('Airport: %s:' % self.city)
        [print('\t--->', x) for x in self.flights]
