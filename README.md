# My_Blog

<p align="center">
  <img src="https://github.com/sanjuGoudru/My_Blog/blob/master/BlogPost_logo.png" >
</p>

## Quickstart
First set the following environment variables

<ul>
  <li><i>MY_FLASK_SECRET_KEY</i>: (secret key)</li>
  <li><i>MY_FLASK_SQLALCHEMY_DATABASE_URI</i>: (For sqlite use "sqlite:///site.db")</li>
  <li><i>EMAIL_USER</i>: (Gmail id for sending mails to reset password. Make sure you enable less secure apps in Gmail Settings)</li>
  <li><i>EMAIL_PASSWORD</i>: (Gmail password)</li>
</ul>

</br></br>
Then run the following command in command line
```bash
git clone https://github.com/sanjuGoudru/My_Blog.git
cd My_Blog
pip install -r requirements.txt
```
</br></br>
Then run the following command in command line
```bash
python run.py
```

## Structure

<ul>
  <li><b>main</b></li>
  <p>handles the HOME and ABOUT page</p>
  <li><b>users</b></li>
  <p>handles the register, login, logout, account, user password reset and displaying specific user posts.</p>
  <li><b>posts</b></li>
  <p>handles creating, displaying, updated and deleted posts.</p>
  <li><b>errors</b></li>
  <p>handles the errors 403,404 and 500</p>

</ul>

## Deployment
I have done deployment on Heroku cloud (free version). But one can deploy on any cloud. All the required packages are mentioned in 'requirements.txt' file.

## Acknowledgment
Idea for this flask project goes to youtuber [Corey Schafer](https://www.youtube.com/user/schafer5) who has helped people like me and many others for learning python and other python related packages. 
