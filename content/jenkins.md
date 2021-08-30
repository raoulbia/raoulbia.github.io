Title: Jenkins
Date: 2018-01-06
Category: CI
Slug: jenkins
Summary: Jenkins

<br> 

#### Useful commands

* `sudo systemctl restart jenkins`
* `dpkg -L jenkins` will help you find what files the package installed


#### Build Periodically

```
# MINUTE (0-59), HOUR (0-23), DAY (1-31), MONTH (1-12), DAY OF THE WEEK (0-6)
# weekday daily build twice a day, at _ and _ , Monday to Friday:
H 10,17 * * 1-5
```

#### Build: Execute Windows Batch Command

```
call C:\Users\Raoul.Biagioni\Miniconda3\Scripts\activate.bat C:\Users\Raoul.Biagioni\Miniconda3
call conda activate gtfsRT
#pip freeze
python C:\\Users\\<FirstName.LastName>\\<path-to-file>\\scriptname.py
```

#### Misc.

* [Set up Jenkins](https://phoenixnap.com/kb/install-jenkins-ubuntu)
* [Disable Jenkins password](https://stackoverflow.com/a/28906663)
