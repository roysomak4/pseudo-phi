from datetime import date, timedelta
from random import randrange, seed


def generate_phi(num_patients: int = 1):
    # Load names
    fnames, lnames, minitials = load_names()

    patients: list = []
    for count in range(num_patients):
        # Get random name
        patient: dict = get_random_name(fnames, lnames, minitials)

        # Get random DOB
        patient["dob"] = date.strftime(generate_random_dob(), "%m/%d/%Y")

        # Get random MRN
        patient["mrn"] = randrange(10000, 500000)

        # Get random gender
        genders = ["M", "F"]
        option = randrange(0, 2)
        patient["gender"] = genders[option]

        patients.append(patient)

    return patients


def get_random_name(fnames: list, lnames: list, minitials: list) -> tuple:
    patient = {}
    rand_pos: int = randrange(len(fnames))
    patient["firstname"] = fnames[rand_pos]
    patient["lastname"] = lnames[rand_pos]
    patient["minitial"] = minitials[rand_pos]
    return patient


def generate_random_dob() -> date:
    start_date: date = date(1980, 1, 1)
    end_date: date = date(2024, 6, 30)
    interval_dates: timedelta = end_date - start_date
    total_days: int = interval_dates.days

    seed(a=None)
    randay: int = randrange(total_days)
    randate: date = start_date + timedelta(days=randay)
    return randate


def load_names() -> tuple:
    fnames: list = []
    lnames: list = []
    minitials: list = []
    with open("names.txt", "r") as f:
        for line in f:
            tmpArr = line.strip().split(" ")
            minitial = ""
            fname = tmpArr[0]
            lname = tmpArr[-1]
            if len(tmpArr) > 2:
                minitial = tmpArr[1]
            fnames.append(fname)
            lnames.append(lname)
            minitials.append(minitial)
    return fnames, lnames, minitials


if __name__ == "__main__":
    print(
        "This script generates fictious patient records for software development and testing purposes."
    )
    num_patients = int(input("How many patient records to generate? "))
    print(generate_phi(num_patients))
