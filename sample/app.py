from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize empty list to store books
books = []

# Routes for CRUD operations
@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    author = request.form['author']
    publisher = request.form['publisher']
    cost = int(request.form['cost'])
    book = {"id": len(books) + 1, "title": title, "author": author, "publisher": publisher, "cost": cost}
    books.append(book)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    global books
    books = [book for book in books if book['id'] != id]
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return render_template('edit.html', book=book)
    else:
        return 'Book not found', 404

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['publisher'] = request.form['publisher']
        book['cost'] = int(request.form['cost'])
        return redirect(url_for('index'))
    else:
        return 'Book not found', 404

if __name__ == '__main__':
    app.run(debug=True)
