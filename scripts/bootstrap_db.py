# Run this script to bootstrap the database with seed data for the app. You will
# need to provide a seed csv file w/ appropriate fields located at base dir.
# It will always aim to bring up a clean database with the provided seed data
# regardless of what state it was run.

# Based on Pyramid default initializedb.py script.
# github.com/Pylons/pyramid/blob/master/pyramid/scaffolds/alchemy/+package+/scripts/initializedb.py

import os
import sys
import csv
import transaction

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars

from springboard.models import Base, sess
from springboard.models import Product, Vendor, User, Board


def main(argv=sys.argv):
    if len(argv) < 2:
        cmd = os.path.basename(argv[0])
        print("You are doing it wrong.\n"
              'usage: %s <config_uri> [var=value]\n'
              '(example: "%s development.ini")' % (cmd, cmd)
        )
        sys.exit(1)

    # Parse and merge passed args and config ini file.
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    settings = get_appsettings(config_uri, options=options)

    # Ensure we have a database url set.
    db_url = settings.get("sqlalchemy.url")
    if not db_url:
        print("You need to configure sqlalchemy.url to connect to postgres.")

    # Ensure we have a seed file to bootstrap to begin with.
    seedfile = settings.get("springboard.seedfile")
    is_seedfile_given = bool(seedfile)
    is_seedfile_found = os.path.isfile(seedfile) if seedfile else False
    if not is_seedfile_given or not is_seedfile_found:
        print("You need to provide a csv file for seed data.")
        sys.exit(1)

    # Drop the existing database if we already have one; if not create new one.
    # Either way start with a clean slate.
    engine = create_engine(db_url)
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

    # Create all tables based on defined model classes.
    sess.configure(bind=engine)
    Base.metadata.create_all(engine)

    # Import data from the seed file while mapping appropriate relationships.
    with transaction.manager:
        with open(seedfile) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Get or create vendor.
                vendor_id = row["vendor_id"]
                vendor = sess.query(Vendor).get(vendor_id)
                if not vendor:
                    vendor = Vendor(id=vendor_id, name=row["vendor_name"])
                    sess.add(vendor)
                    sess.flush()

                # Get or create product
                product_id = row["product_id"]
                product = sess.query(Product).get(product_id)
                if not product:
                    # XXX: Ignore taxonomy hierarchy and track only the top
                    # most level as 'category' in products table for simplicity.
                    taxonomies_list = row["backend_taxonomy"]
                    category = taxonomies_list.strip("{}").split(",")[0]
                    category = category or "unassigned"

                    product = Product(id=product_id,
                                      name=row["product_name"],
                                      description=row["product_desc"],
                                      original_price=row["original_price"],
                                      latest_price=row["price"],
                                      is_on_sale=row["is_on_sale"],
                                      targeted_gender=row["gender"].strip().lower(),
                                      category=category,
                                      photo_url=row["photo_url"],
                                      created_at=row["created_at"])
                    product.vendor_id = vendor.id
                    sess.add(product)
                    sess.flush()

        # Create dummy user and board.
        # XXX: Limit the prototype app to one user, and only one board per user.
        user = User(name="Chaz")
        sess.add(user)
        sess.flush()

        board = Board(name="2015W", description="Winter 2015 Favorites")
        board.user_id = user.id
        sess.add(board)
        sess.flush()

    print("All done!")


if __name__ == "__main__":
    main()
