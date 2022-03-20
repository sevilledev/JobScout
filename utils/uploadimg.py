def upload_job_img(instance,filename):
    return f'job/{instance.id}/{filename}'

def upload_blog_img(instance,filename):
    return f'blog/{instance.id}/{filename}'

def upload_appfront_img(instance,filename):
    return f'appfront/{filename}'

def upload_contact_file(instance,filename):
    return f'contact/{filename}'