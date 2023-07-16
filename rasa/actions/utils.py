from connection import get_database


def find_examples():
    dbname = get_database()

    # Retrieve a collection named "user_1_items" from database
    collection_name = dbname["examples"]


    item_details = collection_name.find()
    for item in item_details:
        # This does not give a very readable output
        print(item)