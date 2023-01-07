
def exc_to_dict(exc):
    try:
        remark = exc.detail["remarks"]
    except:
        remark = exc.detail 


    return dict(status="failed",remarks=remark,response_code=exc.status_code)

def error_404(request,exc,templates,layer_4,JSONResponse,auth_re):
    resp = dict(status="failed",remarks=str(exc),errorCode=exc.status_code,errorType="Page Not Found")
    resp = dict(layer_4(**resp))
    return templates.TemplateResponse('404.html', status_code=404,context={'request': request})

def error_401(exc,JSONResponse,auth_re):
    resp = dict(auth_re(**exc_to_dict(exc)))
    return JSONResponse(status_code=exc.status_code, content=resp)

def error_500(exc,JSONResponse,auth_re):
    resp = dict(auth_re(**exc_to_dict(exc)))
    return JSONResponse(status_code=exc.status_code, content=resp)

def error_422(exc,JSONResponse,auth_re):
    resp = dict(auth_re(**exc_to_dict(exc)))
    return JSONResponse(status_code=exc.status_code, content=resp)