import mongodb_client as client

def test_basic():
    db = client.get_db('test')
    db.testCollection.drop()
    assert db.testCollection.count() == 0
    db.testCollection.insert({'test': 1, 'hello': 'world'})
    assert db.testCollection.count() == 1
    db.testCollection.drop()
    assert db.testCollection.count() == 0
    print 'test_basic passed.'

if __name__ == "__main__":
    test_basic()
