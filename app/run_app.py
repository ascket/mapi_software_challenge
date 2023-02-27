"""The main module that starts the application"""

from app.general.general_run import MainDialog
from app.general.get_data_from_database import get_data_from_db

if __name__ == "__main__":
    md = MainDialog()
    md.main_dialog()
    # If after the first launch of the application the results are saved to the database, you can see them if you uncomment line number 10. Lines 7. and 8. should be comment
    #print(get_data_from_db("wollplatz"))
