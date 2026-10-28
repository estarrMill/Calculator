# Tkinter Calculator

A simple desktop calculator built with Python and **Tkinter**. It shows a window with clickable buttons and a display screen, similar to a basic handheld calculator.

Developed in **Visual Studio Code.**

## Features

- Addition (`+`), subtraction (`-`), multiplication (`*`) and division (`/`)
- Modulo (`%`), which gives the remainder of a division
- Decimal numbers (`.`)
- `=` button to calculate the result
- `C` button to clear the display
- Shows `Error` instead of crashing on invalid input (e.g. dividing by zero)
- Fixed-size window with a right-aligned display

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)

To check that Tkinter is installed, run:

```
python -m tkinter
```

A small test window should appear.

## How to Run

1. Clone the repository:

   ```
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```

2. Run the program:

   ```
   python calculator.py
   ```

   Or open the folder in VS Code and click the **Run** button.

**How to Use**

1. Click the number buttons to enter a value.
2. Click an operator (`+`, `-`, `*`, `/`, `%`).
3. Enter the next number.
4. Click `=` to see the result.
5. Click `C` to clear and start again.

Example: `12 * 3 =` → `36`

**How It Works**

- `tk.Entry` is the display screen at the top of the window.
- Buttons are created in a loop and placed in a 4-column grid using `.grid()`.
- Each button calls the `press()` function with its own label.
- When `=` is pressed, the expression on the display is calculated with Python's `eval()` function.
- A `try/except` block catches any errors and shows `Error` on the display.

**Project Structure**

```
├── calculator.py   # Main program
└── README.md       # Project documentation
```

**Known Limitations**

- The `,` and `X` buttons are not yet functional for calculations. Use `*` for multiplication.
- `%` performs modulo (remainder), not percentage.
- The calculator uses `eval()`, which runs any Python expression typed into the display. That's fine for a personal learning project, but `eval()` should never be used on untrusted input in real applications.

**Future Improvements**

- Add keyboard input support
- Add a backspace (delete last digit) button
- Add a percentage function
- Improve the button layout and colours



~~ Author ~~

**Oluwabiyi Bukola Esther**

~~ License ~~

This project is open source and available under the (MIT License).
