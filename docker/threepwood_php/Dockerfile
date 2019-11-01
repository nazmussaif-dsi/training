FROM composer AS composer

FROM php:7.2-cli
RUN apt-get update && apt-get install -y zip unzip
COPY --from=composer /usr/bin/composer /usr/bin/composer
WORKDIR /usr/src/app
COPY php ./
RUN composer install
EXPOSE 8181
CMD php artisan serve --host=0.0.0.0 --port=8181


