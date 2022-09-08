from project.__init__ import db, create_tables

from project import create_app

app = create_app()
with app.app_context():
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    app.run()