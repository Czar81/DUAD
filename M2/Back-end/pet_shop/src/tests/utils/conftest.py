from src.utils import register_error_handlers, APIException
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask, Blueprint
import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    bp = Blueprint("test_bp", __name__)

    register_error_handlers(bp)

    @bp.route("/value-error")
    def route_value_error():
        raise ValueError("bad value")

    @bp.route("/db-error")
    def route_db_error():
        raise SQLAlchemyError("db failed")

    @bp.route("/api-error")
    def route_api_error():
        raise APIException("custom fail", 418)

    @bp.route("/rec-error")
    def route_rec_error():
        raise RecursionError("stack explosion")

    @bp.route("/generic-error")
    def route_generic_error():
        raise RuntimeError("boom")

    app.register_blueprint(bp)
    client = app.test_client()

    return client
