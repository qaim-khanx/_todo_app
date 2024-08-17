from fastapi.testclient import TestClient
from fastapi import FastAPI
from todo_app import settings
from sqlmodel import SQLModel, create_engine, Session
from todo_app.main import app, get_session

connection_string : str = str(settings.TEST_DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode":"require"}, pool_recycle = 300, pool_size = 10, echo = True)
# Test-1 Root test  
def test_root():
    client = TestClient(app = app)
    respone = client.get('/')
    data = respone.json()
    assert respone.status_code == 200
    assert data == {"message": "Welcome to todo app"}

# Test-2 Post test
def test_create_todo():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def db_session_override():
            return session
    app.dependency_overrides[get_session] = db_session_override
    client = TestClient(app=app)
    test_todo = {"content": "create todo test", "is_completed":False}
    response = client.post('/todos', json=test_todo)
    data = response.status_code == 200
    assert data["content"] == test_todo["content"]

# Test-3 : get_all
def test_get_all():
      SQLModel.metadata.create_all(engine)
      with Session(engine) as session:
        def db_session_override():
            return session
      app.dependency_overrides[get_session] = db_session_override
      client = TestClient(app=app)
      test_todo = {"content": "get all todos test", "is_completed":False}
      response = client.post('/todos', json= test_todo)
      data = response.json()

      response = client.get('/todos')
      new_todo =  response.json()[-1]
      assert response.status_code == 200
      assert new_todo["content"] == test_todo["content"]

# Test-4 Single todo
def test_get_single_todo():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        def db_session_override():
            return session
    app.dependency_overrides[get_session] = db_session_override
    client = TestClient(app = app)
    test_todo = { "content": "get single todo test", "is_completed":False}    
    response = client.post('/todos/', json= test_todo)
    todo_id = response.json()["id"]

    res= client.get(f'/todos/{todo_id}')
    data = res.json()
    assert res.status_code == 200
    assert data["content"] == test_todo["content"]  

# Test-5 :Edit todo
def test_edit_todo():
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            def db_session_override():
               return session
        app.dependency_overrides[get_session] = db_session_override
        client = TestClient(app=app)

        test_todo = {"content": "edit todos test", "is_completed":False}
        response = client.post('/todos', json= test_todo)
        todo_id = response.json()["id"]

        edited_todo = {"content":"We have edited this", "is_completed":False}
        respone = client.put(f'/todos/{todo_id}', json= edited_todo)
        data = response.json()
        assert response.status_code == 200
        assert data["content"] == edited_todo["content"]
#Test -6 Delete Todo

def test_delete_todo():
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            def db_session_override():
               return session
        app.dependency_overrides[get_session] = db_session_override
        client = TestClient(app=app)

        test_todo = {"content": "delete todos test", "is_completed":False}
        response = client.post('/todos', json= test_todo)
        todo_id = response.json()["id"] 

        response = client.delete(f'/todos{todo_id}')
        data = response.json()
        assert response.status_code == 200 
        assert data["message"] == "Task successfully deleted"