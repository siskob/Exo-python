import logging


logging.basicConfig(level = logging.DEBUG, # Permet de spécifier le niveau à partir duquel je souhaite afficher
                    filename = "C:\\Users\\sisso\\Documents\\Exo-python\\Mes_Modules\\app.log",
                    filemode = "w",
                    format= '%(asctime)s - %(levelname)s - %(message)s')


logging.debug("La fonction a bien été exécutée")
logging.info("Message d'info générale")
logging.warning("Attention ! ")
logging.error("Un erreur est arrivée")
logging.critical("Erreur critique")