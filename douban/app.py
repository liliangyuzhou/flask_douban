from flask import Flask,render_template,request

app = Flask(__name__)
movies = [
    {
        'id': '11211',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2499793218.webp',
        'title': u'王牌特工2',
        'rating': u'7.3',
        'comment_count': 12000,
        'authors': u'科林·费尔斯 / 塔伦·埃格顿 / 朱丽安·摩尔'
    },
    {
        'id': '34532',
        'title': u'羞羞的铁拳',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2499793218.webp',
        'rating': u'7.6',
        'comment_count': 39450,
        'authors': u'艾伦/马丽/沈腾'
    },
    {
        'id': '394558',
        'title': u'情圣',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2499793218.webp',
        'rating': u'6.3',
        'comment_count': 38409,
        'authors': u'肖央 / 闫妮 / 小沈阳'
    },
    {
        'id': '9384089',
        'title': u'全球风暴',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2499793218.webp',
        'rating': u'7.4',
        'comment_count': 4555,
        'authors': u'杰拉德·巴特勒/吉姆·斯特'
    },
    {
        'id': '26921827',
        'title': u'大卫贝肯之倒霉特工熊',
        'thumbnail': u'https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p2408893200.jpg',
        'rating': u'4.3',
        'comment_count': 682,
        'authors': u'汤水雨 / 徐佳琪 / 杨默'
    },
    {
        'id': '26287884',
        'title': u'追龙',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2499793218.webp',
        'rating': u'7.5',
        'comment_count': 33060,
        'authors': u'查理兹·塞隆 / 阿特·帕金森 / 拉尔夫·费因斯'
    }
]

# 电视剧
tvs = [
    {
        'id': '235434',
        'title': u'鬼吹灯之精绝古城',
        'thumbnail': u'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2404604903.jpg',
        'rating': u'8.4',
        'comment_count': 49328,
        'authors': u'靳东 / 陈乔恩 / 赵达 / 付枚 / 金泽灏 /'
    },
    {
        'id': '9498327',
        'title': u'孤芳不自赏',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2407425119.jpg',
        'rating': u'3.7',
        'comment_count': 8493,
        'authors': u'钟汉良 / 杨颖 / 甘婷婷 / 孙艺洲 / 亓航 /'
    },
    {
        'id': '26685451',
        'title': u'全球风暴',
        'thumbnail': u'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2501769525.webp',
        'rating': u'8.2',
        'comment_count': 345,
        'authors': u' 卢克·崔德威 / 琼安·弗洛加特 / 露塔·格德米纳斯 / 安东尼·海德 / 卡罗琳·古多尔 /'
    },
    {
        'id': '235434',
        'title': u'其他人',
        'thumbnail': u'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2371503632.jpg',
        'rating': u'7.6',
        'comment_count': 25532,
        'authors': u'杰西·普莱蒙 / 莫莉·香侬 / 布莱德利·惠特福德 / Maude Apatow / 麦迪逊·贝蒂 /'
    },
    {
        'id': '48373095',
        'title': u'全员单恋',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2367986708.jpg',
        'rating': u'6.4',
        'comment_count': 2483,
        'authors': u'伊藤沙莉 / 中川大志 / 上原实矩 / 森绘梨佳 / 樱田通 /'
    },
    {
        'id': '292843',
        'title': u'废纸板拳击手',
        'thumbnail': u'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2380194237.jpg',
        'rating': u'8.2',
        'comment_count': 23456,
        'authors': u'托马斯·哈登·丘奇 / 泰伦斯·霍华德 / 波伊德·霍布鲁克 / 瑞斯·维克菲尔德 / 马尔洛·托马斯 /'
    }
]

@app.route('/')
def hello_world():
    context = {
        'movies': movies,
        'tvs': tvs
    }
    return render_template('index.html',**context)

@app.route('/list/')
def my_list():
    items=None
    category=int(request.args.get('category'))
    if category==1:
        items=movies
    else:
        items=tvs

    return render_template('list.html',items=items)


if __name__ == '__main__':
    app.run()
