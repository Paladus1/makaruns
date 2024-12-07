@app.router('/')
def index():
    return render_template('insex.html')
@app route("/result")
def result():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM products").fetchal()
    return render_template(template_name_or_list: 'products.html',produts=cards)

    app.run(debug=True)