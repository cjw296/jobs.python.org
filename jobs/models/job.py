from mortar_rdb import declarative_base

from .common import Common

Base = declarative_base()

"""
class Job(Base,Common):

    # primary key
    id = Column(Integer, primary_key=True)
    
    # job fields
    company_name
    company_url
    company_description
    location
    description
    requirements = relationship(
        "Requirement",
        order_by="Requirement.id",
        backref="job",
        cascade="all"
        )
    python_use
    contact_name
    contact_email
    contact_other
    job_url
    job_type # per, contract, project
    telecommuting # none, some, all

    type_of_work
      full or part time employment
      project-based contract
      day or hourly rate
    
    # workflow fields
    workflow_state
    first_published
    
    
    
    username = Column(String(50), primary_key=True)
    full_name = Column(Unicode(100), nullable=False, default=u'')
    company = Column(Unicode(100), nullable=False, default=u'')
    role = Column(Enum(*roles))

    ips = 

    grants = relationship("Grant",
                          cascade="all",
                          lazy="dynamic",
                          order_by=Grant.sku)
"""
