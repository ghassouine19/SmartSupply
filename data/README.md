# Data

This directory contains the data used by SmartSupply.

## Structure

- `samples/` - Small datasets used for development and testing.
- `raw/` - Raw source data.
- `bronze/` - Raw ingested data stored in the data lake.
- `silver/` - Cleaned and transformed data.
- `gold/` - Business-ready datasets and ML features.

Large datasets are intentionally excluded from Git.

The project uses public datasets such as:

- M5 Forecasting dataset for demand forecasting.
- DataCo Smart Supply Chain dataset for logistics analytics.

See the project documentation for dataset sources and preparation steps.