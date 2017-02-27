# -*- coding: utf-8 -*-


from facility.models import ContactOwner


title = ('ID',
         u'Тип обекта',
         u'Улица',
         u'Район',
         u'Метро',
         u'Номер дома',
         u'Номер квартиры',
         u'Цена(выкуп)',
         u'Цена(месяц)',
         u'Тип операции',
         u'Строение',
         u'Ремонт',
         u'Ориентир',
         u'Этажность от',
         u'Этажность до',
         u'Первый',
         u'Последний',
         u'Этаж',
         u'Спальня площадь',
         u'Кухня площадь',
         u'Гостинная площадь',
         u'Доп.комната площадь',
         u'Общая площадь',
         u'Комнаты',
         u'Платежи',
         u'Комнат',
         u'Комментарий',
         u'Риелтор',
         u'Лояльность',
         u'Актуальность',
         u'Состояние',
         u'Комиссия',
         u'Валюта',
         u'Количество фото',
         u'Заголовок',
         u'YouTube',
         u'Панорама',
         u'Количество человек',
         u'Техника',
         u'Вода',
         u'Участок',
         u'Спальных мест',
         u'Где спать ?',
         u'Предоплата',
         u'Окна',
         u'Отопление',
         u'Санузел',
         u'Мебель',
         u'Дата обновления',
         u'Дата добавления',
         u'Публикуеться',
         u'Тип владельца',
         u'Агенство',
         u'Имя владельца',
         u'Пересмотр Дата',
         u'Звонок Дата',
         u'E-mail владельца',
         'Vip',
         u'Телефон',
         u'Допол. Телефон')


class SaveConOwn(ContactOwner):
    class Meta:
        proxy = True

    def __str__(self):
        return '''%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                  %s,%s,%s,%s,%s''' % \
            (self.id,
             self.type_facilit,
             self.street_obj,
             self.district_obj,
             self.subway_obj,
             str(self.number_home),
             str(self.number_apartment),
             str(self.price_bay),
             str(self.price_month),
             str(self.list_operations.all()),
             self.type_building_data,
             self.repairs,
             self.landmark.encode('utf8'),
             str(self.number_of_floors),
             str(self.floors_up),
             str(self.first_floor),
             str(self.last_floor),
             str(self.floor),
             self.area_badroom.encode('utf8'),
             str(self.area_kitchen),
             self.area_living_room.encode('utf8'),
             self.area_extra_room.encode('utf8'),
             str(self.total_area),
             self.room,
             self.payments.encode('utf8'),
             str(self.rooms),
             self.comment.encode('utf8'),
             self.rieltor.all(),
             self.loyality.all(),
             self.actuality,
             self.condition,
             self.commission.encode('utf8'),
             self.currency,
             str(self.images_count),
             self.title.encode('utf8'),
             self.youtube.encode('utf8'),
             self.panorama.encode('utf8'),
             self.number_of_persons.all(),
             self.equipment.all(),
             self.the_presence_of_hot_water,
             str(self.lot),
             str(self.sleeps),
             self.where_to_stay.all(),
             self.prepayment,
             self.windows,
             self.heating,
             self.lavatory,
             self.furniture,
             str(self.date_of_renovation),
             str(self.date_added),
             str(self.public),
             self.contact_owner,
             self.agency.encode('utf8'),
             self.name_owner.encode('utf8'),
             str(self.review_date),
             str(self.call_date),
             self.email_owner.encode('utf8'),
             self.vip_owner,
             self.phone_owner.encode('utf8'),
             self.phone_owner_plus.encode('utf8')
             )