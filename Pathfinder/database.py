from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import PostOffice, Edge, Base

class Database:
    # Create engine and sessionmaker
    def __init__(self):
        self.engine = create_engine('sqlite:///test.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    # Create objects in the database
    def create_post_office(self, name, location):
        session = self.Session()
        post_office = PostOffice(name=name, location=location)
        session.add(post_office)
        session.commit()
        session.close()
        return post_office

    def create_edge(self, start, end, distance):
        session = self.Session()
        nStart = self.get_post_office_by_name(start)
        nEnd = self.get_post_office_by_name(end)
        if nEnd is None:
            self.create_post_office(end, end.split(" ")[2:][0])
            return end
        end_id = self.get_post_office_by_name(end)
        edge = Edge(start=nStart, end=end_id, distance=distance)
        session.add(edge)
        session.commit()
        session.close()

    # Retrieve objects from the database
    def get_all_post_offices(self):
        session = self.Session()
        post_offices = session.query(PostOffice).all()
        session.close()
        return post_offices

    def get_post_office_by_id(self, id):
        session = self.Session()
        post_office = session.query(PostOffice).filter_by(id=id).first()
        session.close()
        return post_office
    
    def get_post_office_by_name(self, name):
        session = self.Session()
        post_office = session.query(PostOffice).filter_by(name=name).first()
        session.close()
        return post_office.id if post_office else None

    def get_all_edges(self):
        session = self.Session()
        edges = session.query(Edge).all()
        session.close()
        return edges

    def get_edge_by_id(self, id):
        session = self.Session()
        edge = session.query(Edge).filter_by(id=id).first()
        session.close()
        return edge

    # Update objects in the database
    def update_post_office(self, id, name=None, location=None):
        session = self.Session()
        post_office = session.query(PostOffice).filter_by(id=id).first()
        if name:
            post_office.name = name
        if location:
            post_office.location = location
        session.commit()
        session.close()
        return post_office

    def update_edge(self, id, start=None, end=None, distance=None):
        session = self.Session()
        edge = session.query(Edge).filter_by(id=id).first()
        if start:
            edge.start = start
        if end:
            edge.end = end
        if distance:
            edge.distance = distance
        session.commit()
        session.close()
        return edge

    # Delete objects from the database
    def delete_post_office(self, id_):
        session = self.Session()
        post_office = session.query(PostOffice).filter_by(id=id_).first()
        print(id_)
        if post_office:
            session.delete(post_office)
            print("leeeeeeeeeeeeeeeeeeeeeel")
        session.commit()
        session.close()

    def delete_edge(self, locationID):
        session = self.Session()
        edge = session.query(Edge)
        while edge:
            edge = session.query(Edge).filter_by(start=locationID).first()
            if edge:
                session.delete(edge)
        edge = session.query(Edge)
        while edge:
            edge = session.query(Edge).filter_by(end=locationID).first()
            if edge:
                session.delete(edge)
        session.commit()
        session.close()


col = Database().delete_edge(6)
print(col)