# create role tamanno;
# create database tamanno;

# 1 - savol

# import datetime
# from sqlalchemy import create_engine, String, Text, ForeignKey, Column, DateTime
# from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship,sessionmaker
# from faker import Faker
#
# engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/postgres")
#
# faker = Faker()
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()
#
#
# class CreateModel(Base):
#     __abstract__ = True
#     created_at = Column("created_at",DateTime, default=datetime.datetime.now)
#     updated_at = Column("updated_at",DateTime, default=datetime.datetime.now)
#
# class Car(CreateModel):
#     __tablename__ = 'car'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(255))
#     price: Mapped[float] = mapped_column()
#     brand: Mapped[str] = mapped_column(String(255))
#
# Base.metadata.create_all(engine)
#
#
# all_obj = []
# all_obj.extend([Car(name=faker.name() , price=faker.random_int(1,100),brand=faker.text()) for i in range(1 , 400000)])
# session.add_all(all_obj)
# session.commit()


# 2 - savol

'''

tamanno@tamanno:~$ docker run --name my_postgresql  -e POSTGRES_PASSWORD=1 -p 6000:5432 -it -d postgres:15.3-alpine
32b11b97b1fd6f4c3c5eb09273c08da5cfa40e008a1511cad1279913686111c1
tamanno@tamanno:~$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS                     PORTS                                       NAMES
32b11b97b1fd   postgres:15.3-alpine   "docker-entrypoint.s…"   6 seconds ago   Up 5 seconds               0.0.0.0:6000->5432/tcp, :::6000->5432/tcp   my_postgresql
27c41f932019   redis:alpine           "docker-entrypoint.s…"   3 weeks ago     Exited (0) 3 weeks ago                                                 redis_con
2ed235e6c488   postgres:15.3-alpine   "docker-entrypoint.s…"   4 weeks ago     Exited (0) 3 weeks ago                                                 my_laptop
49a4d9869089   postgres:15.3-alpine   "docker-entrypoint.s…"   4 weeks ago     Exited (0) 4 weeks ago                                                 my_container
ed2aaf63fa6d   postgres:15.3-alpine   "docker-entrypoint.s…"   4 weeks ago     Exited (128) 3 weeks ago                                               my_postgres
tamanno@tamanno:~$ \cd Downloads/
tamanno@tamanno:~/Downloads$ docker cp dvdrental.zip my_postgresql:\tmp\
Successfully copied 552kB to my_postgresql:tmp
tamanno@tamanno:~/Downloads$ ls
 chart.png
 docker-desktop-4.19.0-amd64.deb
'dvdrental (1).zip'
 dvdrental.tar
 dvdrental.zip
 _gpgbuilder
 online_shop.pdf
 photo_2023-07-04_17-19-09-removebg-preview.png
 pycharm-2021.2.1
 pycharm-2023.1
 pycharm-professional-2021.2.1.tar.gz
 pycharm-professional-2023.1.1.tar.gz
 pycharm-professional-2023.1.tar.gz
'screen-capture (1).webm'
 screen-capture.webm
 Telegram
'Telegram Desktop'
 tsetup.4.8.1.tar.xz
'zoom_amd64 (1).deb'
'zoom_amd64 (2).deb'
 zoom_amd64.deb
tamanno@tamanno:~/Downloads$ docker exec -it -u postgres my_postgresql sh
/ $ ls
bin                         proc
dev                         root
docker-entrypoint-initdb.d  run
etc                         sbin
home                        srv
lib                         sys
media                       tmp
mnt                         usr
opt                         var
/ $ cd tmp
/tmp $ ls
dvdrental.zip
/tmp $ unzip dvdrental.zip
Archive:  dvdrental.zip
  inflating: dvdrental.tar
/tmp $ ls
dvdrental.tar  dvdrental.zip
/tmp $

'''


# 3 - savol


# import datetime
# from sqlalchemy import String, Text, ForeignKey, Column, DateTime,create_engine
# from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship,Session
# from faker import Faker
#
# faker = Faker()
# Base = declarative_base()
# session = Session()
# engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/faker_db")
#
#
# class CreateModel(Base):
#     __abstract__ = True
#     created_at = Column("created_at",DateTime, default=datetime.datetime.now)
#     updated_at = Column("updated_at",DateTime, default=datetime.datetime.now)
#
# class Car(CreateModel):
#     __tablename__ = 'car'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(255))
#     price: Mapped[float] = mapped_column()
#     brand: Mapped[str] = mapped_column(String(255))
#     car_details:Mapped[list["Car_detail"]] = relationship(back_populates="car")
#
# class Car_detail(CreateModel):
#     __tablename__ = 'car_detail'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
#     detail: Mapped[str] = mapped_column(String(255))
#     car:Mapped["Car"] = relationship(back_populates="car_detail")
#
# Base.metadata.create_all(engine)
#
#
# detail_data = {
#     "name": "Harry",
#     "age": 17,
#     "city": "America"
# }
#
#
# Car_detail.insert(detail = detail_data)
# Car_detail.commit()
#
# all_obj = [Car_detail(id=i) for i in range(1, 6)]
# session.add_all(all_obj)
# session.commit()



# 4 - savol


# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,DateTime
# from sqlalchemy.orm import relationship,declarative_base
# import uuid
# import datetime
#
# engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/faker_db")
#
# Base = declarative_base()
#
# class CreateModel(Base):
#     __abstract__ = True
#     created_at = Column("created_at",DateTime, default=datetime.datetime.now)
#     updated_at = Column("updated_at",DateTime, default=datetime.datetime.now)
#
# class CarOwner(CreateModel):
#     __tablename__ = 'car_owner'
#
#     id = Column(String, primary_key=True, default=str(uuid.uuid4()))
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True)
#
#     cars = relationship('Car', back_populates='owner')
#
# class Car(CreateModel):
#     __tablename__ = 'car'
#
#     id = Column(String, primary_key=True, default=str(uuid.uuid4()))
#     car_owner_id = Column(String, ForeignKey('car_owner.id'))
#
#     owner = relationship('CarOwner', back_populates='cars')
#
# Base.metadata.create_all(engine)


