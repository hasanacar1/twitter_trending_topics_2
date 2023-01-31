# Copyright 2018 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
import datetime

import influxdb
import six

from datetime import datetime


INFLUX_STORAGE_GROUP = 'storage_influxdb'

PERIOD_FIELD_NAME = '__ck_collect_period'


def _sanitized_groupby(groupby):
    forbidden = ('time',)
    return [g for g in groupby if g not in forbidden] if groupby else []


class InfluxClient(object):
  """Classe used to ease interaction with InfluxDB"""
  def __init__(self, chunk_size=500, autocommit=True, default_period=3600):
      self._conn = self._get_influx_client()
      self._chunk_size = chunk_size
      self._autocommit = autocommit
      self._retention_policy = 'autogen'
      self._default_period = default_period
      self._points = []

  def _get_influx_client(self):
        return influxdb.InfluxDBClient(
              username='admin',
              password='1234qweR',
              host='localhost',
              port=8086,
              database='twitter'
            )

  def commit(self):
        self._conn.write_points(self._points,
                                retention_policy=self._retention_policy)
        self._points = []

  def append_point(self,point_list):
        """Adds a point to commit to InfluxDB.

        :param metric_type: Name of the metric type
        :type metric_type: str
        :param start: Start of the period the point applies to
        :type start: datetime.datetime
        :param period: length of the period the point applies to (in seconds)
        :type period: int
        :param point: Point to push
        :type point: dataframe.DataPoint
        """
        print(point_list)
        measurement_fields = dict()
        measurement_tags = dict()
        for count, dict_item in enumerate(point_list):
              column_name1 = 'wordcount_{}'.format(count)
              column_name2 = 'word_{}'.format(count)
              measurement_fields[column_name1] = int(dict_item['wordcount'])
              measurement_tags[column_name2] = dict_item['word']
  
        print(measurement_tags)
        print(measurement_fields)

        self._points.append({
              'measurement': 'twitter_meas',
              'tags': measurement_tags,
              'fields': measurement_fields,
              'time': datetime.now(),
        })
        self.commit()

  def get_tweets(self, start, end):
        print(start)
        print(end)
        start_time = start.isoformat() + ".00Z"
        end_time = end.isoformat() + ".00Z"
        x = """select * from (select sum(wordcount_0) as max_value from twitter_meas where time >= '{x}' and time < {y} group by word_0 )""".format(x=start_time, y=end_time)
        print(x)
        tweets = self._conn.query(
              """select * from (select sum(wordcount_0) as max_value from twitter_meas where time >= '{x}' and time < '{y}'
               group by word_0 )""".format(x=start_time, y=end_time))
        return tweets