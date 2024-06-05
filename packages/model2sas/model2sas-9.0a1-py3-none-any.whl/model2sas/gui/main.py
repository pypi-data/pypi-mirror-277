import panel as pn
from .webui import app

def run():
    pn.serve(
        {"Model2SAS-GUI": app},
        title="Model2SAS",
        show=True,
        start=True,
        autoreload=False
    )

if __name__ == '__main__':
    run()