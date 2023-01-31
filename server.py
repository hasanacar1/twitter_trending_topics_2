# Copyright 2014 IBM Corp
# (C) Copyright 2015,2016 Hewlett Packard Enterprise Development LP
# Copyright 2017 Fujitsu LIMITED
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

import os

import falcon
#from monasca_common.simport import simport
# from oslo_config import cfg
# from oslo_log import log
import paste.deploy

# from monasca_api.api.core import request
#from monasca_api import config

import trending_words

# LOG = log.getLogger(__name__)
#CONF = config.CONF


def launch():

    app = falcon.API()
    app.req_options.strip_url_path_trailing_slash = True

    launch_tweets_api(app)

    print('Dispatcher drivers have been added to the routes!')
    return app


def launch_tweets_api(app):
    #metrics = simport.load(cfg.CONF.dispatcher.metrics)()
    trending_tweets = trending_words.Tweets()
    app.add_route("/v2.0/tweets", trending_tweets)


def get_wsgi_app():
    #if __name__ == '__main__':
    from wsgiref import simple_server
    wsgi_app = launch()
    httpd = simple_server.make_server('10.8.131.99', 8071, wsgi_app)
    httpd.serve_forever()
