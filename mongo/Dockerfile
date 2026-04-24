FROM mongo:6.0
COPY init.js /docker-entrypoint-initdb.d/init.js
RUN chmod 644 /docker-entrypoint-initdb.d/init.js
USER mongodb
EXPOSE 27017
