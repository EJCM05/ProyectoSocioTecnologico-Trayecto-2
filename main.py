# main.py
from login import LoginApp
from dashboard import Dashboard


def main():
        login_app = LoginApp()
        usuario_autenticado = login_app.run()  # Suponiendo que run devuelve True si la autenticación es exitosa
if usuario_autenticado:
        dashboard = Dashboard()
        dashboard.run()

if _name_ == "_main_":
        main()