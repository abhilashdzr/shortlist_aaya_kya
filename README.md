# shortlist_aaya_kya
A Python program which takes your erp credentials as input and alerts in-case your name pops up in noticeboard ;)

# 2 points to remember
1. Python and pip must be installed in the system to run this
2. Credentials of erp must be put in correctly, otherwise it will pause at the erp login screen. Better look at the terminal then.

# How to run
1. Clone the repository ```git clone https://github.com/abhilashdzr/shortlist_aaya_kya.git```
2. Change to the directory ```cd shortlist_aaya_kya```
3. Install the requirements ```pip install -r requirements.txt``` . If you think this is a bullshit, you can turn on a virtual env.
4. Run the script ```python cdc_notice_scraper.py```


# What you can change 
1. Add a parameter other than username such as ```self.roll_no``` to check whether his/her shortlist has come. Your credentials are still needed.
2. You can change the time after which the program repeats
3. The tone of the alarm lol ;)
