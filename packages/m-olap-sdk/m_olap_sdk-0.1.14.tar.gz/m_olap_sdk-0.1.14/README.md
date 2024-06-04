
==============================

  module mining data in OLAP

==============================

* Raw Query: 
```python
from mobio.libs.olap.mining_warehouse.base_engine.base_session import BaseSession
from sqlalchemy import text


class JourneyReportHandle:
    def __init__(self, olap_uri, sniff=False):
        self.session = BaseSession(olap_uri=olap_uri, sniff=sniff)

    def get_journey_by_id(self, record_id):
        stmt = """
        select `name` from report where id=:record_id
        """
        with self.session.SessionLocal() as session:
            result = session.execute(
                text(stmt),
                {"id": record_id},
            ).first()
            session.close()

        return result

if __name__ == "__main__":
    with JourneyReportHandle(
        olap_uri="mobio://user:pass@host:host/default_catalog.journey_builder"
    ).session.SessionLocal() as ss:
        result1 = list(
            ss.execute(
                text(
                    """
                    select id from report limit 10
                    """
                ),
            ).all()
        )
        ss.close()
    print("result1 {}".format(result1))
```

* ORM:
```python
from sqlalchemy.orm import declarative_base
from mobio.libs.olap.mining_warehouse.base_engine.base_session import BaseSession
from sqlalchemy import Column, String

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    def __init__(self, olap_uri, sniff=False):
        super(BaseModel, self).__init__()
        self.session = BaseSession(olap_uri=olap_uri, sniff=sniff)
        pass


class JourneyReport(BaseModel):
    __tablename__ = "report"

    id = Column(String(36), primary_key=True)
    journey_id = Column(String(36))
    instance_id = Column(String(36))

    def __repr__(self):
        return f"JourneyReport(id={self.id!r}, journey_id={self.journey_id!r}, instance_id={self.instance_id!r})"

if __name__ == "__main__":
    with JourneyReport(
        olap_uri="mobio://user:pass@host:host/default_catalog.journey_builder"
    ).session.SessionLocal() as ss3:
        result3 = ss3.query(JourneyReport).limit(10).all()
    print("result3 {}".format(result3))
```


Release notes:
* 0.1.14 (2024-06-04):
  * dùng pymysql thay cho MySQL-Client
* 0.1.13 (2024-01-06):
  * Fix issue create connection when cluster only has leader
  * support sniff frontends
* 0.1.12 (2024-01-06):
  * support HA
* 0.1.11 (2023-12-07):
  * port libs
* 0.1.4 (2023-11-28):
  * fix validate column name, support dynamic field with prefix
* 0.1.3 (2023-11-27):
  * remove m-utilities, chỉ dependence m-logging để support python3.8
* 0.1.2 (2023-11-27):
  * alter table
* 0.1.1 (2023-11-24):
  * support lấy profile by id, hỗ trợ việc masking data
