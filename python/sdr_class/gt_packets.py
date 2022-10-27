#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 gr-sdr_class author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr
import pmt

class gt_packets(gr.sync_block):
    """
    docstring for block gt_packets
    """
    def __init__(self, access_code):
        gr.sync_block.__init__(self,
            name="gt_packets",
            in_sig=None,
            out_sig=None)
            
        self.message_port_register_in(pmt.intern('PDU_in'))
        self.message_port_register_out(pmt.intern('PDU_out'))
        self.set_msg_handler(pmt.intern('PDU_in'), self.handle_msg)
            
        self.access_code_list = []
        for code in access_code:
            self.access_code_list.append(ord(code))
            
        print(f"Access Code: {self.access_code_list}")
            
            
    def handle_msg(self, msg):
        inMsg = pmt.to_python (msg)
        pld = inMsg[1]
        mLen = len(pld)
        if (mLen > 0):
            char_list = self.access_code_list
            char_list.append (mLen >> 8)
            char_list.append (mLen & 255)
            char_list.append (mLen >> 8)
            char_list.append (mLen & 255)
            char_list.extend (pld)
            # print (char_list)
            out_len = len(char_list)
            # print (out_len)
            self.message_port_pub(pmt.intern('PDU_out'), pmt.cons(pmt.PMT_NIL,pmt.init_u8vector(out_len,(char_list))))


#    def work(self, input_items, output_items):
#        in0 = input_items[0]
#        out = output_items[0]
#        # <+signal processing here+>
#        out[:] = in0
#        return len(output_items[0])
