# app.py

from flask import Flask, render_template, request, redirect, url_for
from linkedlist import LinkedList

app = Flask(__name__)
ll = LinkedList()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    
    if request.method == 'POST':
        if 'add' in request.form:
            data = request.form.get('data', '').strip()
            if data:
                message = ll.append(data)

        elif 'delete' in request.form:
            try:
                index = int(request.form.get('index', 0))
                message = ll.delete_nth_node(index)
            except ValueError:
                message = "Please enter a valid number for deletion."

        elif 'refresh' in request.form:
            ll.__init__()  # Reinitialize the linked list
            return redirect(url_for('index'))  # Clear form and reload

    elements = ll.print_list()
    return render_template('index.html', elements=elements, message=message)

if __name__ == '__main__':
    app.run(debug=True)
