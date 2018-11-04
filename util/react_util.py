from db_connection import *
from models.reactions import Reaction
import re


def get_reacts(msg):
    keywords = session.query(Reaction.keyword, Reaction.url).all()
    matches = []

    for keyword in keywords:
        match = re.search(r"\b{}\b".format(keyword[0]), msg, re.IGNORECASE | re.M)
        if match:
            matches.append(keyword[1])
    if matches:
        return matches
