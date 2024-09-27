# Project Overview

This project retrieves all PyPI download data for Kedro packages from the ClickHouse server `clickpy-clickhouse.clickhouse.com` and saves the data to Snowflake storage. The pipeline is built using Kedro to ensure efficient data processing and handling.

## Configuration Overview

This folder contains configuration files required by Kedro or other tools used in the project. Please follow the instructions below to ensure proper setup for local and base configurations.

### Local Configuration

The `local` folder should contain user-specific or sensitive configurations, such as security keys, credentials, or development environment settings.

> **Note:** Do not commit any files in the `local` folder to version control.

### Base Configuration

The `base` folder is intended for shared configuration that is non-sensitive and relevant to all team members working on the project. This might include project settings, non-sensitive environment variables, and shared resources.

> **WARNING:** Do not store any sensitive information, such as access credentials or private keys, in the `base` folder.

## Instructions

1. **Local Setup:**
   - Place your local configuration files, such as Snowflake credentials or ClickHouse access keys, in the `local` folder. 
   - Ensure these files are not tracked by version control to maintain security.
   
2. **Base Configuration Setup:**
   - Ensure that non-sensitive, shared configurations (e.g., database connection details without credentials) are stored in the `base` folder.
   
3. **Running the Project:**
   - After configuring the local environment with your credentials, run the Kedro pipeline to retrieve and save PyPI download data from ClickHouse to Snowflake.
   - Ensure your Snowflake instance is properly set up and the necessary tables are available for data storage.

## Need help?

For more detailed instructions on configuration and setup, refer to the [Kedro documentation](https://docs.kedro.org/en/stable/kedro_project_setup/configuration.html).