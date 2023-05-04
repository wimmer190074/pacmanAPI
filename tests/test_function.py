import pytest
from Pathfinder import Database, PostOffice, Edge, PathFinder


@pytest.fixture(scope='module')
def db():
    db = Database()
    yield db
    db.engine.dispose()

@pytest.fixture(scope='module')
def pf():
    pf = PathFinder()
    yield pf
    pf.db.engine.dispose()

def test_create_post_office(db):
    # Test creating a new post office in the database
    post_office = db.create_post_office('PO1', 'location1')
    assert isinstance(post_office, PostOffice)
    assert post_office.name == 'PO1'
    assert post_office.location == 'location1'
    db.delete_post_office(post_office.id)

def test_create_edge(db):
    # Test creating a new edge between post offices in the database
    start_post_office = db.create_post_office('PO2', 'location2')
    end_post_office = db.create_post_office('PO3', 'location3')
    edge = db.create_edge(start_post_office.name, end_post_office.name, 5.5)
    assert edge is not None
    db.delete_edge(start_post_office.id)
    db.delete_post_office(end_post_office.id)

def test_get_all_post_offices(db):
    # Test retrieving all post offices from the database
    post_office1 = db.create_post_office('PO4', 'location4')
    post_office2 = db.create_post_office('PO5', 'location5')
    post_offices = db.get_all_post_offices()
    assert isinstance(post_offices, list)
    assert len(post_offices) >= 2
    db.delete_post_office(post_office1.id)
    db.delete_post_office(post_office2.id)

def test_get_post_office_by_id(db):
    # Test retrieving a post office by its id from the database
    post_office = db.create_post_office('PO6', 'location6')
    retrieved_post_office = db.get_post_office_by_id(post_office.id)
    assert isinstance(retrieved_post_office, PostOffice)
    assert retrieved_post_office.id == post_office.id
    db.delete_post_office(post_office.id)

def test_get_post_office_by_name(db):
    # Test retrieving a post office by its name from the database
    post_office = db.create_post_office('PO7', 'location7')
    retrieved_post_office_id = db.get_post_office_by_name('PO7')
    assert isinstance(retrieved_post_office_id, int)
    assert retrieved_post_office_id == post_office.id
    db.delete_post_office(post_office.id)

def test_get_all_edges(db):
    # Test retrieving all edges from the database
    edge1 = db.create_edge('PO8', 'PO9', 2.5)
    edge2 = db.create_edge('PO10', 'PO11', 3.5)
    edges = db.get_all_edges()
    assert isinstance(edges, list)
    assert len(edges) >= 2
    db.delete_edge(edge1.start)
    db.delete_edge(edge2.start)

def test_get_edge_by_id(db):
    # Test retrieving an edge by its id from the database
    edge = db.create_edge('PO12', 'PO13', 4.5)
    retrieved_edge = db.get_edge_by_id(edge.id)
    assert isinstance(retrieved_edge, Edge)
    assert retrieved_edge.id == edge.id
    db.delete_edge(edge.start)

def test_update_post_office(db):
    # Test updating a post office in the database
    post_office = db.create_post_office('PO14', 'location14')
    updated_post_office = db.update_post_office(post_office.id, name='PO15', location='location15')
    assert isinstance(updated_post_office, PostOffice)
    assert updated_post_office.id == post_office.id
    assert updated_post_office.name == 'PO15'
    assert updated_post_office.location == 'location15'
    db.delete_post_office(updated_post_office.id)

def test_update_edge(db):
    # Test updating an edge in the database
    start_post_office = db.create_post_office('PO16', 'location16')
    end_post_office = db.create_post_office('PO17', 'location17')
    edge = db.create_edge(start_post_office.name, end_post_office.name, 6.6)
    updated_edge = db.update_edge(edge.id, weight=7.7)
    assert isinstance(updated_edge, Edge)
    assert updated_edge.id == edge.id
    assert updated_edge.weight == 7.7
    db.delete_edge(updated_edge.start)

def test_delete_post_office(db):
    # Test deleting a post office from the database
    post_office = db.create_post_office('PO18', 'location18')
    db.delete_post_office(post_office.id)
    deleted_post_office = db.get_post_office_by_id(post_office.id)
    assert deleted_post_office is None

def test_delete_edge(db):
    # Test deleting an edge from the database
    start_post_office = db.create_post_office('PO19', 'location19')
    end_post_office = db.create_post_office('PO20', 'location20')
    edge = db.create_edge(start_post_office.name, end_post_office.name, 8.8)
    db.delete_edge(edge.id)
    deleted_edge = db.get_edge_by_id(edge.id)
    assert deleted_edge is None

def test_shortest_path(pf):
    # Test finding the shortest path between post offices
    po1 = pf.db.create_post_office('PO21', 'location21')
    po2 = pf.db.create_post_office('PO22', 'location22')
    po3 = pf.db.create_post_office('PO23', 'location23')
    pf.db.create_edge(po1.name, po2.name, 2.0)
    pf.db.create_edge(po2.name, po3.name, 3.0)
    path = pf.find_shortest_path('PO21', 'PO23')
    assert isinstance(path, list)
    assert len(path) == 3
    assert path[0].name == 'PO21'
    assert path[1].name == 'PO22'
    assert path[2].name == 'PO23'
    pf.db.delete_post_office(po1.id)
    pf.db.delete_post_office(po2.id)
    pf.db.delete_post_office(po3.id)

def test_shortest_path_with_no_path(pf):
    # Test finding the shortest path between post offices with no path available
    po1 = pf.db.create_post_office('PO24', 'location24')
    po2 = pf.db.create_post_office('PO25', 'location25')
    path = pf.find_shortest_path('PO24', 'PO25')
    assert path is None
    pf.db.delete_post_office(po1.id)
    pf.db.delete_post_office(po2.id)

def test_shortest_path_with_invalid_post_office(pf):
    # Test finding the shortest path between post offices with an invalid post office name
    po1 = pf.db.create_post_office('PO26', 'location26')
    po2 = pf.db.create_post_office('PO27', 'location27')
    path = pf.find_shortest_path('PO26', 'PO28')
    assert path is None
    pf.db.delete_post_office(po1.id)
    pf.db.delete_post_office(po2.id)