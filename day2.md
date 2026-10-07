# Day 2 API Design

## Endpoints

GET /facilities
GET /slots?facility_id=&date=
POST /bookings
GET /bookings?member_id=

## Facility

- id
- name
- weekday_price
- weekend_price

## Booking

- id
- member_id
- facility_id
- date
- start_time

## Availability responsibility

SlotRepository is responsible for retrieving/checking slot availability.

## SOLID improvement

The 3-active-bookings validation is separated from booking creation.