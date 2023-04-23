from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

def create_product_base():
    con = sqlite3.connect('./instance/product_base.db')
    cursor = con.cursor()
    cursor.execute('select * from product')
    return cursor.fetchall()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, intro, text):
        self.title = title
        self.intro = intro
        self.text = text

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post-detail.html', article=article)


@app.route('/posts/<int:id>/del')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return 'При удалении статьи произошла ошибка'


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            print(e)
            return 'При редактировании статьи произошла ошибка'
    else:
        return render_template('post_update.html', article=article)


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            print(e)
            return 'При добавлении статьи произошла ошибка'
    else:
        return render_template('create-article.html')

res_sum = [0, 0, 0, 0]
@app.route('/calc')
def calc():
    global res_sum
    res_sum = [0, 0, 0, 0]
    products_base = create_product_base()
    return render_template('calc.html', pb=products_base)


@app.route('/calc/<int:id>', methods=['POST', 'GET'])
def calc_product(id):
    products_base = create_product_base()
    res_weight = []
    if request.method == 'POST':
        weight = request.form['weight']
        try:
            for i in range(2, 6):
                res_weight.append(products_base[id][i] / 100 * int(weight))
            for i in range(4):
                res_sum[i] += res_weight[i]
        except ValueError:
            pass
    return render_template('calc_product.html', pb=products_base, pb_id=products_base[id], res_w=res_weight, res_s=res_sum)


if __name__ == '__main__':
    app.run(port=5000, debug=True)