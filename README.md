# Qorpo Assignment


## FOLDER STRUCTURE 


```
.
├── README.md                                   # Project documentation
├── app                                         # Application root directory
│   ├── Dockerfile                              # Container configuration for app deployment
│   ├── __init__.py                             
│   ├── api                                     # Web layer handling the RESTful API endpoints
│   │   ├── __init__.py                        
│   │   └── endpoints                           
│   │       └── price_endpoint.py               # API endpoint for price-related operations
│   ├── core                                    # Core application configurations and settings
│   │   ├── __init__.py                         
│   │   └── config.py                           # Application configuration settings
│   ├── databasee                               # Data access layer, managing database connections
│   │   ├── __init__.py                         
│   │   └── connection.py                       # Database connection management
│   ├── docker-compose.yaml                     # Docker compose to manage app containers
│   ├── main.py                                 # Entry point of the application
│   ├── middleware                              # Middleware layer, for cross-cutting concerns
│   │   ├── __init__.py                         
│   │   └── ccxt_handler.py                     # Middleware to handle cryptocurrency data fetching
│   ├── models                                  # Data models representing the structure of data
│   │   ├── __init__.py                         
│   │   ├── price_models.py                     # Models related to price data
│   │   └── utils.py                            # Utilities and helpers for models
│   ├── requirements.txt                        # Dependencies for the application
│   └── service                                 # Service layer handling the business logic
│       ├── __init__.py                     
│       └── kucoin_service.py                   # Services related to kucoin cryptocurrency operations
└── test                                        # Test directory for application tests
    └── endpoint_test.py                        # Test cases for API endpoints

```




## API Endpoints


### 1. Get Current Price

**Endpoint**: GET `/price/{currency}`

**Description**: Fetches the current price of a specified cryptocurrency from the KuCoin exchange.

**URL Parameters**:

- **currency (required)**: The ticker symbol of the cryptocurrency (e.g., BTC-USDT, ETH-USDT).

**Success Response**:

- **Code**: 200 OK
- **Content**: `{"currency": "BTC-USDT", "price": 50000, "date": "2024-04-14T12:00:00Z"}`

**Error Response**:

- **Code**: 400 Bad Request
- **Content**: `{"message": "Price for {currency} not available at the moment"}`


### 2. Get Price History

**Endpoint**: GET `/price/history`

**Description**: Retrieves the price history of a specified cryptocurrency.

**Query Parameters**:

- **page** (optional, default=1): The page number for pagination.
- **page_limit** (optional, default=10): The number of price records to return per page.
- **currency** (optional): The ticker symbol of the cryptocurrency to filter the price history. If not provided, the history of all tracked currencies will be returned.

**Success Response**:

- **Code**: 200 OK
- **Content**: `{"data": [{"currency": "BTC", "price": 50000, "date": "2024-04-14T12:00:00Z"}, ...]}`

**Error Response**:

- **Code**: 400 Bad Request
- **Content**: `{"message": "Error message related to fetching price history"}`

### 3. Delete Price History

**Endpoint**: DELETE `/price/history`

**Description**: Deletes all stored price history data from the database.

**Success Response**:

- **Code**: 200 OK
- **Content**: `{"message": "Price history deleted successfully"}`

**Error Response**:

- **Code**: 400 Bad Request
- **Content**: `{"message": "Error message related to deleting price history"}`




## GET STARTED 


### 1. BUILD AND RUN DOCKER COMPOSE
To run the code, you need to have `docker` and `docker compose` installed on your computer. 

To build and run the `docker-compose`, run the following and command

```
docker-compose build
docker-compose up
```

### 2. TRY END POINT USING CURL

- Get Current Price
```curl -X GET http://localhost:8000/price/BTC-USDT```

- Get Price History
```curl -X GET http://localhost:8000/price/history?page=1&page_limit=10&currency=BTC-USDT```

- Delete Price History
```curl -X DELETE http://localhost:8000/price/history```



## RUN PYTEST 
To run `PyTest` on endpoints, run following command 

```
cd .. && cd test
pytest endpoint_test.py
```