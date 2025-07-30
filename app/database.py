from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "postgresql://postgres:078@localhost:5432/testdb"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
   SQLModel.metadata.create_all(engine)

def get_session():
   with Session(engine) as session:
      yield session