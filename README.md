## To Set-Up and Run

1. Check out this repository:

  `git clone git@github.com:nick-lefley-iw/br-iw.git`.

2. Change directory to `br-iw`.

3. Install dependencies from requirements.txt with `pip install -r requirements.txt`.

4. Run `python3 -m Source.order`.



## Contribution Requirements

+ **Keep code consistent** with mine, using PyCharm's inbuilt linter as a guide. 
+ Run all tests using `pytest -m tests`. Any failures will result in pull requests being rejected.


## Brief Code Breakdown

+ **order.py** contains the main code functionality, including the app start.
+ **classes.py** contains all classes.
+ **persistence_management.py** controls all communication with the .txt files.
+ **string_helpers.py** contains a library of useful string funtions, and table outputs for all displays.
+ **coffee.py** is not used!
