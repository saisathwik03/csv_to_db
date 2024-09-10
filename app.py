import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/databasetocsv'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/import-csv')
def import_csv():
    df = pd.read_csv('data.csv')

    for index, row in df.iterrows():
        record = Data(id=row['id'], name=row['name'], age=row['age'])
        db.session.add(record)
    db.session.commit()

    return 'CSV data imported successfully!'

if __name__ == '__main__':
    app.run(debug=True)
