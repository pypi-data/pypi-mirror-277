# NOVA Python Client

## Getting Started

### Prerequisites

- Python (>= 3.12)

### Installation

```bash
# Create a virtual environment
virtualenv -p python3.12 venv

# Activate the virtual environment
source venv/bin/activate

# Install package (editable)
pip install -e '.[dev]'

# Install pre-commit hooks
pre-commit install
```

### Running tests

Create a `.env` file with api key and bot id

```
NOVA_API_KEY="..."
BOT_ID="bot-..."
```
