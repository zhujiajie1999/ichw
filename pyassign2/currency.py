#!/usr/bin/env python3

'''currency.py:实现按汇率计算的函数,可以通过输入的原货币类型、新货币类型、原货币数额，计算新货币的数额
(合法性测试：可以判断输入货币类型是否是列表中的类型，如果不是会报错并要求重新输入，直到输入有效的类型)

__author__ = "Zhujiajie"
__pkuid__  = "1800011794"
__email__  = "zhujiajie@pku.edu.cn"
'''

import json
from urllib.request import urlopen

def exchange():
    '''实现汇率计算的函数
    '''
    currency_from=input('Please enter source:  ')
    currency_to=input('Please enter target:  ')
    amount_from=input('Please enter amount:  ')
    currency_list=['AED','LKR','AFN','LRD','ALL','LSL','AMD','LTL','ANG','LVL','AOA','LYD','ARS','MAD','AUD',
                   'MDL','AWG','MGA','AZN','MKD','BAM','MMK','BBD','MNT','BDT','MOP','BGN','MRO','BHD','MTL',
                   'BIF','MUR','BMD','MVR','BND','MWK','BOB','MXN','BRL','MYR','BSD','MZN','BTC','NAD','BTN',
                   'NGN','BWP','NIO','BYR','NOK','BZD','NPR','CAD','NZD','CDF','OMR','CHF','PAB','CLF','PEN',
                   'CLP','PGK','CNY','PHP','COP','PKR','CRC','PLN','CUC','PYG','CUP','QAR','CVE','RON','CZK',
                   'RSD','DJF','RUB','DKK','RWF','DOP','SAR','DZD','SBD','EEK','SCR','EGP','SDG','ERN','SEK',
                   'ETB','SGD','EUR','SHP','FJD','SLL','FKP','SOS','GBP','SRD','GEL','STD','GGP','SVC','GHS',
                   'SYP','GIP','SZL','GMD','THB','GNF','TJS','GTQ','TMT','GYD','TND','HKD','TOP','HNL','TRY',
                   'HRK','TTD','HTG','TWD','HUF','TZS','IDR','UAH','ILS','UGX','IMP','USD','INR','UYU','IQD',
                   'UZS','IRR','VEF','ISK','VND','JEP','VUV','JMD','WST','JOD','XAF','JPY','XAG','KES','XAU',
                   'KGS','XCD','KHR','XDR','KMF','XOF','KPW','XPD','KRW','XPF','KWD','XPT','KYD','YER','KZT',
                   'ZAR','LAK','ZMK','LBP','ZMW','LKR','ZWL']
    while currency_from not in currency_list:
        print('Please enter a valid source')
        currency_from=input('please enter source:  ')
    while currency_to not in currency_list:
        print('Please enter a valid target')
        currency_to=input('please enter target:  ')    
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr= docstr.decode('ascii')
    jstr.replace('true','True')
    pdict=json.loads(jstr)
    kstr=pdict.get('to')
    print('You will get',kstr,'.')
    
#以下为测试函数
#通过几组输入，比较输出与理论值是否相同，以初步检查函数的正确性

def get_exchange(currency_from,currency_to,amount_from):
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr= docstr.decode('ascii')
    jstr.replace('true','True')
    pdict=json.loads(jstr)
    kstr=pdict.get('to')
    return(kstr)
    
def test_USD_AUD_32():
    a= get_exchange('USD','AUD','32')
    assert(a=='44.572096 Australian Dollars')
def test_USD_AUD_64():
    a= get_exchange('USD','AUD','64')
    assert(a=='89.144192 Australian Dollars')
def test_USD_EUR_50():
    a= get_exchange('USD','EUR','50')
    assert(a=='43.17845 Euros')
def test_JPY_EUR_200():
    a= get_exchange('JPY','EUR','200.5')
    assert(a=='1.5542831129543 Euros')
    
def testAll():
    '''检查函数正确性的测试函数
    '''
    test_USD_AUD_32()
    test_USD_AUD_64()
    test_USD_EUR_50()
    test_JPY_EUR_200()
    print("All tests passed.")

def main():
    """main module
    """
    exchange()
    testAll()
if __name__ == '__main__':
    main()