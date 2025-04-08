from flask import render_template, request, Blueprint, redirect, url_for
from flaskblog.models import Post

main=Blueprint('main', __name__)

sidebar_items = ['Latest Posts', 'Announcements', 'Calendars', 'etc']
 
@main.route("/")    
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/add_sidebar_item", methods=["POST"])
def add_sidebar_item():
    item = request.form.get("new_item")
    if item:
        sidebar_items.append(item)
    return redirect(url_for('main.home'))

@main.route("/remove_sidebar_item/<item>")
def remove_sidebar_item(item):
    if item in sidebar_items:
        sidebar_items.remove(item)
    return redirect(url_for('main.home'))