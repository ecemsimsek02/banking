import logging


logger = logging.getLogger('bank')

class LogRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Loglama yapılacak yer
        logger.info(f'Request: {request.method} {request.get_full_path()} from {request.META.get("REMOTE_ADDR")}')
        
        response = self.get_response(request)
        
        # Loglama yapılacak yer
        logger.info(f'Response: {response.status_code} for {request.method} {request.get_full_path()}')
        
        return response