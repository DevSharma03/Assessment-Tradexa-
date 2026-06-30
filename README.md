# Assessment-Tradexa: Box Selector API

A Django REST Framework application that intelligently selects the most appropriate shipping box based on product dimensions and weight constraints.

## Overview

This project implements a box selection algorithm for Tradexa that takes a list of items (with dimensions and weight) and automatically selects the smallest suitable box from a predefined inventory. The system handles multiple products, validates constraints, and provides detailed order summaries.

## Features

- **Smart Box Selection**: Automatically selects the smallest box that fits all items
- **Weight Validation**: Ensures the total weight doesn't exceed box capacity
- **Dimension Checking**: Validates that all items fit within box dimensions
- **Order Summary**: Provides detailed information about selected box and total weight
- **Error Handling**: Clear error messages when no suitable box is found
- **REST API**: Clean API endpoints for box selection queries

## Project Structure

```
Assessment-Tradexa-/
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── config/            # Django configuration
│   └── settings.py    # Project settings
└── boxes/             # Main application
    ├── models.py      # Box and Item models
    ├── views.py       # API views
    ├── serializers.py # DRF serializers
    └── tests.py       # Unit tests
```

## Requirements

- Python 3.8+
- Django
- Django REST Framework

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DevSharma03/Assessment-Tradexa-.git
cd Assessment-Tradexa-
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply migrations:
```bash
python manage.py migrate
```

## Usage

### Running the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

### API Endpoint

**POST** `/api/boxes/select/`

**Request Example:**
```json
{
  "items": [
    {
      "name": "Mug",
      "length": 10,
      "width": 10,
      "height": 12,
      "weight": 0.4,
      "quantity": 2
    },
    {
      "name": "Book",
      "length": 20,
      "width": 15,
      "height": 3,
      "weight": 0.5,
      "quantity": 3
    }
  ]
}
```

**Response Example:**
```json
{
  "selected_box": {
    "name": "M",
    "length": 30,
    "width": 25,
    "height": 20,
    "max_weight": 5.0
  },
  "order_summary": {
    "total_weight": 2.3,
    "total_items": 5
  }
}
```

### Running Tests

Execute all unit tests:
```bash
python manage.py test
```

All 7 tests should pass with the following output:
```
Found 7 test(s).
System check identified no issues (0 silenced).
.......
Ran 7 tests in 0.010s
OK
```

## Test Coverage

The project includes comprehensive tests covering:
- Single product fitting
- Multiple products fitting
- Exact weight limit boundaries
- Weight exceeding box capacity
- Dimensions exceeding all available boxes
- Empty order validation
- Invalid request handling

## Configuration

Box definitions and API settings are configured in `config/settings.py`. Boxes are predefined with:
- **XS**: Small box
- **S**: Small-Medium box
- **M**: Medium box
- **L**: Large box
- **XL**: Extra Large box

Each box has maximum dimensions and weight capacity constraints.

## Error Handling

When no suitable box is found, the API returns:
```json
{
  "selected_box": null,
  "reason": "Item [name] cannot fit in any available box"
}
```

Or for weight-related issues:
```json
{
  "selected_box": null,
  "reason": "Total weight exceeds capacity"
}
```

## Author

DevSharma03

## License

[Add your license here]
