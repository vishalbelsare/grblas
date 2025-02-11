def pytest_addoption(parser):
    parser.addoption(
        "--backend",
        action="store",
        default="suitesparse",
        help="name of a backend in grblas.backends",
    )
    parser.addoption("--runslow", action="store_true", help="run slow tests")
    parser.addoption(
        "--blocking",
        dest="blocking",
        default=True,
        action="store_true",
        help="run in blocking mode",
    )
    parser.addoption(
        "--nonblocking",
        "--no-blocking",
        "--non-blocking",
        dest="blocking",
        action="store_false",
        help="run in non-blocking mode",
    )
    parser.addoption(
        "--record",
        dest="record",
        default=False,
        action="store_true",
        help="Record GraphBLAS C calls and save to 'record.txt'",
    )
    parser.addoption(
        "--mapnumpy", action="store_true", default=None, help="may numpy ops to GraphBLAS ops"
    )
