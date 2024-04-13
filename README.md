# Qorpo Assignment


### FOLDER STRUCTURE 

```
my_project/
│
├── app/                        # Application root
│   ├── __init__.py             # Initializes your app and brings together all the components
│   ├── main.py                 # Entry point to your application, setup of your web server
│   │
│   ├── api/                    # Web layer where your endpoints are defined
│   │   ├── __init__.py
│   │   ├── endpoints/          # Different files for each collection of related endpoints
│   │   │   ├── user.py         # Example API endpoints for a 'user' resource
│   │   │   └── product.py      # Example API endpoints for a 'product' resource
│   │   └── dependencies.py     # Dependency injection (e.g., get_db) and other utilities
│   │
│   ├── core/                   # Core application logic, settings, and configs
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration settings and environment variables
│   │   └── security.py         # Security settings, e.g., password hashing, token generation
│   │
│   ├── models/                 # SQLAlchemy models (your database schema)
│   │   ├── __init__.py
│   │   ├── base.py             # Base model definitions, possibly abstract classes
│   │   ├── user.py             # User model
│   │   └── product.py          # Product model
│   │
│   ├── services/               # Business logic layer
│   │   ├── __init__.py
│   │   ├── user_service.py     # Operations related to user entity
│   │   └── product_service.py  # Operations related to product entity
│   │
│   ├── database/               # Database-related operations, e.g., session management
│   │   ├── __init__.py
│   │   ├── connection.py       # Database connection and session management
│   │   └── init_db.py          # Initial database setup, seed data
│   │
│   └── middleware/             # Middleware components, e.g., CORS, authentication
│       ├── __init__.py
│       └── auth_middleware.py  # Authentication middleware
│
├── tests/                      # Test suite for your application
│   ├── __init__.py
│   ├── test_api.py             # Test cases for your API endpoints
│   ├── test_models.py          # Test cases for model validations
│   └── test_services.py        # Test cases for service logic
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

```