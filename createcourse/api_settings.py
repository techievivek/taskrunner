workshop_url=r'http://localhost:5500/api/upcoming_workshops?date_from=2020-06-10' #url on workshop site to fecth data.
yaksh_post_url=r'http://localhost:8000/api/course/create/' #url on yaksh api to create courses.
workshop_json_file_mapper= {
    "1":'1-day-course.json',
    "2":'2-day-course.json',
    "3":'3-day-course.json'
} #based on workshop duration we will match its course content file.