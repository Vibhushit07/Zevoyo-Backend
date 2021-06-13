# Zevoyo Hotel Booking System

<h2 align="center" id="content">🗂 Content</h2>

> :pushpin: [Objective](#objective) <br>
> :pushpin: [Tech Stack](#tech-stack) <br>
> :pushpin: [Features](#features) <br>
> :pushpin: [Screenshots](#screenshots)  <br>
> :pushpin: [Installation](#installation) <br>

<br>

<h2 align="center" id="objective">🏷️ Objective</h2>

User Experience (UX) plays a key role in helping visitors use, understand and stay on the website. Creating obvious, logical navigation with clear hierarchy and using consistent layouts and visual cues for functionality across the site.

The website should work quickly, correctly and as expected. Build to web standards, proofread rigorously and test regularly for problems with speed or functionality. Pages should always be fast and functional.

The website will provide numerous functionalities for the user to increase the productivity of the website, like email confirmations on account creation, user profile updation, booking confirmation and booking cancellation.

Chat Support System will provide the user to converse with the admin in a real time environment.

<p align="center"> <i> <a href="#content"> ⬆️ Back To Content </a> <i> </p>

<br>

<h2 align="center" id="tech-stack">🏷️ Tech Stack</h2>

<h3>

```diff
- Python -
- SQlite -
```
</h3>

<p align="center"> <i> <a href="#content"> ⬆️ Back To Content </a> <i> </p>

<br>

<h2 align="center" id="features">🏷️ Features</h2>

<h3>

```diff
- Email Confirmartion -
- Chat App Support -
```
</h3>

<p align="center"> <i> <a href="#content"> ⬆️ Back To Content </a> <i> </p>

<br>

<h2 align="center" id="screenshots">🏷️ Screenshots</h2>

<h3>Home Page</h3>

![homepage](https://user-images.githubusercontent.com/41487076/121527008-94890b80-ca17-11eb-8115-aea45707b463.png)

<h3>Dashboard</h3>

![dashboard](https://user-images.githubusercontent.com/41487076/121527001-9357de80-ca17-11eb-83b6-beb4b0bf70f1.png)

<h3>User Chat</h3>

![user-chat](https://user-images.githubusercontent.com/41487076/121527011-95ba3880-ca17-11eb-9ac7-affd9c8fe220.png)

<h3>Admin Chat</h3>

![admin-chat](https://user-images.githubusercontent.com/41487076/121527000-92bf4800-ca17-11eb-9835-d19b386689f7.png)

<p align="center"> <i> <a href="#content"> ⬆️ Back To Content </a> <i> </p>

<br>

<h2 align="center" id="installation">🏷️ Installation </h2>

```diff
+ Commands to run django server
```

- <a href = "https://phoenixnap.com/kb/how-to-install-python-3-windows"> Install Python </a>
- Run following commands

```diff

 - git clone https://github.com/Vibhushit07/Zevoyo-Backend.git
 - cd zevoyo-backend
 - python --version
 - python -m pip install -U pip
 - pip install virtualenv
 - virtualenv venv
 - venv\Scripts\activate
 - python -m pip install django
 - pip install -r requirements.txt
 - cd zevoyo
 - python manage.py makemigrations myApp
 - python manage.py makemigrations chat
 - python manage.py migrate
 - python manage.py createsuperuser
```

```diff
 - Enter username, email and password for user as shown in image below-
```

![admin](https://user-images.githubusercontent.com/41487076/121818381-7e43af80-cca4-11eb-91bc-ec5bc752d53c.PNG)

```diff
+ Settings for Sending Emails in django
```

```diff
 - Open "settings.py"
 - Under EMAIL_HOST_USER provide your gmail account
 - Under EMAIL_HOST_PASSWORD provide your gmail account password as shown in image below-
```

![email-configuration](https://user-images.githubusercontent.com/41487076/121800124-a6ec8a80-cc4d-11eb-8adb-f768eef798ad.png)

```diff
+ Setting up Gmail for Django Mail API
```

We need to make some changes in our Gmail account to send an Email. Visit this link with your account signed in:

<a href="https://myaccount.google.com/security" style="color:blue">

```diff

- Gmail Account Settings

```
</a>


The link contains a specific setting that allows access via Django mail API. Since our web application is not a google registered service, it is a less secured app. Therefore, we allow less secured apps to our settings.

Then scroll down to this section of the page.

![mail-api](https://user-images.githubusercontent.com/41487076/121819875-2c535780-ccad-11eb-9376-bdd1182fd29b.PNG)

Less secure app access option will be present. Turn on the access.

<h4>Note:</h4>

```diff

If you are just testing, then you can temporarily do this setting. For a permanent setup, I would recommend a new account. 
Since, using your main account will be risky.

```

Now, we are ready to send emails with Django.

- Run following command-
```diff
 - python manage.py runserver
```

- In browser open http://127.0.0.1:8000/myApp/ to run the application.
- For staff login enter the superuser credentials.
- Now you are ready to go.

<p align="center"> <i> <a href="#content"> ⬆️ Back To Content </a> <i> </p>

<br>

## Contributors:
### Credit goes to these wonderful people: ✨

<table>
	<tr>
		<td>
            <a href="https://github.com/vibhushit07/zevoyo-backend/graphs/contributors">
                <img src="https://contrib.rocks/image?repo=vibhushit07/zevoyo-backend" />
            </a>
		</td>
	</tr>
</table>