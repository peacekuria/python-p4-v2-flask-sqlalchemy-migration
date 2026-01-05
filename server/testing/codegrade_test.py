
import pytest
from app import app
from models import db, Employee, Department


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


def test_employee_model_exists(client):
    """Test that Employee model exists and has correct attributes"""
    with app.app_context():
        employee = Employee(name="Test Employee", salary=50000)
        assert employee.name == "Test Employee"
        assert employee.salary == 50000


def test_department_model_exists(client):
    """Test that Department model exists and has correct attributes"""
    with app.app_context():
        department = Department(name="Test Department", address="Test Address")
        assert department.name == "Test Department"
        assert department.address == "Test Address"


def test_employee_table_name(client):
    """Test that Employee model uses correct table name"""
    with app.app_context():
        assert Employee.__tablename__ == 'employees'


def test_department_table_name(client):
    """Test that Department model uses correct table name"""
    with app.app_context():
        assert Department.__tablename__ == 'departments'


def test_add_employee_to_database(client):
    """Test adding an employee to the database"""
    with app.app_context():
        employee = Employee(name="Kai Uri", salary=89000)
        db.session.add(employee)
        db.session.commit()
        
        result = Employee.query.filter_by(name="Kai Uri").first()
        assert result is not None
        assert result.salary == 89000


def test_add_department_to_database(client):
    """Test adding a department to the database"""
    with app.app_context():
        department = Department(name="Payroll", address="Building A")
        db.session.add(department)
        db.session.commit()
        
        result = Department.query.filter_by(name="Payroll").first()
        assert result is not None
        assert result.address == "Building A"


def test_employee_repr(client):
    """Test Employee __repr__ method"""
    with app.app_context():
        employee = Employee(id=1, name="Test", salary=100)
        repr_str = repr(employee)
        assert "Employee" in repr_str
        assert "Test" in repr_str


def test_department_repr(client):
    """Test Department __repr__ method"""
    with app.app_context():
        department = Department(id=1, name="Test Dept", address="Test Addr")
        repr_str = repr(department)
        assert "Department" in repr_str
        assert "Test Dept" in repr_str
