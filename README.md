# NUFORC Scrapy Project

This is a Scrapy project featuring a spider named "nuforc". It is designed to scrape records from the NUFORC (National UFO Reporting Center) website.

## Installation

This project requires Python 3.9+, Scrapy, and pandas. You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

Or conda:

```bash
conda env create -n scrape -f environment.yml
```

Or mamba:

```bash
mamba env create -n scrape -f environment.yml
```

Clone this repository using the following command:

```bash
git clone https://github.com/ndgigliotti/ufo-scrape.git
```

Navigate to the cloned directory:

```bash
cd /path/to/ufo_scrape
```

## Usage

To run the spider, use the following command from the root directory of the project:

```bash
scrapy crawl nuforc
```

By default, the scraped data is exported as a JSONlines file named with the current timestamp in UTC `yyyy-mm-ddThh-mm-ss.jsonl` in the `ufo-scrape/downloads/nuforc` directory. The output directory can be changed in the `ufo-scrape/ufo_scrape/settings.py` file.

## Spider Details

The spider navigates through the NUFORC website using the [reports indexed by event date page](https://nuforc.org/webreports/ndxevent.html). It follows links to monthly report pages, each of which contains a table of sighting reports. The spider uses Pandas to parse these tables into dataframes, converts the column names to snake case, adds the URL of the page and the year and month of the report to each row, and then yields the rows as dictionaries of data.

## Project Structure

The main project directory contains the following:

- `ufo_scrape/`: The Scrapy project directory.
  - `spiders/`: Contains the NuforcSpider script.
  - `utils.py`: Contains utility functions used by the spider, such as the snake_case function.
- `README.md`: This file.

## Future Enhancements

1. Add additional spiders to scrape data from other UFO reporting websites.
2. Handle potential errors when parsing tables with Pandas.
3. Expand the spider to scrape additional data from the NUFORC website.
4. Clean and validate the data in a Scrapy item pipeline.
5. Add unit tests.

## Issues and Contributions

For any issues, questions, or suggestions for improvements, please create an issue in the GitHub repository. Contributions to the project are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
