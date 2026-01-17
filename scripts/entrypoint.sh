#!/bin/bash
set -e

echo "Waiting for database..."
while ! pg_isready -h db -p 5432 -U ${POSTGRES_USER:-postgres}; do
    sleep 1
done
echo "Database is ready!"

# Run database seed if SEED_DB is set to true
if [ "${SEED_DB:-false}" = "true" ]; then
    echo "Seeding database..."
    python -m app.db.seed
fi

# Start the application
exec python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
