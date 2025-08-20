import marimo

__generated_with = "0.14.17"
app = marimo.App(width="full", sql_output="polars")


@app.cell
def _(mo):
    mo.md("""# Title""")
    return


@app.cell
def cell1():
    x = 42
    return (x,)


@app.cell
def cell2(x):
    y = x + 1
    print("y =", y)
    return


@app.cell
def cell3():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
