# (C) Copyright 2014-2017 Hewlett Packard Enterprise Development LP
# Copyright 2018 OP5 AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import falcon
import json
from influx import InfluxClient
import resource
from datetime import datetime

class TweetsV2API(object):
    def __init__(self):
        super(TweetsV2API, self).__init__()
        print('Initializing TweetsV2API!')

    def on_get(self, req, res):
        res.status = '501 Not Implemented'

    def on_post(self, req, res):
        res.status = '501 Not Implemented'


class Tweets(TweetsV2API):
    def __init__(self):
        try:
            super(Tweets, self).__init__()
        except Exception as ex:
            print(ex)
            raise falcon.HTTPInternalServerError('Service unavailable',
                                                 str(ex))


    @resource.resource_try_catch_block
    def on_get(self, req, res):
        conn = InfluxClient()
        params = falcon.uri.parse_query_string(req.query_string)

        start = datetime.strptime(params['start'], '%y/%m/%d %H:%M:%S')
        end = datetime.strptime(params['end'], '%y/%m/%d %H:%M:%S')
        result = self._get_tweets(start, end)

        max_trending_topic_value = 0
        for serie in result.raw['series']:
                for item in serie['values']:
                  print(item)
                  if int(item[1]) >= max_trending_topic_value :
                        max_trending_topic_value = int(item[1])
                        data_dict = dict()
                        data_dict['time'] = item[0]
                        data_dict['max_value'] = item[1]
                        data_dict['word'] = item[2]
                        print(data_dict)

        res.body = json.dumps(data_dict, ensure_ascii=False)
        res.status = falcon.HTTP_200
    
    def _get_tweets(self, start, end):
       conn = InfluxClient()
       result = conn.get_tweets(start, end)
       return result
