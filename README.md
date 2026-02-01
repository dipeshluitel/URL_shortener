# URL Shortener


🔗 **Live Demo:** https://urlshortener-production-88de.up.railway.app

---

## 💡 About

URL Shortener lets you generate short link for your orginal link and lets you redirect to orginal link, it stores links independently for different users and let you keep track of creation and let you delete it as necessary
---

## 🛠️ Features

- **Converts long URLs into short, unique links using Base62 encoding**
- **Allows short links to be opened directly from any browser**
- **Redirects users to the original website seamlessly**
- **Tracks how many times each short link is visited**
- **Includes user authentication so links are user-specific**
- **Deployed using Gunicorn and Whitenoise**  

---

## 🧱 Tech Stack

This project uses:

| Purpose | Technology |
|---------|------------|
| Backend | Django |
| Database |SQLite |
| Frontend Styles | Bootstrap |
| Markup | HTML |
| Styling | CSS |
| Deployment |Railway|

---

## 🚀 Getting Started (Local Setup)

To run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/dipeshluitel/URL_shortener.git
cd urlshortener
```

### 2. Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # (Mac/Linux)
# or
venv\Scripts\activate      # (Windows)

```


### 3.Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Apply Migrations 

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server
```bash
python manage.py runserver
```
