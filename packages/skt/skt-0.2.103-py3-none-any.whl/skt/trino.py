import os


def init_trino(
    cluster_name: str = "aidp-cluster",
    host: str = "gateway-idp-prd.sktai.io",
    port: int = 443,
    connect_args: dict = None,
    user: str = None,
    password: str = None,
):
    from sqlalchemy import create_engine
    from trino.sqlalchemy import URL

    connect_args = connect_args or {
        "extra_credential": [("cluster_name", cluster_name)],
        "http_scheme": "https",
    }

    engine = create_engine(
        URL(host=host, port=port, user=user or os.environ.get("NB_USER", "skt"), password=password),
        connect_args=connect_args,
    )

    try:
        from IPython import get_ipython

        ipython = get_ipython()
        if ipython:
            ipython.run_line_magic("load_ext", "sql", 1)
            ipython.run_line_magic("alias_magic", "trino sql", 1)
            ipython.run_line_magic("sql", "engine", 1)
    except ImportError:
        print("IPython not found, skipping magic commands")

    return engine
