# Reversed Polish Notation calculator - backend

Backend part of the project.

Unit test are performed during the docker container build.

- API Created using fastapi
- SQLAlchemy used for persistence (sqlite database)


exposed URLs:

- http://localhost:8000/docs (API documentation, provided by FastAPI)
- http://localhost:8000/process (POST endpoint to send the expressions to process)
- http://localhost:8000/calculations (GET endpoint, will return a CSV file)

```
curl --location 'http://localhost:8000/process' \
--header 'Content-Type: application/json' \
--data '{
    "expression": "1 2 + 3 4 + *"
}'
```

