# Fastapi example with SQLModel

This project created with Fastapi and SQLModel libraries
you can use it as a reference for main endpoints and for learning purpose

## Get started

You can use this project as beginners ( learning purpose only ) template

- Install the requirements

```bash
  pip install -r requirements.txt
```

- Run database file to create the database

```bash
  python database.py
```

- Run the next code to start the fastapi server

```bash
  uvicorn main:app --reload
```

- Go to localhost url to test the server (API)

```bash
  http://127.0.0.1:8000/docs/

  or

  localhost:8000/docs/
```

## Acknowledgements

Read the docs to get familiar with these libraries

- [Fastapi docs](https://fastapi.tiangolo.com/)
- [SQLModel docs](https://sqlmodel.tiangolo.com/)
