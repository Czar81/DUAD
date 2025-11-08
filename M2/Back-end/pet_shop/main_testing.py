from db.utils_db.tables_manager import TablesManager
from testing.db_testing import DbTestingManager

if __name__=="__main__":
    TablesManager.create_tables()
    db_testing=DbTestingManager()
    db_testing.menu()