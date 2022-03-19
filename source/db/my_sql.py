from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TIMESTAMP, BOOLEAN
from sqlalchemy.orm import declarative_base, Session
from constants import DATABASE_HOST, DATABASE_PASSWORD, DATABASE_USER_NAME
from utils import get_environment_variable

Base = declarative_base()


class ProductionHospitalsData:
    def __init__(self):
        self.database_name = "production_hospitals_data"
        self.host = get_environment_variable(DATABASE_HOST)
        self.username = get_environment_variable(DATABASE_USER_NAME)
        self.password = get_environment_variable(DATABASE_PASSWORD)
        self.url_connection = f"mysql://{self.username}:{self.password}@{self.host}/{self.database_name}"
        self.engine = create_engine(self.url_connection, echo=True, future=True)

    def __enter__(self):
        self.session = Session(self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()


class Treatments(Base):
    __tablename__ = "treatments"

    patient_id = Column(String, nullable=False)
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)
    active = Column(BOOLEAN, nullable=False)
    display_name = Column(String, nullable=False)
    diagnoses = Column(String, nullable=False)
    treatment_line = Column(String, nullable=False)
    number_of_cycles = Column(String, nullable=False)
    treatment_id = Column(String, nullable=False)
    protocol_id = Column(String, nullable=False)


class Patients(Base):
    __tablename__ = "patients"

    patient_id = Column(String, nullable=False)
    mrn = Column(String, nullable=False)
    date_of_birth = Column(TIMESTAMP, nullable=False)
    is_deceased = Column(String, nullable=False)
    date_of_death = Column(TIMESTAMP, nullable=False)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    last_modified_date = Column(TIMESTAMP, nullable=False)
