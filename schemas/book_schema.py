def individual_serializer(book) -> dict:
        return {
        "id": str(book["_id"]),
        "name": str(book["name"]),
        "synopsis": str(book["synopsis"]),
        "price": float(book["price"]),
        "author": str(book["author"]),
        "genre": str(book["genre"]),
        "publication_date": str(book["publication_date"]),
        "rating": int(book["rating"])
    }

def list_serializer(books) -> list:
    try:
        list_serialized = [individual_serializer(book) for book in books]
        return list_serialized
    except Exception as e:
        print(e)
