from datetime import date, timedelta
from random import randrange, seed


def generate_phi(num_patients: int):
    # Load names
    names: list = load_names_and_gender()

    patients: list = []
    for count in range(num_patients):
        # Get random name
        patient: dict = get_random_name_and_gender(names)

        # Get random DOB
        patient["dob"] = date.strftime(generate_random_dob(), "%m/%d/%Y")

        # Get random MRN
        patient["mrn"] = randrange(10000, 500000)

        patients.append(patient)

    return patients


def get_random_name_and_gender(name_list: list) -> dict:
    rand_pos: int = randrange(len(name_list))
    return name_list[rand_pos]


def generate_random_dob() -> date:
    start_date: date = date(1980, 1, 1)
    end_date: date = date(2024, 6, 30)
    interval_dates: timedelta = end_date - start_date
    total_days: int = interval_dates.days

    seed(a=None)
    randay: int = randrange(total_days)
    randate: date = start_date + timedelta(days=randay)
    return randate


def load_names_and_gender() -> list:
    names: list = []
    with open("names.txt", "r") as f:
        for line in f:
            name, gender = line.strip().split(",")
            nameArr: list = name.split(" ")
            tmpDict: dict = {}
            tmpDict["fname"] = nameArr[0].strip()
            tmpDict["lname"] = nameArr[-1].strip()
            tmpDict["mname"] = ""
            if len(nameArr) > 2:
                tmpDict["mname"] = nameArr[1].strip()
            tmpDict["gender"] = gender.strip()
            names.append(tmpDict)
    return names


if __name__ == "__main__":
    print(
        "This script generates fictious patient records for software development and testing purposes."
    )
    num_patients = int(input("How many patient records to generate? "))
    print(generate_phi(num_patients))
