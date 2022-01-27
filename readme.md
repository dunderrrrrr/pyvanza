
# Py(A)vanza

Fetch fund data from [avanza.se](https://avanza.se/) using Python and some web scraping with bs4.  The default way is to display the data in the terminal, apply `--json` for json output.

![Tux, the Linux mascot](https://i.imgur.com/g7bMnFa.png)

### How does it work?

Provide this script with the `fund id` (can be found in the url of the fund, example below). The script is scraping the funds page and displays the output.

### How is this useful?

You can use this data for your own project, perhaps on a Raspberry Pi with a display?

### Installation

We're going to use selenium with chrome driver for this one. So apt install `chromium-chromedriver` and `xvfb`.
```
$ sudo apt install chromium-chromedriver
$ sudo apt install xvfb
```

Next, clone repo and install requirements (preferably inside a virtualenv of some sort).
```
$ git clone <url>
$ mkvirtualenv pyvanza
$ pip install -r requirements.txt
```
Grab the `fund id` from url. In this case the id is `325406`.  

**URL:** https://www.avanza.se/fonder/om-fonden.html/325406/spiltan-aktiefond-investmentbolag  

### Running script

| Argument | Required |  Description  |  
|---|---|---|
| `id`  | Yes  | Fund id is mandatory  |
| `--json`  | No  | Output will be in json format  |
| `--nocolors`  | No  | Terminal colors will be disabled  |

```
(pyvanza) user@host:~ $ python pyvanza.py 693994
┌──────────────────────────────────────┐
│  Spiltan Globalfond Investmentbolag  │
└──────────────────────────────────────┘
┌──────┬─────────┐
│ Time │ Change  │
├──────┼─────────┤
│ 1 m. │ −2,82%  │
│ 3 m. │ +1,54%  │
│ i år │ −3,84%  │
│ 1 år │ +26,21% │
│ 3 år │ +55,97% │
│ 5 år │ +70,65% │
│ Max  │ +87,05% │
└──────┴─────────┘
```
```
(pyvanza) user@host:~ $ python pyvanza.py 693994
{
  'title': ' Spiltan Globalfond Investmentbolag ',
  'data': {
     '1 m.': '−2,82%',
     '3 m.': '+1,54%',
     'i år': '−3,84%',
     '1 år': '+26,21%',
     '3 år': '+55,97%',
     '5 år': '+70,65%',
     'Max': '+87,05%'
 }
}
```
