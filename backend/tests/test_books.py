def test_create_and_get_book(client):
    response = client.post(
        "/books/",
        json={
            "title": "Test Book",
            "author": "Tester",
            "total_copies": 2,
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["available_copies"] == 2

    detail = client.get(f"/books/{data['id']}")
    assert detail.status_code == 200
    assert detail.json()["author"] == "Tester"


def test_rejects_invalid_copy_count(client):
    response = client.post(
        "/books/",
        json={
            "title": "Bad Book",
            "author": "Tester",
            "total_copies": 0,
        },
    )

    assert response.status_code == 422


def test_missing_book_returns_404(client):
    response = client.get("/books/999")

    assert response.status_code == 404
