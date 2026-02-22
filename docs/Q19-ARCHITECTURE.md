# Q19 Architecture\nNode.js/React/SQLite3 on Debian.

## Database Layer

Production database: PostgreSQL 'q19_inventory' owned by user 'aaa'. Schema: inventory_items (id, name, description, price, category, original_url, local_image).

## Data Layer Finalized

PostgreSQL user 'aaa' (superuser) @ localhost:5432  
Database 'aaa' → Table 'quintrix_products' (817 rows)  

Schema:  
  - id SERIAL PK  
  - name TEXT NOT NULL (product title)  
  - description TEXT (filtered paragraphs)  
  - price DECIMAL(12,2) (extracted from h2 RON pattern)  
  - currency VARCHAR(10) (default 'RON')  
  - category VARCHAR(255) (breadcrumb navigation)  
  - original_url VARCHAR(512) UNIQUE (source HTML path)  
  - local_image VARCHAR(512) (image URL for catalog)  
  - inserted_at TIMESTAMP DEFAULT NOW()  
  - updated_at TIMESTAMP DEFAULT NOW()  

Indexes: name, price, original_url (UNIQUE)  
Duplicate protection: ON CONFLICT original_url DO NOTHING  

Import script features:  
  ✓ Auto-detect selectors from samples  
  ✓ Fallback chains (e.g., h1 → .title → [itemprop])  
  ✓ Recursive HTML scan (2278 files)  
  ✓ Batch inserts (250 items/query)  
  ✓ Price extraction: regex (\d+[.,]\d{2}) RON  
  ✓ Category from breadcrumb navigation  
  ✓ Logging every 500 files  
  ✓ Error recovery (continue on parse errors)  
  ✓ Zero errors in production run

## Data Layer Verified - Production Ready

PostgreSQL: localhost:5432 / Database aaa / User aaa (superuser)
Table quintrix_products (817 rows)

Schema:
  id SERIAL PK
  name VARCHAR(255) NOT NULL
  description TEXT
  price DECIMAL(12,2)
  currency VARCHAR(10) DEFAULT RON
  category VARCHAR(255)
  original_url VARCHAR(512) UNIQUE
  local_image VARCHAR(512)
  inserted_at/updated_at TIMESTAMP

Indexes: name, price, original_url (UNIQUE)
Duplicate protection: ON CONFLICT original_url

Import: 2278 files scanned → 817 products (35.9%)
Batch size: 250 items
Processing time: ~8.5 minutes
Errors: 0

Selectors (15-file sample):
  name: h1 / .title / [itemprop]
  price: h2 with RON pattern (loop detection)
  category: breadcrumb navigation
  image: img[src*=catalog]
  description: p (filtered)

Status: PRODUCTION READY
Next: Voice interface (Web Speech API + Claude API)
