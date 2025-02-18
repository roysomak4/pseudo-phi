from generator import generate_phi as gp

pdata = gp(num_patients=20)

for item in pdata:
    print(
        f"{item['firstname']}\t{item['lastname']}\t{item['minitial']}\t{item['dob']}\t{item['mrn']}\t{item['gender']}"
    )
