# Stock Portfolio Tracker

A beginner Python program that estimates the value of a stock portfolio using manually entered share quantities and a small dictionary of example prices.

> The prices in this project are hardcoded examples. They are not live market prices or financial advice.

## Requirements

- Python 3

## Run the program

Open a terminal in this folder and run:

```bash
python stock_tracker.py
```

On some systems, use `python3 stock_tracker.py` instead.

Enter a stock symbol from the displayed list, then enter the number of shares. Type `done` when you have entered all your stocks. The program prints each holding's estimated value and the portfolio total.

## Change the example prices

Edit `STOCK_PRICES` near the top of `stock_tracker.py`. For example:

```python
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
}
```

## Upload to GitHub in your browser

1. Sign in at [github.com](https://github.com/).
2. Select **New repository** (or use the **+** menu and choose **New repository**).
3. Name it `stock-portfolio-tracker`, choose **Public** or **Private**, and select **Create repository**. Leave the initialize-with-README option unchecked because this folder already has a README.
4. On the new repository page, choose **Add file** → **Upload files**.
5. Upload `stock_tracker.py` and `README.md` from this folder, then select **Commit changes**.

## Upload with Git from a local folder

If Git is installed and this folder is not already a Git repository, open a terminal in it and run:

```bash
git init
git add stock_tracker.py README.md
git commit -m "Add stock portfolio tracker"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/stock-portfolio-tracker.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Create the empty GitHub repository first. If Git says a remote named `origin` already exists, check it with `git remote -v` instead of adding it again.
