#Assign4
#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhujiajie"
__pkuid__  = "1800011794"
__email__  = "zhujiajie@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(urls,topn=10):
    """Count words from lines of text string, 
       then sort by their counts in reverse order, 
       output the topn word, each in one line. 
       Results may differ from the sample for a bit,
       as punctuations such as hyphen and possessive cases 
       are not handled in the same way.
    """
    infile = urlopen(urls)
    aline = infile.readline().lower()
    dict_1={97:'a',98:'b',99:'c',100:'d',101:'e',102:'f',103:'g',104:'h',105:'i',
        106:'j',107: 'k',108:'l',109:'m',110:'n',111:'o',112:'p',113:'q',114:'r',
        115:'s',116:'t',117:'u',118:'v',119:'w',120:'x',121:'y',122:'z',32:' '}
    counts={}
    while aline:
        s=''
        for i in aline:
            if i in range(97,123) or i==32:
                s+=(dict_1.get(i))
        items =s.split()
        for words in items:
            counts[words] = counts.get(words, 0)+1
        aline = infile.readline().lower()
    list_1=[]
    for k,v in counts.items():
        list_1.append((k,v))
    list_1.sort(key=lambda x:x[1],reverse=True)
    if topn<=len(list_1):
        for tuples in list_1[0:topn]:
            print('{0:<15}{1}'.format(tuples[0],str(tuples[1])))
    else:
        for tuples in list_1:
            print('{0:<15}{1}'.format(tuples[0],str(tuples[1])))
    infile.close()

if __name__ == '__main__':
    '''Main function contains error examing procedures:
       While entering topn with non-int type,
       output 'invalid topn';
       while entering url which cannot lead to correct website,
       output 'invalid url'.
    '''
    
    if len(sys.argv)==1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
        
    if len(sys.argv)==2:
        try:
            wcount(sys.argv[1])
        except Exception:
            print('invalid url')
        
    if len(sys.argv)==3:
        try:
            topn_1=int(sys.argv[2])
            wcount(sys.argv[1],topn_1)
        except ValueError:
            print('invalid topn')
        except Exception:
            print('invalid url')
