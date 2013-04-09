from sqlalchemy.ext.declarative import has_inherited_table
from sqlalchemy.util import classproperty

class Common(object):
    
    @classproperty
    def __tablename__(cls):
        if has_inherited_table(cls):
            return None
        return cls.__name__.lower()
    
    __table_args__ = {'mysql_engine':'InnoDB',
                      'mysql_charset':'utf8'}
