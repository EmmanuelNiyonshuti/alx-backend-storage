#a Dockerfile to set up enviromnment required.

# Use Ubuntu 18.04 LTS as the base image
FROM ubuntu:18.04

# Avoid prompts from apt during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install necessary software
RUN apt-get update \
    && apt-get install -y python3.7 python3-pip \
    curl \
    && apt-get install -y mysql-server-5.7 \
    && rm -rf /var/lib/apt/lists/*


# Set the MySQL root password
ENV MYSQL_ROOT_PASSWORD=root

# Initialize MySQL data directory (if needed)
# Ensure MySQL has the correct permissions
RUN mkdir -p /var/lib/mysql /var/run/mysqld \
    && chown -R mysql:mysql /var/lib/mysql /var/run/mysqld

# Expose MySQL port
EXPOSE 3306

# Start MySQL when the container launches
CMD ["mysqld_safe"]
