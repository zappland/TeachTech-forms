```
  _____                _    _____          _            __
 /__   \___  __ _  ___| |__/__   \___  ___| |__        / _| ___  _ __ _ __ ___  ___
   / /\/ _ \/ _` |/ __| '_ \ / /\/ _ \/ __| '_ \ _____| |_ / _ \| '__| '_ ` _ \/ __|
  / / |  __/ (_| | (__| | | / / |  __/ (__| | | |_____|  _| (_) | |  | | | | | \__ \
  \/   \___|\__,_|\___|_| |_\/   \___|\___|_| |_|     |_|  \___/|_|  |_| |_| |_|___/

```
### About
Certification form using django framework. Upload certification information to database.


### Dependencies:
- Python3 [Download Link](https://www.python.org/getit/)


### Install Steps:
- Clone this repo to your project directory
```
git clone https://github.com/zappland/TeachTech-forms.git
```
- create virtual environment in project directory and activate
```
python3 -m venv venv

source venv/bin/activate
```
- Install packages
```
pip install -r requirements.txt
```

- Create the database
```
python manage.py makemigrations
python mananage.py migrate
```

- Run
```
python manage.py runserver
```



### Fields

- Last Name
- First Name
- SS#
- Returning or New Hire
- Title / Position
- Current  Assignment             
- subject(s) and grade(s)
- Certification Status
- NYS Cert. Area
- Cert.Type
- Expiration  date
- CURRENT Comments and Interpretive Notes
- Comments and Interpretive Notes from Last Wksht
- LAST
- ATS-W 
- CST
- CST Subject(s)
- EAS
- ATAS



