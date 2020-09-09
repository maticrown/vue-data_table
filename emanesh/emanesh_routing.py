#
# Copyright (c) 2015-2016,2019 - Adjacent Link LLC, Bridgewater,
# New Jersey
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of Adjacent Link LLC nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

from .probebase import ProbeBase
#from .emanesh_routing_pb2 import Measurement_emane_transport.BroadcastPacketAcceptTable
#from .emanesh_routing_pb2 import Measurement_emane_transport.BroadcastPacketDropTable
#from .emanesh_routing_pb2 import Measurement_emane_transport.EventReceptionTable
#from .emanesh_routing_pb2 import Measurement_emane_transport.UnicastPacketAcceptTable
#from .emanesh_routing_pb2 import Measurement_emane_transport.UnicastPacketDropTable
#from .emanesh_routing_pb2 import Measurement_emane_mac.broadcastPacketAcceptTable0
#from .emanesh_routing_pb2 import Measurement_emane_mac.BroadcastPacketDropTable0
#from .emanesh_routing_pb2 import Measurement_emane_mac.BroadcastPacketDropTable0
#from .emanesh_routing_pb2 import Measurement_emane_mac.EventReceptionTable
#from .emanesh_routing_pb2 import Measurement_emane_mac.NeighborMetricTable
#from .emanesh_routing_pb2 import Measurement_emane_mac.NeighborStatusTable
#from .emanesh_routing_pb2 import Measurement_emane_mac.UnicastPacketAcceptTable
#from .emanesh_routing_pb2 import Measurement_emane_mac.UnicastPacketDropTable
#from .emanesh_routing_pb2 import Measurement_emane_phy.AntennaProfileEventInfoTable
#from .emanesh_routing_pb2 import Measurement_emane_phy.BroadcastPacketAcceptTable0
#from .emanesh_routing_pb2 import Measurement_emane_phy.BroadcastPacketDropTable0
#from .emanesh_routing_pb2 import Measurement_emane_phy.EventReceptionTable
#from .emanesh_routing_pb2 import Measurement_emane_phy.LocationEventInfoTable
#from .emanesh_routing_pb2 import Measurement_emane_phy.PathlossEventInfoTable
from .emanesh_routing_pb2 import Measurement_emane_emanesh_routing_transport
from .emanesh_routing_pb2 import Measurement_emane_emanesh_routing_mac
from .emanesh_routing_pb2 import Measurement_emane_emanesh_routing_phy

import otestpoint.toolkit.logger as Logger
from otestpoint.interface import Probe
from otestpoint.interface.measurementtable_pb2 import MeasurementTable

import time
import ntplib

import subprocess
import json
import re


from .probeprinter import output

class EMANESH_ROUTING(ProbeBase):
    def __init__(self):
        ProbeBase.__init__(self,
                           'EMANESH_ROUTING',
                           'emanesh_routing',
                           'otestpoint.emane',
                           'probe-emane-emanesh_routing.xsd')

    def build(self,probe):
        c = globals()[probe]
        p = c()
        return p

def default_method_format(self,measurement):
    return output(measurement)


class EMANESH(Probe):
    def initialize(self,configurationFile=None):
        '''
        Initialize the probe.

        Returns:
        The probe name list.
        '''
        self._logger.log(Logger.DEBUG_LEVEL,
                         '/emane/emanesh initialize'
                         ' configuration: %s' % configurationFile)

        self._measurement = Measurement_emane_emanesh_routing_transport()

        self._measurement_transport_labels = ('BroadcastPacketAcceptTable',
                                         'BroadcastPacketDropTable',
                                         'EventReceptionTable',
                                         'UnicastPacketAcceptTable',
                                         'UnicastPacketDropTable',
                                         )

        self._measurement.emanesh_routing.labels.extend(self._measurement_transport_labels)

	return ('Emane.EMANESH',)


    def start(self):
        self._logger.log(Logger.DEBUG_LEVEL,'/emane/emanesh start')


    def stop(self):
        self._logger.log(Logger.DEBUG_LEVEL,'/emane/emanesh stop')


    def destroy(self):
        self._logger.log(Logger.DEBUG_LEVEL,'/emane/emanesh destroy')


    def probe(self):
        self._logger.log(Logger.DEBUG_LEVEL,'/emane/emanesh probe')

        self.parse_transport_parameters()

        return (('Emane EMANESH',
                 self._measurement.SerializeToString(),
                 self._measurement.description.name,
                 self._measurement.description.module,
                 self._measurement.description.version),)

  #  def get_ntp_response(self):
  #      for retry in range(NTP_RETRIES):
#	    ntp_server = config.user.ntp_servers[retry % len(config.user.ntp_server)]
#	    try:
#		ntp_client=NTPClient()
#		ntp_client.request(ntp_server, version=NTP_VERSION,timeout=config.user.ntp_request_timeout)
#	    except Exception as e:
#		#logger.warning(e)
#		self._logger.log(Logger.ERROR_LEVEL,'/time/ntp error')
#		continue
 #           return response

    def parse_transport_parameters(self):
        del self._measurement.emanesh.rows[:]

	#response = get_ntp_response()


        #for key in data:
        row = self._measurement.transport.rows.add()

        dictio = EMANESH.dicto(self)

        # BroadcastPacketDropTable
        value = row.values.add()
        value.type = MeasurementTable.Measurement.TYPE_STRING
        value.sValue = dictio.get('BroadcastPacketDropTable')

        # EventReceptionTable
        value = row.values.add()
        value.type = MeasurementTable.Measurement.TYPE_STRING
        value.sValue = dictio.get('EventReceptionTable')

        # UnicastPacketAcceptTable
        value = row.values.add()
        value.type = MeasurementTable.Measurement.TYPE_STRING
        value.sValue = dictio.get('UnicastPacketAcceptTable')

        # UnicastPacketDropTable
        value = row.values.add()
        value.type = MeasurementTable.Measurement.TYPE_STRING
        value.sValue = dictio.get('UnicastPacketAcceptTable')


def default_method_format(self, measurement):
    def fromMeasurement(measurement):
        if measurement.type == MeasurementTable.Measurement.TYPE_UINTEGER:
            return measurement.uValue,str(measurement.uValue)
        elif measurement.type == MeasurementTable.Measurement.TYPE_DOUBLE:
            return measurement.dValue,'%0.2f' % measurement.dValue
        else:
            return measurement.sValue,measurement.sValue


    def format_table(table):
        buf = ''

        widths = [];

        for label in table.labels:
            widths.append(len(label))

        for row in table.rows:
            for i,value in enumerate(row.values):
                widths[i] = max(widths[i],len(fromMeasurement(value)[1]))

        for i,label in enumerate(table.labels):
            buf += '|' + label.ljust(widths[i])
        buf += "|\n"

        for row in table.rows:
            for i,value in enumerate(row.values):
                val = fromMeasurement(value)[1]
                buf += '|' + val.rjust(widths[i])
            buf += "|\n"

        return buf

    buf = '[] emanesh\n'
    buf += format_table(measurement.ntp)
    buf += '--\n'

    return buf
