from wordcloud import WordCloud
from konlpy.tag import Twitter
from collections import Counter

# 텍스트 파일 경로를 정확하게 지정
text = open('C:/Users/dodadak/Desktop/glucoach/똑같은 날.txt', encoding='utf8').read()

# Twitter 객체 생성
twitter = Twitter()

# 형태소 분석
sentences_tag = twitter.pos(text)

# 명사와 형용사만 추출
noun_adj_list = []
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)

# 가장 많이 나온 단어부터 40개 추출
counts = Counter(noun_adj_list)
tags = counts.most_common(40)

# WordCloud를 생성 (한글 폰트 경로를 윈도우에 맞게 수정)
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', background_color="white", max_font_size=60)

# WordCloud 생성
cloud = wc.generate_from_frequencies(dict(tags))

# 생성된 WordCloud를 이미지 파일로 저장
cloud.to_file('test.jpg')
