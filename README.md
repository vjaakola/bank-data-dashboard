## Description


This is a demonstration of how to make interactive stock market graphs with Flask + Python + Pandas DataReader 
and put them into one dashboard using Python list [ ] -method append(). 
Codes for these graphs are in the GitHub link under the graphs and the text below. Happy data analysis!

If you are interested to understand the whole configuration, check these links from my GitHub repo: 

- [wrangle_data.py](https://github.com/VesaJ/bank-data-dashboard/blob/master/wrangling_scripts/wrangle_data.py)
- [index.html](https://github.com/VesaJ/bank-data-dashboard/blob/master/bankapp/templates/index.html)
- [routes.py](https://github.com/VesaJ/bank-data-dashboard/blob/master/bankapp/routes.py)

Here is a link to Herokuapp, where you can see the demo:
[Bank Data Dashboard](https://bank-data-demo.herokuapp.com)

### Instructions:
Read the Procfile, where you can check the requirements.

### How to run this project

- Fork files to local
- Make: python3 -m venv venv
- Activate: source venv/bin/activate
- Install: pip install flask pandas plotly gunicorn pandas_datareader
- cd web_app
- (venv)web_app: python bankapp.py 

### Author

Vesa Jaakola

### About
This project was raised as a curiosity on how to make interactive graphs with Flask. Learning materials were part of the Udacity's Data Scientist nanodegree program and Udemy's Learning Python for Data Analysis and Visualization, and Python for Data Science and Machine Learning Bootcamp.



### Acknowledgements
Must give credit to: 
- Udacity 
- Jose Portilla, Head of Data Science, Pierian Data Inc., for teaching methods
- Robert Siipola, Co-founder at Three Point Consulting, for overall mentoring in data science


