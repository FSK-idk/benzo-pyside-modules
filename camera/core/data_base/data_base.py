import os
import json

from PySide6.QtCore import QObject
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord

from core.model.camera_load import CameraLoad

from core.data_base.query import Query


class DataBase(QObject):
    def init(self) -> None:
        if not os.path.isdir('data/'):
            os.mkdir('data/')

        self.data_base: QSqlDatabase = QSqlDatabase('QSQLITE')
        self.data_base.setDatabaseName('data/data_base.sqlite')
        self.data_base.open()

        query: QSqlQuery = QSqlQuery(self.data_base)
        query.prepare(Query.createCardLoadTable())
        query.exec()

        json_filename: str = 'data/camera_load.json'
        with open(json_filename) as json_file:
            json_data = json.load(json_file)
            for json_load in json_data['CameraLoad']:
                load: CameraLoad = CameraLoad(
                    date_time=json_load['date_time'],
                    car_number=json_load['car_number'],
                    image_filename=json_load['image_filename'],
                    is_recognized=json_load['is_recognized'],
                )
                self.insertCameraLoad(load)

    def insertCameraLoad(self, load: CameraLoad) -> None:
        query: QSqlQuery = QSqlQuery(self.data_base)
        query.prepare(Query.insertCameraLoad())
        query.bindValue(':date_time', load.date_time)
        query.bindValue(':car_number', load.car_number)
        query.bindValue(':image_filename', load.image_filename)
        query.bindValue(':is_recognized', load.is_recognized)
        query.exec()

    def selectCameraLoadByImageFilename(self, image_filename: str) -> CameraLoad | None:
        query: QSqlQuery = QSqlQuery(self.data_base)
        query.prepare(Query.selectCameraLoadByImageFilename())
        query.bindValue(':image_filename', image_filename)
        query.exec()

        rec: QSqlRecord = query.record()
        if query.next():
            row = [query.value(index) for index in range(rec.count())]
            return CameraLoad.from_data(row)

        return None


data_base: DataBase = DataBase()
