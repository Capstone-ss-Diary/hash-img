# -*- coding: utf-8 -*-


from tfidf_kor import tfidfScorer

text = ['마지막 시험을 치는 날인데 시험 시간을 착각해서 일찍 일어나버렸다. 그리고 다시 잤다 ㅎㅎ 그런데 진짜 문제는 시험 치는 도중 생겼다. kt 인터넷 문제로 줌이 튕겨서 1/3정도가 줌이 나가졌다. 재시험을 칠까 하는 걱정과 부정행위 처리 되기 싫은 마음에 급하게 동영상을 찍으면서 시험을 쳤당. kt 반성해라']


for id, s in enumerate( tfidfScorer(text) ):
    s = sorted(s, key=lambda x:x[1], reverse=True)
    #print(type(s))
    #print(s[0][0], s[1][0], s[2][0])
    keyword = []
    for i in range(3):
        keyword.append('#'+s[i][0])
        #print(s[i][0])
    print('-original text-\n', text)
    print('top 3 keyword = ', keyword)
    #print('[%d] %s ...' % (id, s[:10]))