
# DjangoConjuror

DjangoConjuror is a command-line tool designed to simplify Django project setup and management. It allows developers to quickly create new projects, add applications, configure databases, and more, using straightforward commands.

## Features

- **Create Django Projects**: Initialize a new Django project at a specified location with a custom project name.
- **Add Django Apps**: Easily add one or more applications to your Django project.
- **Database Configuration**: Change the default database settings to use PostgreSQL, MySQL, or SQLite.
- **Setup Static and Templates**: Automatically set up directories for static files and templates.
- **CRUD Operations**: Import CRUD functionalities to perform create, read, update, and delete operations easily within your Django apps.

## Installation

You can install DjangoConjuror using pip:

```bash
pip install DjangoConjuror
```

## Usage

Here is how you can use DjangoConjuror to manage your Django projects:

### Create a New Project

To create a new Django project:

```bash
conjuror --create --path /path/to/project --name myproject
```

- `--create`: Initiates the creation of a new Django project.
- `--path`: Specifies the directory where the project will be created.
- `--name`: Sets the name of the new Django project (defaults to "myproject" if not specified).

### Add Applications

To add applications to your Django project:

```bash
conjuror --apps app1 app2 app3
```

This command adds the specified apps to your Django project.

### Setup Static and Template Directories

To set up directories for static files and templates:

```bash
conjuror --setup-static-templates
```

### Configure Database

To configure the database settings for your Django project:

```bash
conjuror --database --dbtype postgres --username user --password pass --dbname dbname --host localhost --port 5432
```

- `--database`: Enables database configuration.
- `--dbtype`: Specifies the type of database (postgres, mysql, sqlite).
- `--username`: Database username.
- `--password`: Database password.
- `--dbname`: Database name.
- `--host`: Database host (defaults to "localhost").
- `--port`: Database port.

### CRUD Operations

To use CRUD operations in your Django app, import the CRUD functionality provided by DjangoConjuror:

```python
from conjuror.Crud import crud

# Example usage
crud.StoreData(model,dict)
crud.FetchData(model,dict)
crud.UpdateData(model,filters,dict)
crud.DeleteData(model,dict)
crud.GetData(model,dict)
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to improve the functionality of DjangoConjuror.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.