# ListOps Expression calculator

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

A simple command-line tool written in Python to evaluate LISP-like mathematical expressions operating on lists of integers.

## Features

* Parses and evaluates expressions with nested operations.
* Supports common aggregation functions: `SUM`, `MIN`, `MAX`, `AVG` (integer average), `MED` (lower median).
* Includes a custom operator `SM` (Sum Modulo 10).
* Clear error handling for invalid expressions or unknown operators.
* Pure Python, uses only standard libraries.

## Requirements

* **Python 3.x** (Uses `statistics.median_low` introduced in Python 3.4 and f-strings common in 3.6+)

## Installation

No special installation is required beyond having Python 3. Clone the repository or download the script file (`listops_calculator.py`).

1.  **Clone the repository (optional):**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git) # Replace with your repo URL
    cd your-repo-name
    ```
2.  **Or download the script:**
    Simply download the `listops_calculator.py` file to your local machine.

## Usage

Run the script from your terminal using `python listops_calculator.py`. It will prompt you to enter an expression. Type your expression and press Enter to see the result.

**Example Sessions:**

* **Basic Sum with Nesting:**
    ```bash
    $ python listops_calculator.py
    Enter ListOps expression: (SUM 10 20 (MAX 1 5 3))
    Result: 35
    ```

* **Median:**
    ```bash
    $ python listops_calculator.py
    Enter ListOps expression: (MED 1 5 2 8 3)
    Result: 3
    ```

* **Sum Modulo 10 with Nesting:**
    ```bash
    $ python listops_calculator.py
    Enter ListOps expression: (SM (AVG 10 11 12) 5)
    Result: 6
    ```

* **Error Handling:**
    ```bash
    $ python listops_calculator.py
    Enter ListOps expression: (SUB 10 5)
    Error evaluating expression: Unknown operator: SUB
    ```

## Expression Syntax

Expressions follow a LISP-like prefix notation:

* An expression is either an integer literal (e.g., `10`, `-5`) or an operation.
* An operation starts with an opening parenthesis `(`, followed by an operator name (uppercase letters), one or more arguments (which can be integers or nested operations), and a closing parenthesis `)`.
* Example: `(OPERATOR arg1 arg2 ... argN)`

## Supported Operators

| Operator | Description | Example Input | Output |
| :------- | :---------- | :------------ | :----- |
| `SUM` | Calculates the sum of all arguments. | `(SUM 1 2 3 -5)` | `1` |
| `MIN` | Finds the minimum value among the arguments. | `(MIN 10 5 8 20)` | `5` |
| `MAX` | Finds the maximum value among the arguments. | `(MAX 10 5 8 20)` | `20` |
| `AVG` | Calculates the integer average (floor division).   | `(AVG 10 11 12)` | `11` |
| `MED` | Finds the lower median of the arguments. | `(MED 1 5 2 8 3)` | `3` |
| `SM`  | Calculates the sum of arguments modulo 10. | `(SM 7 8 9)` | `4` |

## Nested Expressions

Operators can be nested to create more complex calculations:

* `(MAX 10 (SUM 1 2 3))` evaluates `(SUM 1 2 3)` first (result is `6`), then evaluates `(MAX 10 6)`, resulting in `10`.
* `(AVG (MIN 1 5) (MAX 10 20) 3)` evaluates `(MIN 1 5)` (result `1`), evaluates `(MAX 10 20)` (result `20`), then evaluates `(AVG 1 20 3)`, resulting in `(1+20+3)//3 = 24//3 = 8`.

## How It Works (Briefly)

1.  **Tokenization:** The input string is split into meaningful units (tokens) like parentheses `(`, `)`, operators (`SUM`, `MAX`, etc.), and numbers (`-10`, `5`). This uses regular expressions.
2.  **Parsing:** The script recursively parses the token stream. When it encounters an opening parenthesis `(`, it expects an operator followed by arguments. It parses each argument (which could trigger further recursive calls for nested expressions) until it finds a closing parenthesis `)`.
3.  **Evaluation:** Once an operator and its evaluated arguments are identified, the corresponding function (`sum`, `min`, `max`, etc.) is applied, and the result is returned up the recursion chain.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
