# FastAPI Exercise Using Pydantic

This project is an exercise in using **FastAPI** along with **Pydantic** for creating a simple API. The goal of the project is to demonstrate how to define and validate data models using Pydantic, and how to integrate them into a FastAPI-based application.

## Features

- **FastAPI**: Utilizes the FastAPI framework for building high-performance APIs.
- **Pydantic Models**: Uses Pydantic for data validation and serialization.
- **CRUD Operations**: Demonstrates basic CRUD operations (Create, Read, Update, Delete) using FastAPI endpoints.
- **Automatic Docs**: FastAPI generates interactive documentation using Swagger UI.

## Requirements

- **Python 3.x**
- **FastAPI**: The web framework used for building the API.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server to run the FastAPI app.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/FasyApi_Exercise_Using_Pydanic.git
    cd FasyApi_Exercise_Using_Pydanic
    ```

2. **Install Dependencies:**

    You can install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the API:**

    To start the FastAPI server, use the following command:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the API at `http://127.0.0.1:8000`.

4. **Access the API Documentation:**

    FastAPI automatically generates Swagger UI documentation for your API at `http://127.0.0.1:8000/docs`.

### Project Structure

- `main.py`: Contains the FastAPI app and routes.
- `models.py`: Contains Pydantic models for data validation.
- `requirements.txt`: Lists the required Python packages.

### Example Usage

- **Create Item**: Send a POST request to `/items/` with a JSON body containing item data.
  
    Example:

    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/items/' \
      -H 'Content-Type: application/json' \
      -d '{
      "name": "Item Name",
      "description": "Item Description",
      "price": 100.0
    }'
    ```

- **Get Items**: Send a GET request to `/items/` to retrieve all items.

    Example:

    ```bash
    curl 'http://127.0.0.1:8000/items/'
    ```

- **Update Item**: Send a PUT request to `/items/{item_id}/` to update an existing item.

- **Delete Item**: Send a DELETE request to `/items/{item_id}/` to delete an item.

## Contributing

Feel free to fork the repository and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
