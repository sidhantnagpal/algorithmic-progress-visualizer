# Algorithmic Progress Visualizer
Python Web Scraper &amp; Data Visualizer for keeping track and visualising Algorithmic Progress on various Online Judges (Codeforces, SPOJ, CodeChef, CSAcademy, HackerRank, HackerEarth, UVa).  

# Supported Platforms
Linux   
macOS   
       
# Setup
*Python 2 Version >= 2.7*   
     
*For Synaptic Package Manager*   
```bash
sudo pip install requests beautifulsoup4 matplotlib python-tk selenium pyvirtualdisplay xvfbwrapper    
sudo apt install xvfb    
```

*Download Chrome Driver for Linux, unzip it, and goto the containing folder*    
```bash
chmod +x chromedriver   
sudo cp chromedriver /usr/local/bin/   
```

*For macOS, use Command Line to install following libraries*     
`pip install requests beautifulsoup4 matplotlib python-tk selenium pyvirtualdisplay xvfbwrapper`      
(make sure `xvfb` is supported and install it)   
(download and install Chrome Driver to `/usr/local/bin`)    

# Execution
```bash
python scrape.py         
python pie.py   
```
*scrape - Fetch the data from different Online Judges and dump it to JSON file*    
*pie - Parse the JSON file and visualize it using a Pie Chart*    
       
# Sample
![alt text](https://github.com/sidhantnagpal/algorithmic-progress-visualizer/blob/master/sample/sample.png "Sample")

# How to Contribute?
Feel free to ping me via [email](mailto:sidhantnagpal97@gmail.com)! :)    
    
# License
MIT
