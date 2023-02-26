from app.general.general_run import MainDialog
from app.general.get_data_from_database import get_data_from_db




if __name__ == "__main__":
    md = MainDialog()
    md.main_dialog()
    #print(get_data_from_db("wollplatz"))
