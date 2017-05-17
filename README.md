# README

Attempting to recreate [http://csrankings.org/collab/](http://csrankings.org/collab/) with JCU researcher data

![Screenshot of site](img/screenshot.png)

## Explanation

* `collab/` contains the graph page from `csrankings.org` to populate with JCU data.

* `data-preparation` contains the sample data from `input/` into the python munging code `dumber.py` to create a the `nodes.csv` and `matrix.json` expected by D3.js in `output`.

## Getting Started

```shell

# run the python code
cd data-preparation
python dumber.py

# serve up the site
cd ../collab
npm install -g serve # feel free to use a different HTTP server like
serve
```
Open [http://localhost:3000](http://localhost:3000) in your browser and get hacking.


## Limitations

The D3.js chord viz seems to hit visual limits at < 1000 publications.  Note `if counter > 500:` currently used to limit.

## TODO

Get subsections of data for each school or year or something that appears 500 - 1000 rows to then toggle using Drop down select or something better.
