# Overview
Simple project to try to isolate race condition when doing externalbrowser auth to snowflake from docker using `snowflake-connector-python` library.

The `snowflake-connector-python` is installed as an editable path dependency.  You should be able to edit the source code directly in the folder to try various fixes.

# Run project

## Setup your environment variables
Copy the `.env.example` file to `.env` and set variables to match your settings

## Build
`./docker-build.sh`

## Run
`./docker-run.sh`

# Outstanding issues
1. Getting browser to open on host from code running in docker container
