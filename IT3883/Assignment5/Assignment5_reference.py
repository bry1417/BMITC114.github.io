# Program Name: Assignment5_reference.py
# Course: IT3883 / Section WO1 - Advanced Application Development
# Student Name: Bryson Mitchell
# Assignment Number: Lab 5
# Due Date: 11/20/2026
# Purpose: Store the supplied daily temperature readings in SQLite and
#          print the average temperatures for Sunday and Thursday.
# Resources: Assignment 5 handout and Assignment5input.txt
#            https://docs.python.org/3/library/sqlite3.html
#            https://www.sqlite.org/lang_aggfunc.html#avg
# Assistance: ChatGPT wrote this worked example for Bryson Mitchell.

import sqlite3
from contextlib import closing
from pathlib import Path


def read_temperatures(input_path):
    """Read one weekday and one decimal temperature from each nonempty line."""
    readings = []
    with input_path.open(encoding="utf-8-sig") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                day, temperature_text = line.split()
                temperature = float(temperature_text)
            except ValueError as error:
                raise ValueError(
                    f"Expected a weekday and a numeric temperature on line {line_number}."
                ) from error
            readings.append((day, temperature))
    return readings


def main():
    # Find the input and database beside the program, including when run from an IDE.
    folder = Path(__file__).resolve().parent
    readings = read_temperatures(folder / "Assignment5input.txt")

    with closing(sqlite3.connect(folder / "Assignment5_reference.sqlite3")) as database:
        # Refresh the assignment table in one transaction so reruns count each line once.
        with database:
            database.execute("""
                CREATE TABLE IF NOT EXISTS TemperatureReadings (
                    ID INTEGER PRIMARY KEY,
                    Day_Of_Week TEXT NOT NULL,
                    Temperature_Value REAL NOT NULL
                )
            """)
            database.execute("DELETE FROM TemperatureReadings")
            # SQLite assigns the ID. The two placeholders receive the day and value.
            database.executemany(
                "INSERT INTO TemperatureReadings (Day_Of_Week, Temperature_Value) "
                "VALUES (?, ?)",
                readings,
            )

        print(f"Imported {len(readings):,} readings.")
        # Filtering by one day at a time gives each average its own set of readings.
        for day in ("Sunday", "Thursday"):
            count, average = database.execute(
                "SELECT COUNT(*), AVG(Temperature_Value) FROM TemperatureReadings "
                "WHERE Day_Of_Week = ?",
                (day,),
            ).fetchone()
            if count:
                print(f"{day} average temperature: {average:.2f} ({count} readings)")
            else:
                print(f"{day} has no readings.")


if __name__ == "__main__":
    main()
