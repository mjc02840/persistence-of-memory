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

## Voice Interface Layer

Frontend Stack:
  - React 18.2 with Web Speech API
  - Axios for HTTP requests
  - Pastel color scheme (CSS gradients)
  - 3px lime green borders on buttons and responses

Backend Stack:
  - Express.js server (port 3001)
  - PostgreSQL connection to aaa database
  - CORS enabled for frontend communication
  - Basic query parsing (number extraction)

Data Flow:
  Voice Input → Web Speech API → Transcription
  → HTTP POST /api/query → Backend
  → SQL generation (Claude API pending)
  → PostgreSQL quintrix_products
  → JSON response → Display in UI

Database Connection:
  Host: localhost:5432
  Database: aaa
  Table: quintrix_products (817 rows)
  User: aaa (superuser)

Status: READY FOR CLAUDE API INTEGRATION

## Q19 Voice + Claude Complete Stack

Frontend (React):
  - Web Speech Recognition (4 languages)
  - Speech Synthesis for responses
  - Error display and loading feedback
  - Pastel UI with lime borders

Backend (Node.js):
  - Express.js on port 3001
  - PostgreSQL connection pool
  - Claude Opus 3 API integration
  - Safe prompt: SELECT-only SQL generation
  - SQL validation: blocks INSERT/UPDATE/DELETE/DROP/CREATE/ALTER/TRUNCATE
  - Result formatting: name, price, category, preview, image
  - Error handling and logging

Database:
  - PostgreSQL (localhost:5432)
  - Table: quintrix_products (817 rows)
  - Indexed on name, price, original_url

Security:
  - .env with API key (600 permissions)
  - SQL validation (no DML/DDL)
  - Query timeout (30s)
  - CORS enabled

Status: READY FOR PRODUCTION

## Q19 PRODUCTION DEPLOYMENT

Complete Voice-to-SQL Architecture:

Frontend (React @ port 3000):
  - Web Speech Recognition + Synthesis
  - 4 multilingual options
  - Pastel UI with lime borders
  - Real-time transcription/response display

Backend (Node.js @ port 3001):
  - Express server with CORS
  - PostgreSQL connection pool
  - Claude Opus 3 API integration
  - SQL validation (SELECT + LIMIT 20)
  - Comprehensive logging

Database (PostgreSQL):
  - Host: localhost:5432
  - DB: aaa / Table: quintrix_products
  - 817 products, indexed on name/price/url
  - User: aaa (superuser)

Flow:
  Voice Input → Transcription → Backend
  → Claude (safe SQL) → PostgreSQL
  → Formatted JSON → TTS + Display

Status: READY FOR PRODUCTION
