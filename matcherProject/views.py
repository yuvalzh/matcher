from django.http import HttpResponse
from matcherProject.services.candidates_service import find_best_candidates

# Create your views here.

def handle_candidates_query (request):
    # get param from request
    job_title = request.GET.get('job_title')
    
    # validate them 
    if not job_title:
        return HttpResponse('not valid job title')
    try:
        candidates  = find_best_candidates(job_title)
    except Exception as err:
        return HttpResponse(err)

    # return the response
    return HttpResponse(candidates)
