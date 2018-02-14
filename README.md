# Algorithmic Progress Visualizer
Python Web Scraper &amp; Data Visualizer for keeping track and visualising Algorithmic Progress on various Online Judges (Codeforces, SPOJ, CodeChef, CSAcademy, HackerRank, HackerEarth, UVa).   
    
# Setup
*Python Version >= 2.7*   
     
*For Synaptic Package Manager*   
sudo pip install requests beautifulsoup4 matplotlib python-tk selenium pyvirtualdisplay xvfbwrapper    
sudo apt install xvfb    
     
*Download Chrome Driver for Linux, unzip it, and goto the containing folder*    
chmod +x chromedriver   
sudo cp chromedriver /usr/local/bin/   
    
*For macOS or Windows, use Python Command Line to install following libraries*     
(download and install ChromeDriver)    
pip install requests beautifulsoup4 matplotlib python-tk selenium pyvirtualdisplay xvfbwrapper
(make sure xvfb is supported by your OS and install it)   
    
# Execution
*Fetch the data from different Online Judges and dump it to JSON file*    
python scrape.py     
    
*Parse the JSON file and visualize it using a Pie Chart*    
python pie.py
