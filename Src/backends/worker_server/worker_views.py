__author__ = 'zdvitas'
import tools.worker_mysql


def get_document_view(document_id):
    result = tools.worker_mysql.get_document(document_id)
    return result


def get_all_documents_view():
    return tools.worker_mysql.get_all_documents_sql()