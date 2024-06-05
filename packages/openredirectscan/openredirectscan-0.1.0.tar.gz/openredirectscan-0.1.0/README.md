

<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/openredirect.png" alt="logo">
</div>


## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)(https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/openredirect)
![PyPI - Downloads](https://img.shields.io/pypi/dm/openredirect)
<p align="center">

<p align="center">





## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install open_redirect_scan 
        ```
   - Run bellow command to check
     - `openredirectscan -h`

## Usages 
2. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          openredirectscan -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          openredirectscan -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          openredirectscan -i urls.txt -o out.txt
        ```
   - Want to Learn about [`openredirect`](https://blogs.cappriciosec.com/application/143/Open%20Redirection%20-%20A%20Deceptive%20Detour%20for%20Users%20and%20a%20Vulnerability%20for%20Applications)? Then Type Below command
      - ```bash
          openredirectscan -b
        ```
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Help menu

#### Get all items

```bash
    Hey Hacker
                                             v1.0


   ______                  _       _
  / _____)                (_)     (_)
 ( (____   ____ ____ ____ _ ____  _ ____   ____
  \____ \ / ___) _  |  _  | |  _ \| |  _ \ / _  |
  _____) | (  ( ( | | | | | | | | | | | | ( (_| |
 (______/ \____)_||_|_| |_|_|_| |_|_|_| |_|\___ |
                                           (____/                                                



openredirectscan : Bug scanner for WebPentesters and Bugbounty Hunters 

$ openredirectscan [option]

Usage: openredirectscan [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | openredirectscan -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | openredirectscan -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | openredirectscan -i target.txt -o output.txt |
| `-b` | `--blog` | To Read about openredirect Bug | openredirectscan -b |
| `-h` | `--help` | Help Menu | openredirectscan -h |


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]




