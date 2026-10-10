from fastapi import FastAPI
from db import get_connection
from datetime import date
from fastapi import Query
app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/facilities")
def get_facilities():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT id, name, weekday_price, weekend_price
            FROM facilities
            ORDER BY id;
        """)

        rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "name": row[1],
                "weekday_price": float(row[2]),
                "weekend_price": float(row[3])
            }
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()


@app.get("/slots")
def get_slots(
    facility_id: int,
    booking_date: date = Query(..., alias="date")
):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT start_time
            FROM bookings
            WHERE facility_id = %s
              AND booking_date = %s;
        """, (facility_id, booking_date))

        rows = cursor.fetchall()

        booked_times = {
            row[0].strftime("%H:%M")
            for row in rows
        }

        slots = []

        for hour in range(6, 22):
            start_time = f"{hour:02d}:00"

            slots.append({
                "start_time": start_time,
                "available": start_time not in booked_times
            })

        return slots

    finally:
        cursor.close()
        connection.close()

def validate_booking_limit(member_id: int):
    # temporary hardcoded validation
    # database logic comes on Day 3
    return True

@app.post("/bookings")
def create_booking(
    member_id: int,
    facility_id: int,
    date: str,
    start_time: str
):
    validate_booking_limit(member_id)

    return {
        "message": "Booking created",
        "member_id": member_id,
        "facility_id": facility_id,
        "date": date,
        "start_time": start_time
    }