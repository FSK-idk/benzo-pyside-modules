import os
import sys

from dotenv import load_dotenv

from core.net.server import create_app

from core.data_base.data_base import data_base


def main() -> None:
    os.chdir(os.path.dirname(sys.argv[0]))
    load_dotenv('.env')

    data_base.init()

    app = create_app()

    host = os.getenv('HOST')
    port = os.getenv('PORT')
    if port is not None:
        port = int(port)

    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
