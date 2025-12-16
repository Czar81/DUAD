from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .api_exception import APIException
import logging
import traceback

logger = logging.getLogger(__name__)


def register_error_handlers(blueprint):
    
    @blueprint.errorhandler(ValueError)
    def handle_value_error(e):
        logger.warning(f"ValueError: {str(e)}")
        traceback.print_exc()
        return jsonify(error=str(e)), 400
    
    @blueprint.errorhandler(IntegrityError)    
    def handle_integrity_error(e):
        logger.warning(f"Integrity error: {str(e)}")
        traceback.print_exc()
        return jsonify(error=f"Database integrity error: {e}"), 409

    @blueprint.errorhandler(SQLAlchemyError)
    def handle_db_error(e):
        logger.error(f"Database error: {str(e)}")
        traceback.print_exc()
        return jsonify(error=f"Internal database error: {e}"), 500
    
    @blueprint.errorhandler(APIException)
    def handle_api_error(e):
        logger.warning(f"API error: {str(e)}")
        traceback.print_exc()
        return jsonify(error=str(e)), e.status_code
    
    @blueprint.errorhandler(RecursionError)
    def handle_recursion_error(e):
        logger.error(f"Recursion error (Redis issue?): {str(e)}")
        traceback.print_exc()
        return jsonify(error="An unexpected error occurred with redis"), 500
    
    @blueprint.errorhandler(Exception)
    def handle_generic_error(e):
        logger.error(f"Unexpected error: {str(e)}")
        traceback.print_exc()
        return jsonify(error=f"An unexpected error occurred: {e}"), 500