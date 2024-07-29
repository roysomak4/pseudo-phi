# pseudo-phi
This simple python app generates fictious patient information for healthcare software development and testing.

### System requirement
Python >=3.10

### How to use
1. Clone the repository
   ```bash
   git clone https://github.com/roysomak4/pseudo-phi.git
   cd pseudo-phi
   ```
2. For quick test run `python3 test.py`. This should output a list of dictionaries of 4 random patient records in `stdout`.
3. This is meant to be used as a module in apps. An example is below

```python
from generator import generate_phi

patients: list = generate_phi(num_patients=4)

..... Do something with the patient records..... 

``` 
4. The application currently generates random names using characters from Star Wars and Harry Potter movie series! Date of birth and MRN are completely random. This provides an easy way to generate a large number of patient records for development and testing of healthcare software without compromising data privacy and security regulations in healthcare.

The `names.txt` file is the source of the names. You can replace that with any list of names of your choice as long as the data structure is preserved.