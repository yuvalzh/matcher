from matcherProject.models import Job , Candidate 
from django.db.models import Count
from django.db.models.expressions import RawSQL

def find_best_candidates(job_title):
    # Get requested job
    try:
        job = Job.objects.get(title=job_title)
    except Job.DoesNotExist:
        raise(Exception("job not exist"))
    
    # Get best candidates by 2 params: job_title AND candidates skills
    full_text_search_query = "SELECT id FROM matcher.matcherproject_candidate where match(title) against(%s)"
    qualified_candidates = Candidate.objects.filter(id__in=RawSQL(full_text_search_query,[job_title]),skills__in = job.skills.all()).\
    annotate(relevante_skills = Count("skills")).order_by("-relevante_skills")
    if not qualified_candidates:
        raise(Exception("candidate not exist"))

    # Get the best candidate - with the most required skills to the job 
    max_skills_matched = qualified_candidates.first().relevante_skills
    best_candidates = qualified_candidates.filter(relevante_skills=max_skills_matched).values_list("id", "title")

    return best_candidates


def find_best_candidates_no_bonus(job_title):
    # Get requested job
    try:
        jobs = Job.objects.get(title=job_title)
    except Job.DoesNotExist:
        raise(Exception("job not exist"))
    
    # Get best candidates by 2 params: job_title AND candidates skills
    qualified_candidate = Candidate.objects.filter(title=job_title,skills__in = jobs.skills.all()).\
    annotate(relevante_skills = Count("skills")).order_by("-relevante_skills")
    if not qualified_candidate:
        raise(Exception("candidate not exist"))

    # Get the best candidate - with the most required skills to the job 
    max_skills_matched = qualified_candidate.first().relevante_skills
    best_candidates = qualified_candidate.filter(relevante_skills=max_skills_matched).values_list("id", "title")
    
    return best_candidates