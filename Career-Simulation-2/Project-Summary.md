# Project Summary

## Explanation of Files

- [Career-Simulation-2.pbix](/Career-Simulation-2/Career-Simulation-2.pbix) is the PowerBI file with visuals
- [data-schematics.png](/Career-Simulation-2/data-schematics.png) is a screenshot of the database schema in PowerBI (and SQL)
- [Queries.sql](/Career-Simulation-2/Queries.sql) is a collection of SQL queries used to clean, sort, and aggregate the raw data.

## Dataset

- The dataset is pulled from [here](https://www.kaggle.com/datasets/yapwh1208/supermarket-sales-data)
- Code discussions [here](https://www.kaggle.com/datasets/yapwh1208/supermarket-sales-data/code)

## Findings

A number of kery findings with this analysis will allow managers to better staff, shelve, and monitor sales in the store. Firstly, the highest client volume (by sales) is in the morning, presumably before work. Many clients are probably repeat customers and know what they need at this time (since they are on a schedule) and number of available cashiers should take precednece over number of employees on the shop floor.

There is a minor lunch rush to purchase produce, but not one that warrants staffing changes. In the evenings, the "rush" is more drawn out, so suffficient staffing should be priority. Based on sales volume, the highest sales are generated just after the top of every hour. Because of this, shifts should start and end on the bottom of the hour (say, 8:30am to 3:30pm) to avoid shift changes during rush times.

Capsicum (peppers) are by far and away the most popular category of product. The peppers should be mainly stocked in the front of the store for easy customer access. A couple of high-selling peppers should be showcased in the back of the store though, to increase customer time in-store and thus increase the probability of buying other products. Any seasonal produce (such as produce typically bought in preparation for a certain holiday) should be strategically placed as well.

Customer habits by day of the month show a clear spike in the middle, after the 15th of the month (payday for many, presumably). Stocking the store fully before this monthly rush should be top priority for management, to minimize sales lost due to not having the product in stock.

## Further Research

A deep-dive into price changes (highlighted in the "Price Lookups" tab) and their effect on sales would be in order, but this is beyond a simple sales analysis. One could plot % change in price vs. % change in sales, binned by week, perhaps, so see if customers are responding to price changes with purchase behaviors. Of course, the presence of lurking variables (seasonal, holidays) may restrict the usefulness of this analysis a bit.

## Summary

Business recommendations are as follows:

- Shifts start and end at the bottom of the hour.
- Highest staffing for cashiers in the morning, stockers in the evening.
- Consistent number of floor sales associated throughout the day.
- Continued logging of all of this data after each reccomended change to view effectiveness.
- For convenience, put half of the highest selling peppers in the front for easy access and spread the rest around the store to maximize customer time-in-store.
- Schedule biggest restockings two or three days before the middle and the end of each month (ensures fresh produce in preparation for highewst customer sales volume).
