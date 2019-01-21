# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from cement.core.foundation import CementApp
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.controllers.configure_controller import ConfigureController
from jdcloud_cli.controllers.services.rds import RdsController
from jdcloud_cli.controllers.services.jke import JkeController
from jdcloud_cli.controllers.services.ams import AmsController
from jdcloud_cli.controllers.services.streamcomputer import StreamcomputerController
from jdcloud_cli.controllers.services.ipanti import IpantiController
from jdcloud_cli.controllers.services.datastar import DatastarController
from jdcloud_cli.controllers.services.oss import OssController
from jdcloud_cli.controllers.services.redis import RedisController
from jdcloud_cli.controllers.services.kms import KmsController
from jdcloud_cli.controllers.services.iam import IamController
from jdcloud_cli.controllers.services.sop import SopController
from jdcloud_cli.controllers.services.function import FunctionController
from jdcloud_cli.controllers.services.iothub import IothubController
from jdcloud_cli.controllers.services.baseanti import BaseantiController
from jdcloud_cli.controllers.services.ias import IasController
from jdcloud_cli.controllers.services.mongodb import MongodbController
from jdcloud_cli.controllers.services.live import LiveController
from jdcloud_cli.controllers.services.jdfusion import JdfusionController
from jdcloud_cli.controllers.services.clouddnsservice import ClouddnsserviceController
from jdcloud_cli.controllers.services.cps import CpsController
from jdcloud_cli.controllers.services.vpc import VpcController
from jdcloud_cli.controllers.services.monitor import MonitorController
from jdcloud_cli.controllers.services.xdata import XdataController
from jdcloud_cli.controllers.services.cdn import CdnController
from jdcloud_cli.controllers.services.cr import CrController
from jdcloud_cli.controllers.services.streambus import StreambusController
from jdcloud_cli.controllers.services.httpdns import HttpdnsController
from jdcloud_cli.controllers.services.mps import MpsController
from jdcloud_cli.controllers.services.disk import DiskController
from jdcloud_cli.controllers.services.nc import NcController
from jdcloud_cli.controllers.services.vm import VmController


class JDC(CementApp):
    class Meta:
        label = 'jdc'
        extensions = ['argcomplete']
        handlers = [BaseController]


def main():

    with JDC() as app:
        app.handler.register(ConfigureController)
        app.handler.register(RdsController)
        app.handler.register(JkeController)
        app.handler.register(AmsController)
        app.handler.register(StreamcomputerController)
        app.handler.register(IpantiController)
        app.handler.register(DatastarController)
        app.handler.register(OssController)
        app.handler.register(RedisController)
        app.handler.register(KmsController)
        app.handler.register(IamController)
        app.handler.register(SopController)
        app.handler.register(FunctionController)
        app.handler.register(IothubController)
        app.handler.register(BaseantiController)
        app.handler.register(IasController)
        app.handler.register(MongodbController)
        app.handler.register(LiveController)
        app.handler.register(JdfusionController)
        app.handler.register(ClouddnsserviceController)
        app.handler.register(CpsController)
        app.handler.register(VpcController)
        app.handler.register(MonitorController)
        app.handler.register(XdataController)
        app.handler.register(CdnController)
        app.handler.register(CrController)
        app.handler.register(StreambusController)
        app.handler.register(HttpdnsController)
        app.handler.register(MpsController)
        app.handler.register(DiskController)
        app.handler.register(NcController)
        app.handler.register(VmController)

        app.run()
