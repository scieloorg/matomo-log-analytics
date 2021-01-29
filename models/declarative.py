from sqlalchemy import Column, BOOLEAN, Date, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class LogFile(Base):
    __tablename__ = 'log_file'

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)

    full_path = Column(VARCHAR(255), nullable=False, unique=True)
    name = Column(VARCHAR(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    size = Column(INTEGER, nullable=False)
    server = Column(VARCHAR(255), nullable=False)
    date = Column(Date, nullable=False, index=True)
    status = Column(VARCHAR(10))


class LogFileSummary(Base):
    __tablename__ = 'log_file_summary'

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    idlogfile = Column(INTEGER(unsigned=True), ForeignKey('log_file.id', name='idlogfile'))

    total_lines = Column(INTEGER, nullable=False)
    lines_parsed = Column(INTEGER)

    total_imported_lines = Column(INTEGER)
    total_ignored_lines = Column(INTEGER)

    ignored_lines_filtered = Column(INTEGER)
    ignored_lines_http_errors = Column(INTEGER)
    ignored_lines_http_redirects = Column(INTEGER)
    ignored_lines_invalid = Column(INTEGER)
    ignored_lines_bots = Column(INTEGER)
    ignored_lines_static_resources = Column(INTEGER)

    total_time = Column(INTEGER)
    status = Column(VARCHAR(10))
