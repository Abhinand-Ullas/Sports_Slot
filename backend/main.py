from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/facilities")
def get_facilities():
    return [
        {
            "id": 1,
            "name": "Badminton Court 1",
            "weekday_price": 100,
            "weekend_price": 150
        },
        {
            "id": 2,
            "name": "Badminton Court 2",
            "weekday_price": 100,
            "weekend_price": 150
        },
        {
            "id": 3,
            "name": "Tennis Court",
            "weekday_price": 200,
            "weekend_price": 300
        }
    ]

@app.get("/slots")
def get_slots(facility_id: int, date: str):
    return [
        {
            "start_time": "06:00",
            "available": True
        },
        {
            "start_time": "07:00",
            "available": True
        }
    ]

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