#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from lmnotify import LaMetricManager


def main():
    # create an instance of the LaMetricManager
    lmn = LaMetricManager()

    # get devices
    devices = lmn.get_devices()

    # use first device to do some tests
    lmn.set_device(devices[0])

    # turn on radio
    lmn.radio_play()

    # listen for a few seconds
    time.sleep(5)

    # switch channel
    lmn.radio_next()

    # listen for again for a few seconds
    time.sleep(5)

    # turn radio off
    lmn.radio_stop()


if __name__ == "__main__":
    main()
