from db import db


class ItemsTags(db.Model):
    __table__="items_tags"

    id=db.Column(db.Integer,primary_key=True),
    