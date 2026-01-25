"""Database seeding script - creates test users on startup."""
import random
from sqlalchemy.orm import Session

from app.utils.database import SessionLocal, engine
from app.utils.auth import get_password_hash
from app.models.base import BaseModel
from app.models.users.admin import Admin
from app.models.users.customer import Customer
from app.models.users.driver import Driver
from app.models.users.restaurant import Restaurant
from app.models.review import Review
from app.core.enums import CuisineStyle

# Default password for all test users
DEFAULT_PASSWORD = "password123"


def clear_db(db: Session) -> None:
    """Clear all data from tables."""
    db.query(Review).delete()
    db.query(Admin).delete()
    db.query(Customer).delete()
    db.query(Driver).delete()
    db.query(Restaurant).delete()
    db.commit()
    print("Database cleared.")


def seed_admins(db: Session) -> list[Admin]:
    """Create test admin users."""
    admins_data = [
        {"username": "admin1", "email": "admin1@example.com"},
        {"username": "admin2", "email": "admin2@example.com"},
    ]

    admins = []
    for data in admins_data:
        admin = Admin(
            username=data["username"],
            email=data["email"],
            hashed_password=get_password_hash(DEFAULT_PASSWORD),
        )
        db.add(admin)
        admins.append(admin)

    db.commit()
    print(f"Created {len(admins)} admins.")
    return admins


def seed_customers(db: Session) -> list[Customer]:
    """Create test customer users."""
    customers_data = [
        {"username": "customer1", "email": "customer1@example.com", "phone_number": "555-0101"},
        {"username": "customer2", "email": "customer2@example.com", "phone_number": "555-0102"},
        {"username": "customer3", "email": "customer3@example.com", "phone_number": "555-0103"},
        {"username": "john_doe", "email": "john@example.com", "phone_number": "555-0104"},
        {"username": "jane_doe", "email": "jane@example.com", "phone_number": "555-0105"},
    ]

    customers = []
    for data in customers_data:
        customer = Customer(
            username=data["username"],
            email=data["email"],
            hashed_password=get_password_hash(DEFAULT_PASSWORD),
            phone_number=data["phone_number"],
        )
        db.add(customer)
        customers.append(customer)

    db.commit()
    print(f"Created {len(customers)} customers.")
    return customers


def seed_drivers(db: Session) -> list[Driver]:
    """Create test driver users."""
    drivers_data = [
        {"username": "driver1", "email": "driver1@example.com", "license_number": "DL-001", "vehicle_type": "car"},
        {"username": "driver2", "email": "driver2@example.com", "license_number": "DL-002", "vehicle_type": "motorcycle"},
        {"username": "driver3", "email": "driver3@example.com", "license_number": "DL-003", "vehicle_type": "bicycle"},
        {"username": "speedy_mike", "email": "mike@example.com", "license_number": "DL-004", "vehicle_type": "car"},
    ]

    drivers = []
    for data in drivers_data:
        driver = Driver(
            username=data["username"],
            email=data["email"],
            hashed_password=get_password_hash(DEFAULT_PASSWORD),
            license_number=data["license_number"],
            vehicle_type=data["vehicle_type"],
            is_available=True,
        )
        db.add(driver)
        drivers.append(driver)

    db.commit()
    print(f"Created {len(drivers)} drivers.")
    return drivers


def seed_restaurants(db: Session) -> list[Restaurant]:
    """Create test restaurant users."""
    restaurants_data = [
        {"username": "restaurant1", "email": "restaurant1@example.com", "name": "Pizza Palace", "address": "123 Main St", "phone_number": "555-1001", "cuisine_style": CuisineStyle.italian},
        {"username": "restaurant2", "email": "restaurant2@example.com", "name": "Sushi World", "address": "456 Oak Ave", "phone_number": "555-1002", "cuisine_style": CuisineStyle.japanese},
        {"username": "restaurant3", "email": "restaurant3@example.com", "name": "Taco Town", "address": "789 Elm Blvd", "phone_number": "555-1003", "cuisine_style": CuisineStyle.mexican},
        {"username": "restaurant4", "email": "restaurant4@example.com", "name": "Golden Dragon", "address": "321 Pine Rd", "phone_number": "555-1004", "cuisine_style": CuisineStyle.chinese},
        {"username": "restaurant5", "email": "restaurant5@example.com", "name": "Seoul Kitchen", "address": "654 Maple Dr", "phone_number": "555-1005", "cuisine_style": CuisineStyle.korean},
        {"username": "burger_joint", "email": "burger@example.com", "name": "Burger Joint", "address": "111 Fast Food Ln", "phone_number": "555-1006", "cuisine_style": CuisineStyle.american},
    ]

    restaurants = []
    for data in restaurants_data:
        restaurant = Restaurant(
            username=data["username"],
            email=data["email"],
            hashed_password=get_password_hash(DEFAULT_PASSWORD),
            name=data["name"],
            address=data["address"],
            phone_number=data["phone_number"],
            cuisine_style=data["cuisine_style"],
        )
        db.add(restaurant)
        restaurants.append(restaurant)

    db.commit()
    print(f"Created {len(restaurants)} restaurants.")
    return restaurants


def seed_reviews(db: Session, customers: list[Customer], restaurants: list[Restaurant]) -> list[Review]:
    """Create test reviews."""
    reviews = []
    review_contents = [
        "Great food, will order again!",
        "Delivery was fast and food was hot.",
        "Average experience, nothing special.",
        "Loved it! Best in town.",
        "Good value for money.",
        "Could be better, but decent.",
    ]

    for customer in customers[:3]:  # First 3 customers leave reviews
        for restaurant in random.sample(restaurants, min(3, len(restaurants))):  # Each reviews 3 random restaurants
            review = Review(
                customer_id=customer.id,
                restaurant_id=restaurant.id,
                content=random.choice(review_contents),
                rating=random.randint(3, 5),
            )
            db.add(review)
            reviews.append(review)

    db.commit()

    # Update restaurant ratings
    for restaurant in restaurants:
        restaurant.update_rating(db)
    db.commit()

    print(f"Created {len(reviews)} reviews.")
    return reviews


def seed_database() -> None:
    """Main function to seed the database."""
    db = SessionLocal()
    try:
        print("Starting database seed...")

        # Clear existing data
        clear_db(db)

        # Seed all user types
        admins = seed_admins(db)
        customers = seed_customers(db)
        drivers = seed_drivers(db)
        restaurants = seed_restaurants(db)

        # Seed reviews
        reviews = seed_reviews(db, customers, restaurants)

        print("Database seeding completed successfully!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()