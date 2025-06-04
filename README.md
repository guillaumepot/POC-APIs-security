# POC - OWASP 2023 Top 10 API Security Vulnerabilities

<div align="center">
  <h3>🔐 Educational API Security Demonstration</h3>
  <p>
    A comprehensive FastAPI-based proof of concept demonstrating all 10 OWASP API Security Top 10 (2023) vulnerabilities with both vulnerable and secure implementations for educational purposes.
  </p>
  
  [![OWASP 2023 Top10 API vulnerabilities](https://img.shields.io/badge/OWASP-2023_Top10_API_vulnerabilities-blue)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
  [![Python](https://img.shields.io/badge/python-v3.13.2+-blue.svg)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12+-green.svg)](https://fastapi.tiangolo.com/)
  [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
</div>

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [OWASP API Security Top 10 Coverage](#owasp-api-security-top-10-coverage)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Starting the Server](#starting-the-server)
  - [API Documentation](#api-documentation)
  - [Test Accounts](#test-accounts)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Security Features](#security-features)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 About The Project

This project is an educational demonstration of the **OWASP API Security Top 10 (2023)** vulnerabilities. It provides:

- **Vulnerable endpoints** that demonstrate each of the 10 API security risks
- **Secure counterparts** showing proper implementation and mitigation techniques
- **Complete documentation** of each vulnerability with examples
- **Testing scripts** to verify vulnerabilities and their fixes
- **Real-world scenarios** that developers commonly encounter

**⚠️ Warning**: This application contains intentionally vulnerable code for educational purposes. **Never deploy this in a production environment**.

## 🔥 OWASP API Security Top 10 Coverage

| Vulnerability | Status | Description |
|---------------|---------|-------------|
| **API1:2023** | ✅ | Broken Object Level Authorization (BOLA) |
| **API2:2023** | ✅ | Broken Authentication |
| **API3:2023** | ✅ | Broken Object Property Level Authorization |
| **API4:2023** | ✅ | Unrestricted Resource Consumption |
| **API5:2023** | ✅ | Broken Function Level Authorization |
| **API6:2023** | ✅ | Unrestricted Access to Sensitive Business Flows |
| **API7:2023** | ✅ | Server Side Request Forgery (SSRF) |
| **API8:2023** | ✅ | Security Misconfiguration |
| **API9:2023** | ✅ | Improper Inventory Management |
| **API10:2023** | ✅ | Unsafe Consumption of APIs |

Each vulnerability includes:
- 🔴 **Broken implementation** (demonstrates the vulnerability)
- 🟢 **Fixed implementation** (shows proper security measures)

## 🛠 Tech Stack

- **Backend**: FastAPI (0.115.12+)
- **Authentication**: JWT with PyJWT, Passlib, Argon2
- **Database**: SQLite with custom ORM
- **Security**: Rate limiting (SlowAPI), Input validation (Pydantic)
- **Templates**: Jinja2
- **Environment**: Python 3.13.2+
- **Package Management**: UV
- **Development**: Uvicorn (ASGI server)

## 🚀 Getting Started

### Prerequisites

1. **UV Package Manager** (recommended):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   
2. **Python 3.13.2+** (if not using UV):
   ```bash
   python --version  # Should be 3.13.2+
   ```

3. **[Optional] hCaptcha Keys** for captcha-protected routes:
   - Get free keys from [hCaptcha](https://www.hcaptcha.com/)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/guillaumepot/POC-APIs-security.git
   cd POC-APIs-security
   ```

2. **Set up the environment**:
   ```bash
   uv sync
   ```

3. **Create environment configuration**:
   ```bash
   # Create the config directory if it doesn't exist
   mkdir -p src/config
   
   # Create .env file
   cat > src/config/.env << EOF
   DB_NAME='./database/database.db'
   API_HOST='localhost'
   API_PORT=8000
   HTML_TEMPLATES_DIR='./src/templates'
   CAPTCHA_VERIFY_URL='https://hcaptcha.com/siteverify'
   CAPTCHA_SITE_KEY='changeme'
   CAPTCHA_SECRET='changeme'
   LOGS_FILEPATH='./logs/api.log'
   EOF
   ```

4. **Generate sample database and logs**:
   ```bash
   uv run scripts/generate_example_database.py
   ```

### Configuration

The application uses environment variables defined in `src/config/.env`:

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_NAME` | SQLite database path | `./database/database.db` |
| `API_HOST` | Server host | `localhost` |
| `API_PORT` | Server port | `8000` |
| `HTML_TEMPLATES_DIR` | Templates directory | `./src/templates` |
| `CAPTCHA_SITE_KEY` | hCaptcha site key | `changeme` |
| `CAPTCHA_SECRET` | hCaptcha secret key | `changeme` |
| `LOGS_FILEPATH` | API logs file path | `./logs/api.log` |

## 💻 Usage

### Starting the Server

```bash
# Start the development server
uv run main.py

# Or using uvicorn directly
uv run uvicorn src.app:app --host localhost --port 8000 --reload
```

The API will be available at: `http://localhost:8000`

### API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

### Test Accounts

| Username | Password | Role | Description |
|----------|----------|------|-------------|
| `admin` | `admin` | Administrator | Full access to all endpoints |
| `john_doe` | `johndoe` | Regular User | Limited access for testing BOLA |

## 🔗 API Endpoints

### Authentication
- `POST /login` - User authentication (JWT token)
- `GET /read_payload` - Decode JWT payload
- `GET /jwt_secret_key` - [VULNERABLE] Expose JWT secret

### Vulnerability Demonstrations

#### API1 - Broken Object Level Authorization
- `GET /vuln1/broken/collaborator/{id}` - 🔴 Access any user's data
- `GET /vuln1/fixed/collaborator/{id}` - 🟢 Proper authorization checks

#### API2 - Broken Authentication  
- `POST /vuln2/broken/login` - 🔴 Weak authentication
- `POST /vuln2/fixed/login` - 🟢 Secure authentication

#### API3 - Broken Object Property Level Authorization
- `GET /vuln3/broken/activity` - 🔴 Excessive data exposure
- `POST /vuln3/broken/register` - 🔴 Mass assignment vulnerability
- `GET /vuln3/fixed/activity` - 🟢 Filtered response data
- `POST /vuln3/fixed/register` - 🟢 Input validation and filtering

#### API4 - Unrestricted Resource Consumption
- `GET /vuln4/broken/limited_route` - 🔴 No rate limiting
- `GET /vuln4/fixed/limited_route` - 🟢 Rate limiting implemented

#### API5 - Broken Function Level Authorization
- `GET /vuln5/broken/limited_to_admin` - 🔴 Missing role checks
- `GET /vuln5/fixed/limited_to_admin` - 🟢 Proper role-based access

#### API6 - Unrestricted Access to Sensitive Business Flows
- `GET /vuln6/broken/route_to_spam` - 🔴 No business logic protection
- `GET /vuln6/fixed/route_to_spam` - 🟢 Protected sensitive operations

#### API7 - Server Side Request Forgery
- `GET /vuln7/broken/fetch` - 🔴 Unvalidated external requests
- `GET /vuln7/fixed/fetch` - 🟢 Domain whitelist validation

#### API8 - Security Misconfiguration
- `GET /vuln8/broken/logs` - 🔴 Sensitive information exposure
- `GET /vuln8/fixed/logs` - 🟢 Secured endpoint with proper access control

#### API9 - Improper Inventory Management
- `GET /vuln9/beta/user_info` - 🔴 Unversioned/test endpoint exposure
- `GET /vuln9/administration/user_info` - 🟢 Properly managed endpoint

#### API10 - Unsafe Consumption of APIs
- `GET /vuln10/broken/sql_query` - 🔴 SQL injection via external API data
- `GET /vuln10/fixed/sql_query` - 🟢 Parameterized queries and input validation

## 📁 Project Structure

```
POC-APIs-security/
├── src/
│   ├── app.py                 # FastAPI application
│   ├── config/
│   │   ├── config.py          # Configuration management
│   │   ├── .env               # Environment variables
│   │   └── *.yaml, *.json     # Config files
│   ├── routes/
│   │   ├── login.py           # Authentication endpoints
│   │   ├── vuln1.py           # OWASP API1 demonstrations
│   │   ├── vuln2.py           # OWASP API2 demonstrations
│   │   └── ...                # API3-API10 demonstrations
│   ├── templates/             # Jinja2 HTML templates
│   └── utils/
│       ├── security_functions.py  # Security utilities
│       ├── sqlite_engine.py       # Database operations
│       ├── rate_limiter.py        # Rate limiting
│       └── logger.py              # API logging
├── scripts/
│   ├── generate_example_database.py  # Database setup
│   ├── test_api_routes.py           # API testing
│   └── simulate_dos_on_api.py       # DoS testing
├── database/
│   └── database.db            # SQLite database
├── logs/                      # Application logs
├── main.py                    # Application entry point
├── pyproject.toml            # Project dependencies
└── README.md                 # This file
```

## 🧪 Testing

### Run API Tests
```bash
# Test all vulnerable and secure endpoints
uv run scripts/test_api_routes.py

# Simulate DoS attack (for API4 testing)
uv run scripts/simulate_dos_on_api.py
```

### Manual Testing
1. Start the server: `uv run main.py`
2. Open Swagger UI: `http://localhost:8000/docs`
3. Use test accounts to authenticate
4. Try both vulnerable and secure endpoints
5. Observe the differences in behavior

## 🔒 Security Features

### Implemented Security Measures
- **JWT Authentication** with proper token validation
- **Rate Limiting** using SlowAPI
- **Input Validation** with Pydantic models
- **SQL Injection Protection** with parameterized queries
- **CORS Configuration** for cross-origin requests
- **Password Hashing** using Argon2
- **Role-Based Access Control** (RBAC)
- **Request Logging** for audit trails

### Security Testing Tools
- Built-in testing scripts for all vulnerabilities
- DoS simulation for rate limiting tests
- JWT token manipulation examples
- SQL injection test cases

## 👨‍💻 Development

### Development Dependencies
```bash
uv sync --group dev
```

### Code Quality Tools
- **Ruff** - Linting and formatting
- **GittyLeaks** - Secret detection
- **Pre-commit hooks** - Code quality enforcement

### Running Development Server
```bash
uv run main.py  # Auto-reload enabled
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contributing Guidelines
- Follow the existing code style
- Add tests for new features
- Update documentation as needed
- Ensure all security demonstrations work correctly

## 📄 License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.

## 📞 Contact

**Guillaume Pot**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/062guillaumepot/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/guillaumepot)

**Project Link**: [https://github.com/guillaumepot/POC-APIs-security](https://github.com/guillaumepot/POC-APIs-security)

---

## ⚠️ Disclaimer

This project is intended **solely for educational purposes**. The vulnerable code examples are designed to help developers understand common API security pitfalls and how to avoid them. 

**DO NOT** use this code in production environments or as a basis for real applications without proper security reviews and implementations.

---

<div align="center">
  <p><strong>🔐 Learn. Secure. Protect. 🔐</strong></p>
  <p><em>Understanding vulnerabilities is the first step to building secure APIs</em></p>
</div>