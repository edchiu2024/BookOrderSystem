from flask import Flask, request, jsonify
from bookstore import Bookstore
from factory import BookFactory
from ordermanager import OrderManager

app = Flask(__name__)
store = Bookstore()
ordermanager=OrderManager()


@app.route("/api/v1/orders", methods=['GET'])
def list_orders():
    try:
        orders=ordermanager.list_books()
        return jsonify(orders)
    except Exception as e:
        return jsonify({"error":f"{e}"}),500
    
@app.route("/api/v1/order", methods=['POST'])
def add_order():
    data=request.json
    order_id=data.get('order_id')
    customer_name=data.get('customer_name')
    total_amount=data.get('total_amount')
    items=data.get('items')

    try:
        ordermanager.add_order(order_id,customer_name,items,total_amount)
        return jsonify({'message':"order placed successfully"}), 201
    except ValueError as e:
        return jsonify({"error":f"something is wrong: {e}"}), 400
    except Exception as e:
        return jsonify({"error":f"something is wrong: {e}"}), 500



@app.route("/api/v1/books/search", methods=["GET"])
def search_books():
    try:
        title=request.args.get('title','')
        author_name=request.args.get('author_name','')

        if title:
            results=store.search_books_by_title(title)
        elif author_name:
            results=store.search_books_by_author(author_name)
        else:
            results=[]

        return jsonify(results)
    except Exception as e:
        return jsonify({"error":f"{e}"}),500
        

@app.route('/api/v1/books', methods=['GET'])
def list_books():
    try:
        books=store.list_books()
        return jsonify(books)
    except Exception as e:
        return jsonify({"error":f"{e}"}),500


@app.route('/api/v1/book', methods=['POST'])
def add_book():

    data=request.json
    book_type=data.get('type')
    author_name=data.get('author')
    title=data.get('title')
    price=data.get('price')
    extra_fields = {
        'weight': data.get('weight'),
        'file_size': data.get('file_size'),
        'duration': data.get('duration')
    }
    
    try:


        book=BookFactory.create_book(book_type, title, author_name, price, **extra_fields)

        store.add_book(book)
        return jsonify({"message": "Book added successfully!"}), 201
    except ValueError as e:
        return jsonify({"error": f"Incorrect input: {e}"}), 400
    except Exception as e:
        return jsonify({"error":f"something is wrong: {e}"}), 500


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)

