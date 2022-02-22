# Speedtest to MySQL

Docker image (or Python script) to save internet speedtest into MySQL database.

## Installation

### Build from source code

1. Download source code
2. Edit Dockerfile to change local variables
    | Variable      | Default value     | Description           |
    | ------------- | ----------------- | --------------------- |
    | DB_HOST       | host              | Ip of db host         |
    | DB_PORT       | port              | db port               |
    | DB_USER       | user              | db user               |
    | DB_PASSWD     | pwd               | db password           |
    | DB_DATABASE   | db                | db name               |
    | TIME          | 1800              | time between tests    |
2. Build Docker image
    ```
    docker build --tag speedtest .
    ```
3. Create container
    ```
    docker create --name Speedtest speedtest
    ```
4. Start container
    ```
    docker start Speedtest
    ```
In some distributon, like Synology DSM, you must execute the commands above with `sudo`.

### Using Docker image from DockerHub

1. Dowload Docker image from [DockerHub](https://hub.docker.com/r/fantinialex/speedtest-to-mysql)
    ```
    docker pull fantinialex/speedtest-to-mysql
    ```
2. Create a new container
    ```
    docker create --name Speedtest fantinialex/speedtest-to-mysql
    ```
3. Edit local variables value
    | Variable      | Default value     | Description           |
    | ------------- | ----------------- | --------------------- |
    | DB_HOST       | host              | Ip of db host         |
    | DB_PORT       | port              | db port               |
    | DB_USER       | user              | db user               |
    | DB_PASSWD     | pwd               | db password           |
    | DB_DATABASE   | db                | db name               |
    | TIME          | 1800              | time between tests    |
4. Start container
    ```
    docker start Speedtest
    ```

## Faq

**Why you memorize the ISP?**
This script is designed for a network with redoundance connection, so the easy way to know what connection is active is saving the Isp name.

## Visualization

Do you want to easy view this datas? You can use Grafana (coming soon ;)).

## Resources
* [Speedtest-cli](https://github.com/sivel/speedtest-cli/wiki)