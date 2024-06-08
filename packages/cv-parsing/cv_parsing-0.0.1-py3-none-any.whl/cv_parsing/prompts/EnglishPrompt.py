from cv_parsing.prompts.Prompt import Prompt
from string import Template
from cv_parsing.utils.json_utils import JSON_STR, SCHEMA_DICT


prompt_header = """
    You are an assistant for the Human Resource Team at a Portuguese employer. 
    You have been tasked with extracting information from a resume in json structured format.
    Your answer must skip any introductory text and focus on the json structured information.
    Most of the candidates are applying for a job in Portugal, so most of the resumes are in Portuguese.
"""


class BasicPrompt(Prompt):
    def __init__(self, feature="all", schema=JSON_STR, header=prompt_header) -> None:
        super().__init__('english', feature, schema, header, Template(
            f"""
    The unstructured String that represents the resume is as follows:

    $cv

    You should extract the following information from the resume:
    
    $json_schema   

    Some of the information may not be present in the resume. In such cases, you should produce null.

    The jobs can either be a job in industry or academic

    If you need to perform any calculations regarding dates: 
     - you can assume that the current year is $current_year.
     - if the date extends to the present, you should consider the date as "PRESENT".
     
    If the age is provided: 
     - instead of the birth_year, you should provide the birthyear only.
     - The age should be calculated based on the current year $current_year.

    In the cases of the languages: 
     - You should consider three language_levels: A, B, C.
     - The mother tongue should be considered as the highest language_level.
    """))


class ExtractPersonalInformationPrompt(Prompt):
    def __init__(self, feature="personal_information", schema=SCHEMA_DICT['personal_information'], header=prompt_header) -> None:
        super().__init__('english', feature, schema, header, Template(
            f"""
    The unstructured String that represents the resume is as follows:

    $cv

    You should extract the following information from the resume:
    
    {{"{feature}":$json_schema}}
    
    Some of the information may not be present in the resume. In such cases, you should produce null.

    If you need to perform any calculations regarding dates: 
     - you can assume that the current year is $current_year.
    """))


class ExtractJobsPrompt(Prompt):
    def __init__(self, feature="jobs", schema=SCHEMA_DICT['jobs'], header=prompt_header) -> None:
        super().__init__('english', feature, schema, header, Template(
            f"""
  
    The unstructured String that represents the resume is as follows:

    $cv

    Your job is to extract information regarding the jobs that the candidate has had.
    
    You should extract the following information from the resume:
    
    {{"{feature}":$json_schema}}
        
    Some of the information may not be present in the resume. In such cases, you should produce null.

    The jobs can either be in industry or academia:
     - If it is an academic job, it is heavily like the employer to be a university or research center     
    
     If you need to perform any calculations regarding dates: 
     - you can assume that the current year is $current_year.
     - if the date extends to the present, you should consider the date as "PRESENT".    
    """))


class ExtractEducationPrompt(Prompt):
    def __init__(self, feature="education", schema=SCHEMA_DICT['education'], header=prompt_header) -> None:
        super().__init__('english', feature, schema, header, Template(
            f"""
    The unstructured String that represents the resume is as follows:

    $cv

    Your job is to extract information regarding the education that the candidate has.

    You should extract the following information from the resume:
    
    {{"{feature}":$json_schema}}

    Some of the information may not be present in the resume. In such cases, you should produce null.

    If you need to perform any calculations regarding dates: 
     - you can assume that the current year is $current_year.
     - if the date extends to the present, you should consider the date as "PRESENT".
    """))


class ExtractLanguagesPrompt(Prompt):
    def __init__(self, feature="languages", schema=SCHEMA_DICT['languages'], header=prompt_header) -> None:
        super().__init__('english', feature, schema, header, Template(
            f"""
    
    The unstructured String that represents the resume is as follows:

    $cv

    Your job is to extract information regarding the language that the candidate knows how to speak.

    You should extract the following information from the resume:
    
    {{"{feature}":$json_schema}}

    Some of the information may not be present in the resume. In such cases, you should produce null.
    
    You should consider three proficiency language_levels: 
     -A
     -B 
     -C

    If there is mention of mother tongue / native should be considered C.
    """))
