# fastapi-food-delivery-app-backend
This project is a personal reimplementation based on a previous academic group project for food delivery app

## Quick Start

### Run with Docker

```bash
# Start with database seeding (creates test users)
SEED_DB=true docker-compose up --build

# Start without seeding
docker-compose up --build
```

### Access Points
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **PgAdmin**: http://localhost:5050

## Test Users

All test users have the same password: `password123`

### Admins

| Username | Email | Role |
|----------|-------|------|
| admin1 | admin1@example.com | admin |
| admin2 | admin2@example.com | admin |

### Customers

| Username | Email | Phone |
|----------|-------|-------|
| customer1 | customer1@example.com | 555-0101 |
| customer2 | customer2@example.com | 555-0102 |
| customer3 | customer3@example.com | 555-0103 |
| john_doe | john@example.com | 555-0104 |
| jane_doe | jane@example.com | 555-0105 |

### Drivers

| Username | Email | License | Vehicle |
|----------|-------|---------|---------|
| driver1 | driver1@example.com | DL-001 | car |
| driver2 | driver2@example.com | DL-002 | motorcycle |
| driver3 | driver3@example.com | DL-003 | bicycle |
| speedy_mike | mike@example.com | DL-004 | car |

### Restaurants

| Username | Email | Name | Cuisine | Address |
|----------|-------|------|---------|---------|
| restaurant1 | restaurant1@example.com | Pizza Palace | italian | 123 Main St |
| restaurant2 | restaurant2@example.com | Sushi World | japanese | 456 Oak Ave |
| restaurant3 | restaurant3@example.com | Taco Town | mexican | 789 Elm Blvd |
| restaurant4 | restaurant4@example.com | Golden Dragon | chinese | 321 Pine Rd |
| restaurant5 | restaurant5@example.com | Seoul Kitchen | korean | 654 Maple Dr |
| burger_joint | burger@example.com | Burger Joint | american | 111 Fast Food Ln |

## Database Seeding

To seed the database manually:

```bash
# Inside the container
python -m app.db.seed

# Or from host with docker
docker-compose exec app python -m app.db.seed
```

The seed script will:
1. Clear all existing data
2. Create test users (admins, customers, drivers, restaurants)
3. Create sample reviews
4. Update restaurant ratings based on reviews
