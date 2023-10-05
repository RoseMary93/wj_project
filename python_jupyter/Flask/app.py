from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators, ValidationError
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms.validators import DataRequired 
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import re
from flask import jsonify
# from urllib.parse import quote

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  

def validate_first_char(form, field):
    # if field.data.startswith('/'):
    #     raise validators.ValidationError('第一個字符不能是特殊字符 "/"')
    if re.match(r'^/', field.data):
        raise ValidationError('第一個字不能是特殊符號 "/"')

def check_data(item):
    if str(item)[0]=="/":
        return False
    else:
        return True

class User(UserMixin, db.Model):
    __tablename__ = "useraccount"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    def get_id(self):
        return str(self.id)

class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) 
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    a_title = db.Column(db.String(80), unique=False, nullable=False)
    contents = db.Column(db.String(2000), unique=False, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    edit_timestamp = db.Column(db.DateTime, nullable=True)

class Article_form(FlaskForm):
    a_title = StringField('Title', validators=[DataRequired(), validate_first_char]) 
    contents = TextAreaField('Contents', validators=[DataRequired()]) 
    submit = SubmitField('Submit')

class EditArticleForm(FlaskForm):
    a_title = StringField('Title', validators=[DataRequired(), validate_first_char])
    contents = TextAreaField('Contents', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    db.create_all()
    form = MyForm()
    title = "Register"
    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template("registersuss.html")
        except:
            return 'Register failed. Please check your data.'
    return render_template('register.html', form=form, title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db.create_all()
    form = MyForm()
    title = "Login"
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Login failed. Please check your credentials.'
    return render_template('register.html', form=form, title=title)

@app.route('/homepage')
def homepage():
    new_articles = Article.query.all()
    new_articles = new_articles[::-1]
    new_articles = new_articles[:10]
    return render_template("homepage.html", new_articles=new_articles)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard2.html")

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/article', methods=['GET', 'POST'])
@login_required
def article():
    db.create_all()
    form = Article_form()
    title = "Article"
    if form.validate_on_submit():
        try:
            a_title = form.a_title.data
            contents = form.contents.data
            html_contents = contents.replace("\n", "<br>")
            author = current_user.username
            if check_data(a_title)==False:
                return "標題開頭不能是/，請按上一頁修改"
            new_article = Article(a_title=a_title, contents=contents, author=author)
            db.session.add(new_article)
            db.session.commit()
            return render_template("person_art.html", a_title=a_title, contents=contents, html_contents=html_contents)
        except:
            return 'Submit failed. Please check your data.'
    return render_template('article2.html', form=form, title=title)


@app.route('/my_articles')
@login_required
def my_articles():
    articles = Article.query.filter_by(author=current_user.username).all()
    return render_template('my_articles.html', articles=articles)

# @app.route('/search')
# @login_required
# def search():
#     return render_template('search.html')

@app.route('/search_user', methods=['POST'])
@login_required
def search_user():
    search = request.form.get('user_input')
    print(f'您輸入的文字是：{search}')
    return redirect('/user_articles/'+str(search))

@app.route('/search_articles', methods=['POST'])
def search_articles():
    search_keyword = request.form.get('search_keyword')
    # 使用 ilike 進行不區分大小寫的模糊搜索
    articles = Article.query.filter(Article.a_title.ilike(f'%{search_keyword}%')).all()
    return render_template('search_article_result.html', articles=articles)

@app.route('/user_articles/<username>')
@login_required
def user_articles(username):
    search_user = User.query.filter_by(username=username).first()
    if search_user:
        articles = Article.query.filter_by(author=username).all()
        return render_template('user_articles.html', articles=articles, username=username)
    else:
        return 'User not found.'
    
@app.route('/user_articles/<username>/<path:a_title>')
@login_required
def each_article(username, a_title):
    search_article = Article.query.filter_by(author=username, a_title=a_title).first()
    if search_article:
        html_contents = search_article.contents.replace("\n", "<br>")
        return render_template('article_tem.html', author=username, article=search_article, html_contents=html_contents)
    else:
        return 'Article not found.'

@app.route('/edit_articles/<username>/<a_title>', methods=['GET', 'POST'])
@login_required
def edit_articles(username, a_title):
    article = Article.query.filter_by(author=username, a_title=a_title).first()
    if not article:
        return redirect(url_for('each_article', username=username, a_title=a_title))
    if current_user.username != username:
        return redirect(url_for('each_article', username=username, a_title=a_title))
    form = EditArticleForm()
    if form.validate_on_submit():
        # 更新文章的內容
        article.a_title = form.a_title.data
        article.contents = form.contents.data
        article.edit_timestamp = datetime.utcnow()
        db.session.commit()   # 保存到 PostgreSQL 數據庫
        return redirect(url_for('my_articles'))
    # 將文章內容填充到表單中，以便進行編輯
    form.a_title.data = article.a_title
    form.contents.data = article.contents
    return render_template('edit_articles.html', form=form, article=article)

@app.route('/delete_article/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    article = Article.query.get(article_id)
    if article:
        if current_user.username == article.author:
            db.session.delete(article)
            db.session.commit()
            flash('文章已刪除', 'success')
        else:
            flash('你無權刪除這篇文章', 'danger')
    else:
        flash('文章不存在', 'danger')
    
    return redirect(url_for('my_articles'))


admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Article, db.session))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9393, debug=True)