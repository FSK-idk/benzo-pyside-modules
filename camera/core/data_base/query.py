class Query:
    @staticmethod
    def createCardLoadTable() -> str:
        return """
            CREATE TABLE IF NOT EXISTS CameraLoad (
                id                      INTEGER     NOT NULL,
                date_time               TEXT        NOT NULL,
                car_number              TEXT,
                image_filename          TEXT        NOT NULL,
                is_recognized           TEXT        NOT NULL,
                PRIMARY KEY (id),
                UNIQUE (car_number, image_filename),
                CHECK (date_time != '' AND car_number != '' AND image_filename != ''),
                CHECK (is_recognized IN ('true', 'false'))
            )
        """

    @staticmethod
    def insertCameraLoad() -> str:
        return """
            INSERT OR IGNORE INTO CameraLoad (
                date_time,
                car_number,
                image_filename,
                is_recognized
            )
            VALUES (
                :date_time, 
                :car_number,
                :image_filename,
                :is_recognized
            )
        """

    @staticmethod
    def selectCameraLoadByImageFilename() -> str:
        return f"""
            SELECT date_time, car_number, image_filename, is_recognized
            FROM CameraLoad
            WHERE image_filename = :image_filename
        """
