def format_response(response):
    return {
        "status": response.status_code,
        "data": response.json()
    }
