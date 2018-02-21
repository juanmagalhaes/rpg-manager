FROM postgres:10.1-alpine
COPY create_db.sh ./docker-entrypoint-initdb.d/
EXPOSE 5432
CMD ["postgres"]
