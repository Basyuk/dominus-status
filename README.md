# Dominus Status Service

<div align="center">

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub issues](https://img.shields.io/github/issues/your-username/dominus-status)
![GitHub stars](https://img.shields.io/github/stars/your-username/dominus-status)

Infrastructure status management service with support for two types of authentication: local and Keycloak.

[Installation](#installation-and-running) •
[Documentation](#api-endpoints) •
[Contributing](#contributing) •
[Support](#support)

</div>

## Table of Contents

- [Features](#features)
- [Authentication Types](#authentication-types)
- [Installation and Running](#installation-and-running)
- [API Endpoints](#api-endpoints)
- [Keycloak Setup](#keycloak-setup)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [Issues and Support](#issues-and-support)
- [Donations](#donations)
- [License](#license)

## Features

- ✅ Service status management (primary/secondary/notset/noset)
- 🔐 Two authentication types: local and Keycloak
- 🐳 Docker containerization with multi-service support
- 📊 RESTful API for monitoring and management
- 🔒 JWT token validation with role-based access control
- 🌐 HTTPS support with SSL certificates
- 📝 Comprehensive logging and error handling
- 🔧 Configurable via environment variables

## Authentication Types

### 1. Local Authentication (default)

Uses HTTP Basic Authentication with username/password.

**Environment Variables:**
```bash
AUTH_TYPE=local
MANAGE_USERNAME=admin
MANAGE_PASSWORD=password
```

**Usage:**
```bash
# Get status
curl -u admin:password http://localhost:8000/status

# Change status
curl -X PUT -u admin:password "http://localhost:8000/state?new_state=primary"
```

### 2. Keycloak Authentication

Uses JWT tokens from Keycloak with role verification.

**Environment Variables:**
```bash
AUTH_TYPE=keycloak
KEYCLOAK_URL=http://your-keycloak:8080
KEYCLOAK_REALM=your-realm
KEYCLOAK_CLIENT_ID=dominus-status
KEYCLOAK_PUBLIC_KEY=your-public-key
REQUIRED_ROLE=dominus-admin
```

**Usage:**
```bash
# Get token from Keycloak
TOKEN=$(curl -X POST "http://keycloak:8080/realms/your-realm/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password&client_id=dominus-status&username=user&password=pass" | jq -r '.access_token')

# Get status
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/status

# Change status (requires dominus-admin role)
curl -X PUT -H "Authorization: Bearer $TOKEN" "http://localhost:8000/state?new_state=primary"
```

## Installation and Running

### 1. Clone Repository
```bash
git clone <repository-url>
cd dominus-status
```

### 2. Environment Variables Setup
Create `.env` file in project root:

**For local authentication:**
```bash
AUTH_TYPE=local
MANAGE_USERNAME=admin
MANAGE_PASSWORD=your-secure-password
```

**For Keycloak authentication:**
```bash
AUTH_TYPE=keycloak
KEYCLOAK_URL=http://your-keycloak:8080
KEYCLOAK_REALM=your-realm
KEYCLOAK_CLIENT_ID=dominus-status
KEYCLOAK_PUBLIC_KEY=your-public-key-here
REQUIRED_ROLE=dominus-admin
```

### 3. Run with Docker Compose
```bash
# Build and run
docker-compose build --no-cache
docker-compose up -d

# View logs
docker-compose logs -f dominus-status
```

### 4. Run Single Service
```bash
# Run only first service
docker-compose up dominus-status

# Run with local authentication
AUTH_TYPE=local docker-compose up dominus-status

# Run with Keycloak authentication
AUTH_TYPE=keycloak docker-compose up dominus-status
```

## API Endpoints

### GET /status
Get current service status.

**Response:**
```json
{
  "service_name": "test-service",
  "state": "primary",
  "hostname": "msk-app1",
  "user": "admin",
  "auth_type": "local"
}
```

### PUT /state
Change service status.

**Parameters:**
- `new_state`: primary, secondary, notset, noset

**Response:**
```json
{
  "service_name": "test-service",
  "state": "secondary",
  "hostname": "msk-app1",
  "user": "admin",
  "auth_type": "local"
}
```

## Keycloak Setup

1. **Create realm** in Keycloak
2. **Create client** with type "confidential"
3. **Configure roles** (e.g., `dominus-admin`)
4. **Get public key** from realm settings
5. **Assign roles** to users

## Project Structure

```
dominus-status/
├── dominus_status/           # Main package
│   ├── api/               # API routers
│   ├── core/              # Configuration and authentication
│   ├── models/            # Pydantic models
│   ├── services/          # Business logic
│   └── main.py           # Entry point
├── data/                  # State files
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile            # Docker image
└── requirements.txt      # Python dependencies
```

## Development

### Local Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run service
uvicorn dominus_status.main:app --reload --host 0.0.0.0 --port 8000
```

### Testing
```bash
# Test local authentication
curl -u admin:password http://localhost:8000/status

# Test Keycloak authentication
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/status
```

## Contributing

We welcome contributions from everyone! Here are some ways you can help:

- 🐛 [Report bugs](https://github.com/your-username/dominus-status/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D+)
- 💡 [Request features](https://github.com/your-username/dominus-status/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=%5BFEATURE%5D+)
- 📝 Improve documentation
- 🔧 Submit pull requests

Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test them
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a pull request

## Issues and Support

### 🐛 Found a Bug?

If you encounter any bugs or issues, please:

1. Check if the issue already exists in our [issue tracker](https://github.com/your-username/dominus-status/issues)
2. If not, [create a new bug report](https://github.com/your-username/dominus-status/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D+)
3. Include as much detail as possible (OS, Docker version, logs, etc.)

### 💡 Have an Idea?

We'd love to hear your ideas for new features:

1. [Submit a feature request](https://github.com/your-username/dominus-status/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=%5BFEATURE%5D+)
2. Describe your use case and how it would benefit others
3. We'll discuss it in the issue comments

### 🤝 Need Help?

- Check our [documentation](#api-endpoints) first
- Search through [existing issues](https://github.com/your-username/dominus-status/issues)
- Create a new [discussion](https://github.com/your-username/dominus-status/discussions) for questions

## ₿ Cryptocurrency Donations

**Perfect for saying "thanks" with your favorite cryptocurrency!**

### 🚀 Easy Method - NOWPayments

**[₿ Donate with Crypto →](https://nowpayments.io/donation/dominus)**

- **100+ cryptocurrencies** supported
- **Credit card to crypto** option available
- **Secure and trusted** payment processor  ч
- **Email notifications** for successful donations
- **Global availability**

**Popular supported cryptocurrencies:**
- Bitcoin (BTC) ₿
- Ethereum (ETH) ⟠
- Dogecoin (DOGE) 🐕
- Litecoin (LTC) 🥈
- Bitcoin Cash (BCH) 💚
- Cardano (ADA) 🎯
- Polkadot (DOT) 🔴
- And 90+ more!

### 🏠 Direct Wallet Donations

**For experienced crypto users who prefer direct transfers:**

- **Bitcoin (BTC):** `1FaUsKnBeS3fByxgi74fLgJJDDSEbmXUyn`
- **Ethereum (ETH):** `0x1bba0e0d37cba3308f296413762f802367b62e29`
- **Bitcoin Cash (BCH):** `bitcoincash:qz07dsqamckgpd2lwexaql73e6knnue2s57m6ru9jc`
- **Litecoin (LTC):** `LZoS8Y61j6HiSneqtF3xchN4RRoWpGDWbE`
- **Dogecoin (DOGE):** `DKiaQaipwqwwiz9HSh4DtSTu6MAY1LLL33`

### Other Ways to Support

- ⭐ Star this repository
- 🔄 Share the project with others
- 📝 Contribute to the code or documentation
- 🐛 Report bugs and suggest features

Every contribution, no matter how small, is greatly appreciated! ❤️

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for the open source community**

[⬆ Back to Top](#dominus-status-service)

</div> 