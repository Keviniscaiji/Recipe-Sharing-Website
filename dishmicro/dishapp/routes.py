import os
# from urllib import request

from flask import url_for, redirect, render_template, flash, session, Response, request, make_response
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash
from dishapp import app, db, form
from dishapp.config import Config
from dishapp.form import LoginForm, SignupForm, ProfileForm, PostForm, SearchForm
from dishapp.models import User, Profile, Post


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    # if user use the search function, the system will check whether the search form have been filled
    # prev_posts = Post.query.all()
    if form.validate_on_submit():

        if form.search.data:
            session.pop("ORDER", None)
            session["TITLE"] = form.criteria.data
        elif form.filter.data:
            session.pop("TITLE", None)
            session['ORDER'] = form.order.data
        return redirect(url_for('index'))
    # use filter the sift the dishes that meet user's requirement
    # This search bar is used to arrange recipes in a certain order
    if not session.get("ORDER") is None:
        o = session.get("ORDER")
        flash("the dish now is ordered by "+o)
        
        if(o == 'From old to new'):
            prev_posts = Post.query.order_by(Post.timestamp).all()
        elif(o == 'From new to old'):
            prev_posts = Post.query.order_by(Post.timestamp.desc()).all()
        elif(o == 'First letter A-Z'):
            prev_posts = Post.query.order_by(Post.title).all()
        else:
            prev_posts = Post.query.order_by(Post.title.desc()).all()
    elif not session.get("TITLE") is None:
        # Fuzzy Search Words
        t = session.get("TITLE")
        prev_posts = db.session.query(Post).filter(Post.title.like('%{0}%'.format(t))).all()
    else:
        prev_posts = Post.query.all()
    if not session.get("USERNAME") is None:
        user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
        stored_profile = Profile.query.filter(Profile.user == user_in_db).first()
        return render_template("index.html", title="Index", form=form, prev_posts=prev_posts, profile=stored_profile)
    return render_template("index.html", title="Index", form=form, prev_posts=prev_posts)


# code is from week 7 page 31 and made several changes
# for user to login the page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # for users who have already login the page, it will move to user directly to the profile page
    if not session.get("USERNAME") is None:
        flash("You have already login")
        return redirect(url_for('profile'))
    else:
        #  if the user fill a the form required but his account is not in the data base, it will return to login page
        if form.validate_on_submit():
            user_in_db = User.query.filter(User.username == form.username.data).first()
            if not user_in_db:
                flash('No user found with username: {}'.format(form.username.data))
                return redirect(url_for('login'))
            else:
                # If the user's is in database, the session USERNAME will be updated so the system will know the user
                # have logged in
                check_password_hash(user_in_db.password_hash, form.password.data)
                flash('Login success!')
                session["USERNAME"] = user_in_db.username
                user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
                if Profile.query.filter(Profile.user == user_in_db).first():
                    stored_profile = Profile.query.filter(Profile.user == user_in_db).first()
                    if stored_profile.avatar:
                        # if the user have set his own avatar, the session AVATAR will also updated too
                        session["AVATAR"] = stored_profile.avatar
                    else:
                        session["AVATAR"] = None
                else:
                    session["AVATAR"] = None
                return redirect(url_for('profile'))
    return render_template("login.html", title="Sign in", form=form)


# code is from week 7 page 31
# for new user to sign up
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash('PassWords do not match')
            return redirect(url_for('signup'))
        # transform the password to hash code to secure safety
        passw_hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=passw_hash)
        db.session.add(user)
        db.session.commit()
        flash('User registered with username:{}'.format(form.username.data))
        return redirect(url_for('profile'))
    return render_template('signup.html', title='Register a new user', form=form)


# use some ideas form week8 page17
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if not session.get("USERNAME") is None:
        if form.validate_on_submit():
            if not form.avatar.data is None:
                # save the picture of user who upload a file and store the file with name of username
                cv_dir = Config.Avatar_UPLOAD_DIR
                img = form.avatar.data
                filename = img.filename
                new_filename = session.get("USERNAME") + "." + filename.rsplit('.')[-1]
                img.save(os.path.join(cv_dir, new_filename))
                path = 'uploaded_Avatar/' + new_filename
                flash('CV uploaded and saved')
            user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
            stored_profile = Profile.query.filter(Profile.user == user_in_db).first()
            # Check whether the data is available for upload and this is for user who have not registered
            if not stored_profile:
                if not form.country.data is None and form.avatar.data is None:
                    profile = Profile(dob=form.dob.data, gender=form.gender.data, country=form.country.data,
                                      user=user_in_db)
                    db.session.add(profile)
                elif not form.country.data is None and not form.avatar.data is None:
                    profile = Profile(dob=form.dob.data, gender=form.gender.data, country=form.country.data,
                                      user=user_in_db,
                                      avatar=path)
                    # the AVATAR is used to store the path of image of the user
                    session["AVATAR"] = path
                    db.session.add(profile)
                elif form.country.data is None and not form.avatar.data is None:
                    profile = Profile(dob=form.dob.data, gender=form.gender.data, user=user_in_db,
                                      avatar=path)
                    session["AVATAR"] = path
                    db.session.add(profile)
                else:
                    profile = Profile(dob=form.dob.data, gender=form.gender.data, user=user_in_db)
                    db.session.add(profile)
            #         this is for user who have already registered and update his information
            else:
                stored_profile.dob = form.dob.data
                stored_profile.db = form.dob.data
                if not form.country.data is None:
                    stored_profile.country = form.country.data
                if not form.avatar.data is None:
                    stored_profile.avatar = path
                    session["AVATAR"] = path
            db.session.commit()
            return redirect(url_for('post'))
        #  the required form have been filled so back to the website and ask user to finish the form
        else:
            user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
            stored_profile = Profile.query.filter(Profile.user == user_in_db).first()
            if not stored_profile:
                return render_template('profile.html', title='Add your profile', form=form,user=user_in_db)
            else:
                form.dob.data = stored_profile.dob
                form.gender.data = stored_profile.gender
                return render_template('profile.html', title='Modify your profile', form=form, user=user_in_db)
    #  if the user who have not login and go into this page, the system will sent him back to the login page
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('login'))

# for each dish it have a separate page for it to show the detail of the dish and depend on its post id
@app.route('/index/<id>', methods=['GET'])
def dish_detail(id):
    id = id.strip("<>")
    dish = Post.query.filter_by(id=id).first()
    return render_template('dish_detail.html', title='Dish_detail', dish=dish, id=id)

# logout the account and pop the session
@app.route('/logout')
def logout():
    session.pop("USERNAME", None)
    session.pop("AVATAR", None)
    return redirect(url_for('login'))

# post the dishes if the user has not login, the system will turn the user back to login page
@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if not session.get("USERNAME") is None:
        if form.validate_on_submit():
            body = form.postbody.data
            title = form.posttitle.data
            user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
            post = Post(body=body, author=user_in_db, title=title)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('post'))
        else:
            user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
            prev_posts = Post.query.filter(Post.user_id == user_in_db.id).all()
            print("Checking for user: {} with id: {}".format(user_in_db.username, user_in_db.id))
            return render_template('post.html', title='User Posts', prev_posts=prev_posts, form=form)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('login'))
