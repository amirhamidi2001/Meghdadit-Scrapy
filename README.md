```markdown
# Meghdadit Scrapy

A Scrapy spider that extracts product data from [meghdadit.com](https://meghdadit.com) and stores it in MongoDB.

## Features

- Extracts product title, ID, URL, categories, currency, and availability
- Saves data to MongoDB
- Respects `robots.txt`

## Requirements

- Python 3.8+
- MongoDB running locally (or update `MONGODB_URI` in `settings.py`)

## Installation

```bash
git clone https://github.com/amirhamidi2001/Meghdadit-Scrapy.git
cd Meghdadit-Scrapy
pip install scrapy pymongo
```

## Usage

Run the spider:

```bash
scrapy crawl meghdadit
```

Data will be saved in the `meghdadit` database, `items` collection.

## Configuration

Edit `meghdadit/settings.py` to change MongoDB connection or collection name:

```python
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "meghdadit"
MONGODB_COLLECTION = "items"
```

## Project Structure

```
├── meghdadit/
│   ├── spiders/
│   │   └── meghdadit_spider.py   # main spider
│   ├── items.py                  # item definition
│   ├── pipelines.py              # MongoDB pipeline
│   └── settings.py
└── README.md
```

## License

MIT
```