# Calculator Web Application

This project is a simple web-based calculator built using Flask. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division through a graphical user interface.

## Project Structure

```
calculator-web-app
├── app.py              # Main entry point of the web application
├── calculator.py       # Contains arithmetic functions
├── templates
│   └── index.html      # HTML template for the user interface
├── static
│   └── style.css       # CSS styles for the web application
└── README.md           # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd calculator-web-app
   ```

2. **Install the required packages**:
   Make sure you have Python and pip installed. Then, run:
   ```
   pip install Flask
   ```

3. **Run the application**:
   Execute the following command in your terminal:
   ```
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

- Enter the first number and the second number in the provided input fields.
- Select the desired arithmetic operation (Add, Subtract, Multiply, Divide).
- Click the "Calculate" button to see the result displayed on the page.

## License

This project is open-source and available under the MIT License.