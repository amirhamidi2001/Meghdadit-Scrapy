# Meghdadit Scrapy Spider

A Scrapy-based project for extracting product data from [meghdadit.com](https://meghdadit.com)  
and storing it in a MongoDB database.

---

## ✨ Features

- Crawls all product categories and paginated pages
- Extracts:
  - Product title
  - Product ID
  - URL
  - Categories
  - Currency
  - Availability status
- Saves items to MongoDB using a dedicated pipeline
- Fully respects `robots.txt`

---

## 🛠 Requirements

- Python 3.8+
- MongoDB (local or remote)
- Dependencies listed in `requirements.txt`

---

## 📦 Installation

```bash
git clone https://github.com/amirhamidi2001/Meghdadit-Scrapy.git
cd Meghdadit-Scrapy
pip install -r requirements.txt
```

Make sure your MongoDB service is running before starting the spider.

---

## ⚙️ Configuration

Edit the following file to adjust your MongoDB connection settings:

```
meghdadit/meghdadit/settings.py
```

```python
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "meghdadit"
MONGODB_COLLECTION = "items"
```

---

## ▶️ Usage

```bash
cd meghdadit
scrapy crawl meghdadit
```

The scraped data will be stored in your MongoDB database  
under the configured database and collection names.

---

## 📁 Project Structure

```
.
├── LICENSE
├── meghdadit/
│   ├── meghdadit/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders/
│   │       ├── meghdadit_spider.py
│   │       ├── plugins.py
│   │       └── __init__.py
│   └── scrapy.cfg
├── requirements.txt
└── README.md
```

---

## 🗄 Database

The MongoDB pipeline is implemented in:

```
meghdadit/meghdadit/pipelines.py
```

You can customize how items are processed or inserted into MongoDB here.

---

## 📜 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 👤 Author

**Amir Hamidi**  
GitHub: [amirhamidi2001](https://github.com/amirhamidi2001)